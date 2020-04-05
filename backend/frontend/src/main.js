// Third-party packages
import Vue from 'vue'
import App from './App.vue'
import router from './router'

// Third-party packages
import AOS from 'aos'
import Buefy from 'buefy'

// CSS
import 'aos/dist/aos.css'
import 'buefy/dist/buefy.css'
import 'bulma/css/bulma.css';



Vue.config.productionTip = false
Vue.use(Buefy)

var VueScrollTo = require('vue-scrollto');
Vue.use(VueScrollTo, {
  duration: 1200,
})

new Vue({
  created() {
    AOS.init({
      once: true
    })
  },
  router,
  render: h => h(App)
}).$mount('#app')
