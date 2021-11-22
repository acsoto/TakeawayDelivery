import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import installElementPlus from './plugins/element'
import './assets/css/icon.css'
import installAxios from './plugins/axios'
import ElementUI from 'element-plus'
import 'element-plus/lib/theme-chalk/index.css'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import 'ant-design-vue/lib'
import * as echarts from 'echarts'
const app = createApp(App)
installElementPlus(app)
installAxios(app)
app.config.globalProperties.$echarts = echarts
app
    .use(store)
    .use(router)
    .use(ElementUI)
    .use(Antd)
    .mount('#app');

router.beforeEach((to, from, next) => {
    if(to.matched.some(res => res.meta.requireAuth)){
        if(store.state.islogin){
            next();
        }
        else{
            next({path: '/login',
            query: {redirect: to.fullPath}
        });

        }
    }
    else{
        next();
    }
});
