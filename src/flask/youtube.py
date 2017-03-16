import cv2
import os
import youtube_dl
from subprocess import call
import glob


if not os.path.isdir('../../data/videos/'):
    os.mkdir('../../data/videos/')
DATA_DIR = '../../data/videos/'


def video_to_frames(filename):
    call(["/home/ubuntu/bin/ffmpeg", "-i", DATA_DIR + filename, "-vf", "fps=1/20", DATA_DIR + filename + "part%03d.jpg"])
    filenames = glob.glob(DATA_DIR + filename + "part*.jpg")
    # print (DATA_DIR + filename)
    # vidcap = cv2.VideoCapture(DATA_DIR + filename)
    # frames=vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    # print(frames)
    # filenames=[]
    # for i in range(1,11):
    #     vidcap.set(cv2.CAP_PROP_POS_FRAMES, frames/10*float(i))
    #     success,image = vidcap.read()
    #     savename= DATA_DIR + "{filename}part{part}.jpg".format(filename=filename, part=i)
    #     cv2.imwrite(savename, image)     # save frame as JPEG file
    #     filenames.append(savename)
    return filenames


def download_youtube_video(video_url):
    filename = video_url.split('=')[1] + ".mp4"
    print(filename)
    ydl_opts = {'outtmpl': '../../data/videos/%(id)s.%(ext)s', 'prefer_insecure': True, 'nocheckcertificate': True, 'format': '134'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return filename

# filename = download_youtube_video('http://www.youtube.com/watch?v=3tRF2FxPrj8')
# filename='3tRF2FxPrj8.mp4'
# print(video_to_frames(filename))


def main(url):
    filename = download_youtube_video(url)
    return video_to_frames(filename)