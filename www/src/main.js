import Vue from 'vue'
import App from './App.vue'
import Axios from 'axios'
import './filters'

Axios.defaults.baseURL = process.env.VUE_APP_SERVER
// Axios.interceptors.request.use(
//   (config) => {
//     config.headers['Authorization'] = `Token ${process.env.VUE_APP_TOKEN}` 
//     return config
//   }, (error) => { return Promise.reject(error) }
// )
Axios.defaults.xsrfCookieName = 'csrftoken'
Axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false


new Vue({
  render: h => h(App),
}).$mount('#app')
