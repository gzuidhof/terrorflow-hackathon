<template>
  <form>

  <div class="imagedrop" :class="{selected: youtubeSelected, ytSelected: youtubeSelected}" style="position: relative">

    <div v-if="!youtubeSelected" class="animated fadeIn"style="width: 100%">
      <p class="sm-header"><i class="fa fa-youtube"></i> YouTube</p>
      <input v-on:keydown.enter="submitYoutube" class="sm-bar" type="text" placeholder="Enter YouTube link.." id='ytInput'>

    </div>

    <div class='frames'>
    <span v-for="(frame, index) in youtubeFrames" @click="showYTFrame(index)" v-if="youtubeSelected" class="frame-selector">
    <i class="fa fa-dot-circle-o"></i>
    </span>
    </div>

    <iframe v-if="youtubeSelected" id="ytplayer" type="text/html" width="790" height="360"
    :src="youtubeUrl.replace('watch?v=', 'embed/') + '?autoplay=1'" frameborder="0"></iframe>
    </div>
  </form>
</template>


<script>

export default {
    props: ['youtubeUrl', 'submitYoutube', 'youtubeSelected', 'youtubeFrames', 'showYoutubePred'],
    data: function() {
        return {
        }
    },
    methods: {
        showYTFrame(i) {
            console.log('showing frame ' + i);
            this.showYoutubePred(this.youtubeFrames[i]);
        }
    }
}


</script>

<style>

.frame-selector {
  font-size: 1.4em;
  vertical-align: middle;
  cursor: pointer;
  transition: all 100ms ease-in-out;
}

.frame-selector:hover {
  color: #ddd;
  font-size: 1.41em;
}

.frames {
    display: flex;
    width: 94%;
    justify-content: space-between;
    position: absolute;
    bottom: 60px;
}

.ytSelected {
    box-shadow: none;
}

.ytborder {
    border: none;
    background-color: transparant;
}

.sm-header {
    font-size: 1.8em !important;
    margin-bottom: 19px !important;
}

input.sm-bar {
    width: 80%;
    height: 50px;
    font-size: 0.95em;
}

</style>