<template>
  <form v-on:submit.prevent>

  <div @dragover.prevent @drop.prevent="drop" class="imagedrop" :class="{selected: imageSelected}" style="position: relative">

    <div v-if="!imageSelected" class="animated fadeIn">
      <p>drop an image</p>
      <p class="or">--- or ---</p>
        <input class="inputfile" v-on:change="submitteroni" type="file" id="imageInput" value="Upload image">
        <label for="imageInput">Choose a file</label>
    </div>

      <img @click="switchToResults" v-if="imageSelected" class="super-img animated fadeIn" :src="imageUrl" style="z-index: 0; position: absolute; left:0px; top:0px; width: 100%; height:100%; object-fit: cover;" ></img>
      <!-- <input v-if="imageSelected" class="my-button" type="submit" style="z-index: 1; margin-top: 20px;"value="Upload image"> -->

    </div>
  </form>
</template>

<script>

export default {
    props: ['imageUrl', 'submitteroni', 'imageSelected', 'switchToResults'],
    data: function() {
        return {
        }
    },
    methods: {

      drop: function(ev) {
          var input = document.getElementById('imageInput');
          console.log(ev.dataTransfer);
          input.files = ev.dataTransfer.files;
      }
    }
}



</script>