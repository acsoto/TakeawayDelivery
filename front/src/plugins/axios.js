'use strict'

import axios from 'axios'

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || ''
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

let config = {
  //baseURL: 'http://localhost:8000/',
  baseURL: 'http://42.192.60.125:80/',
  timeout: 60 * 1000, // Timeout
  withCredentials: true // Check cross-site Access-Control
}

// 创建Axios对象
const Axios = axios.create(config)

// 请求拦截器
Axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error)
  }
)

// 响应拦截器
Axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response
  },
  function(error) {
    // Do something with response error
    return Promise.reject(error)
  }
)

export default app => {
  // 挂载axios到Vue对象
  app.config.globalProperties.$http = Axios
}
