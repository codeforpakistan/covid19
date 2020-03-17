import Vue from 'vue'
import App from './App.vue'
import Axios from 'axios'

Axios.defaults.baseURL = 'https://corona.nhsrc.gov.pk:8000/api/'
// Axios.interceptors.request.use(
//   (config) => {
//     let token = store.state.token
//     if (token) config.headers['Authorization'] = `Token ${token}`
//     return config
//   }, (error) => { return Promise.reject(error) }
// )
Axios.defaults.headers.common['Authorization'] = `Token 4f976f416bf1bbacff0d64d2f2f796e15f322d07` 
Axios.defaults.xsrfCookieName = 'csrftoken'
Axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false


new Vue({
  render: h => h(App),
}).$mount('#app')
