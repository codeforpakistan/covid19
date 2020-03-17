import Vue from 'vue'
import App from './App.vue'
import Axios from 'axios'

Axios.defaults.baseURL = process.env.VUE_APP_SERVER
Axios.defaults.headers.common['Authorization'] = `Token ${process.env.VUE_APP_TOKEN}` 
Axios.defaults.xsrfCookieName = 'csrftoken'
Axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false


new Vue({
  render: h => h(App),
}).$mount('#app')
