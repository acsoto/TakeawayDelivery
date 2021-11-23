import { createRouter, createWebHistory } from "vue-router";


const routes = [
  {
    path: "/",
    redirect: "/home",
    //输入前面的ip地址+端口号立刻会跳转到/login,可以理解为初始界面
  },
  {
    path: "/login",
    name: "Login", //注意，path和name都是绝对不准重复的
    component: () =>
      import(
        /* webpackChunkName: "login" */
        "../views/Login.vue"
      ),
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(
        /* webpackChunkName: "login" */
        "../views/Register.vue"
      ),
  },
  {
    path: "/home",
    name: "Home",
    component: () =>
      import(
        /* webpackChunkName: "login" */
        "../views/Home.vue"
      ),
    children: [
        {
          path: "test",
          name: "test",
          meta: {
            title: '个人中心',
            keepAlive: true
          },
          component: () => import("../views/test")
        },
      {
        path: "userinfo",
        name: "userinfo",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/UserInfo")
      },
      {
        path: "orderquery",
        name: "orderquery",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/OrderQuery")
      },
      {
        path: "userstar",
        name: "userstar",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/UserStar")
      },
      {
        path: "restaurant1",
        name: "restaurant1",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/Restaurant1")
      },
      {
        path: "restaurant2",
        name: "restaurant2",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/Restaurant2")
      },
      {
        path: "restaurant3",
        name: "restaurant3",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/Restaurant3")
      },
      {
        path: "restaurant4",
        name: "restaurant4",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/Restaurant4")
      },
      {
        path: "restaurant5",
        name: "restaurant5",
        meta: {
          keepAlive: true
        },
        component: () => import("../views/Restaurant5")
      },
      ],
  },
  {
    path: "/zoumadeng",
    name: "Zoumadeng",
    component: () =>
        import(
            "../views/zoumadeng"
            ),
  },
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
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
