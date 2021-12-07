import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/icon.css'
import installAxios from './plugins/axios'

import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import 'ant-design-vue/lib'
const app = createApp(App)
installAxios(app)

app
  .use(store)
  .use(router)

  .use(Antd)
  .mount('#app')

router.beforeEach((to, from, next) => {
  if (to.matched.some(res => res.meta.requireAuth)) {
    if (store.state.islogin) {
      next()
    } else {
      next({ path: '/login' })
    }
  } else {
    next()
  }
})
