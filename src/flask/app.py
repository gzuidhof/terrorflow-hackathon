import os
from flask import Flask, request, redirect, flash, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask.ext.cors import CORS, cross_origin

from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

import tensorflow as tf

import numpy as np

from instascraper import scrape_user
import youtube

UPLOAD_FOLDER = '../../data/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

if not os.path.isdir('../../data'):
    os.mkdir('../../data')
    os.mkdir('../../data/uploads')

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['CORS_HEADERS'] = 'Content-Type'

local_data = {}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify(success=True, filename=filename)


def predict(filename):
    img = load_img(filename, target_size=(384, 384))
    img = img_to_array(img)
    img = preprocess_input(np.expand_dims(img, 0)) / 255.

    with tf.device("/gpu:0"):
        with local_data['graphs']['vgg'].as_default():
            vgg_features = np.expand_dims(local_data['models']['vgg'].predict(img).flatten(), 0)

    predictions = {}
    for name, (model, gpu) in local_data['models']['dense'].iteritems():
        with tf.device("/gpu:{}".format(gpu)):
            with local_data['graphs']['dense'][name].as_default():
                predictions[name.replace(".hdf5", "")] = model.predict(vgg_features)[0][0].astype(np.float64)

    predictions['neonazi'] *= 0.25
    return predictions


@app.route('/classify/<filename>')
def classify(filename):
    classes = predict(UPLOAD_FOLDER + filename)
    return jsonify(classes=classes, filename=filename)


@app.route('/classify_instagram/<username>')
def classify_instagram(username):
    classes, filenames = {}, []
    filenames = scrape_user([username], 10)
    for file in filenames:
        classs = predict(file)
        classes[file.replace("../../data/instagram_users/", "")] = classs

    filenames = map(lambda x: x.replace("../../data/instagram_users/", ""), filenames)
    return jsonify(classes=classes, filenames=filenames, username=username)


@app.route('/classify_video/<url>')
def classify_video(url):
    classes, filenames = {}, []
    filenames = youtube.main("http://www.youtube.com/watch?v=" + url)
    for file in filenames:
        classs = predict(file)
        classes[file.replace("../../data/videos/", "")] = classs

    filenames = map(lambda x: x.replace("../../data/videos/", ""), filenames)
    return jsonify(classes=classes, filenames=filenames, videourl=url)


@app.route('/')
def hello_world():
    return '200 OK'


@app.route('/static/uploads/<path:path>')
def send_static(path):
    return send_from_directory('../../data/uploads', path)


@app.route('/static/instagram_users/<path:user>/<path:path>')
def send_static_instagram(user, path):
    return send_from_directory('../../data/instagram_users/{}'.format(user), path)


@app.route('/static/videos/<path:path>')
def send_static_videos(path):
    return send_from_directory('../../data/videos', path)


def load_models():
    local_data['models'] = {}
    local_data['graphs'] = {}
    local_data['models']['dense'] = {}
    local_data['graphs']['dense'] = {}

    with tf.device("/gpu:0"):
        local_data['models']['vgg'] = VGG16(include_top=False, input_shape=(384, 384, 3))
        local_data['graphs']['vgg'] = tf.get_default_graph()

    for i, filename in enumerate(['arabic_sign.hdf5', 'army.hdf5', 'burning_flag.hdf5', 'desert.hdf5', 'dutch_flag.hdf5', 'islam.hdf5', 'islamic_state.hdf5', 'middle_east.hdf5', 'neonazi.hdf5', 'rifles.hdf5']):
        gpu = (i % 7) + 1
        with tf.device("/gpu:{}".format(gpu)):
            print "Loading model {} to GPU {}".format(filename, gpu)
            local_data['models']['dense'][filename] = (load_model("../../models/" + filename), gpu)
            local_data['graphs']['dense'][filename] = tf.get_default_graph()


if __name__ == "__main__":
    # Load model into global alles
    load_models()

    app.debug = False
    app.secret_key = 'joress'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host="0.0.0.0", port=8080, use_reloader=False)
