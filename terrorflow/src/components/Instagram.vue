<template>
  <form>

  <div class="imagedrop" :class="{selected: instagramSelected}" style="position: relative">

    <div v-if="!instagramSelected" class="animated fadeIn" style="width: 100%">
      <p class="sm-header"><i class="fa fa-instagram"></i> Instagram</p>
      <input v-on:keydown.enter="submitInstagram" class="sm-bar" type="text" placeholder="Enter Instagram username.." id="instagramProfile">

    </div>

    <div v-if="instagramSelected" class="animated fadeIn" style="width: 100%; height: 100%;">
    <img @click="getInstagramPredictions(index)" class="tileimage" v-for="(img, index) in instagramImages" :src="img" height="49.5%" width="33%" style="object-fit: cover; padding:5px;">
    </div>

    </div>
  </form>
</template>

<style>

.sm-header {
    font-size: 1.8em !important;
    margin-bottom: 19px !important;
}

input.sm-bar {
    width: 80%;
    height: 50px;
    font-size: 0.95em;
}

.tileimage {
    transition: filter 200ms ease-in-out;
    filter: grayscale(55%);
    z-index: 0;
    border-radius: 15px;
    overflow: hidden;
}

.tileimage:hover {
    transform: scale(1.2);
    z-index: 100;
    position: relative;
    cursor: pointer;
    filter: grayscale(0%);
    
}
</style>

<script>

export default {
    props: ['submitInstagram', 'instagramImages', 'getInstagramPredictions', 'instagramSelected'],
    data: function() {
        return {
        }
    }
}


</script>