import { createRouter, createWebHistory } from "vue-router";


const routes = [
  {
    path: "/",
    redirect: "/test",
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
  },
  {
    path: "/test",
    name: "Test",
    component: () =>
        import(
            "../views/test"
            ),
  },
  {
    path: "/zoumadeng",
    name: "Zoumadeng",
    component: () =>
        import(
            "../views/zoumadeng"
            ),
  }
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
