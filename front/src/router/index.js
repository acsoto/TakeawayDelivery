import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/login'
    //输入前面的ip地址+端口号立刻会跳转到/login,可以理解为初始界面
  },
  {
    path: '/login',
    name: 'Login', //注意，path和name都是绝对不准重复的
    component: () =>
      import(
        /* webpackChunkName: "login" */
        '../views/Login.vue'
      )
  },

  {
    path: '/register',
    name: 'Register',
    component: () =>
      import(
        /* webpackChunkName: "login" */
        '../views/Register.vue'
      )
  },
  {
    path: '/home',
    name: 'Home',
    redirect: '/home/userinfo',
    component: () =>
      import(
        /* webpackChunkName: "login" */
        '../views/Home.vue'
      ),
    children: [
      {
        path: 'test',
        name: 'test',
        meta: {
          title: '个人中心',
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/test')
      },
      {
        path: 'userinfo',
        name: 'userinfo',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/UserInfo')
      },
      {
        path: 'orderquery',
        name: 'orderquery',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/OrderQuery')
      },
      {
        path: 'userstar',
        name: 'userstar',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/UserStar')
      },
        {
        path: 'hotfood',
        name: 'hotfood',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/HotFood')
      },

      {
        path: 'restaurants',
        name: 'restaurants',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/RestaurantList')
      },
      {
        path: 'restaurant',
        name: 'restaurant',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/Restaurant')
      },
      {
        path: 'food',
        name: 'food',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/Food')
      },
      {
        path: 'user',
        name: 'user',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/User')
      },
      {
        path: 'discussion',
        name: 'discussion',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/Discussion')
      },
      {
        path: 'ordernow',
        name: 'ordernow',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/OrderNow')
      },
      {
        path: 'orders',
        name: 'orders',
        meta: {
          keepAlive: true,
          reqsuireAuth: true
        },
        component: () => import('../views/Orders')
      },
      {
        path: 'developmentteam',
        name: 'developmentteam',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/DevelopmentTeam')
      },
      {
        path: 'template',
        name: 'template',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/template')
      },
      {
        path: 'discussionme',
        name: 'discussionme',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/DiscussionMe')
      },
      {
        path: 'mydiscussion',
        name: 'mydiscussion',
        meta: {
          keepAlive: true,
          requireAuth: true
        },
        component: () => import('../views/MyDiscussion')
      }
      // {
      //   path: "",
      //   name: "",
      //   meta: {
      //     keepAlive: true
      //   },
      //   component: () => import("")
      // },
    ]
  },
  {
    path: '/zoumadeng',
    name: 'Zoumadeng',
    component: () => import('../views/zoumadeng')
  }
  // {
  //   path: "/test",
  //   name: "test",
  //   component: () =>
  //       import(
  //           "../views/test"
  //           ),
  //   children: [
  //     {
  //       path: "/zoumadeng",
  //       name: "zoumadeng",
  //       meta: {
  //         title: '个人中心',
  //         requireAuth: true,
  //         keepAlive: true
  //       },
  //       component: () => import("../views/zoumadeng")
  //     },
  //   ],
  // }
  //一个父子组件的案例
  // {
  //   path: "/",
  //   name: "Home", //Home组件里包括了初始的导航栏和侧边栏的样式，它的所有children都会共享Home里的导航栏、侧边栏
  //   component: () =>
  //     import(
  //       /* webpackChunkName: "login" */
  //       "../views/Home.vue"
  //     ),
  //   children: [
  //     // {
  //     //     path: "user",
  //     //     name: "user",
  //     //     meta: {
  //     //         title: '个人中心',
  //     //         requireAuth: true,
  //     //         keepAlive: true
  //     //     },
  //     //     component: () => import("../views/User.vue")
  //     // },
  //   ],
  // },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
