<script>
import {PolarArea} from 'vue-chartjs'

export default PolarArea.extend({
  data () {
      return {
        dataCollection: {
            labels: ['Arabic Sign', 'Army', 'Burning Flag', 'Desert', 'Dutch', 'Islam', 'Islamic State', 'Middle East', 'Neo-Nazi', 'Rifles'],
            datasets: [{
                label: 'Risk factors',
                backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)'

                ],
                data: [this.pred['arabic_sign'],this.pred['army'],this.pred['burning_flag'],
                this.pred['desert'],this.pred['dutch_flag'],this.pred['islam'],
                this.pred['islamic_state'],this.pred['middle_east'],this.pred['neonazi'],this.pred['rifles']]//[100,0.6,25, 0.6, 0.5, 0.3, 18, 0.9, 0.5, 0.1]
            }]
        
        }
      }
  },
  mixins: [],
  props: ['options', 'pred'],
  mounted () {
    // this.chartData is created in the mixin
    this.renderChart(this.dataCollection, this.options)
    console.log('MountResults', this.pred);
    //console.log("On mount preds:", this.pred)
  }
})


</script>

<style>

</style>