import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Image from '@/components/Image'
import Youtube from '@/components/Youtube'
import Instagram from '@/components/Instagram'
import ResultsChart from '@/components/ResultsChart'
import Results from '@/components/Results'

Vue.use(Router)
Vue.component('image-selector', Image)
Vue.component('youtube-selector', Youtube)
Vue.component('instagram-selector', Instagram)
Vue.component('results-chart', ResultsChart)
Vue.component('results', Results)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    }
  ]
})
