<template>
  <div class="sidebar">
    <el-menu
      class="sidebar-el-menu"
      :default-active="onRoutes"
      :collapse="collapse"
      background-color="#324157"
      text-color="#bfcbd9"
      active-text-color="#20a0ff"
      unique-opened
      router
    >
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-submenu :index="item.index" :key="item.index">
            <template #title>
              <i :class="item.icon"></i>
              <span>{{ item.title }}</span>
            </template>
            <template v-for="subItem in item.subs">
              <el-submenu
                v-if="subItem.subs"
                :index="subItem.index"
                :key="subItem.index"
              >
              
                <template #title >{{ subItem.title }}</template>
                <el-menu-item
                  v-for="(threeItem, i) in subItem.subs"
                  :key="i"
                  :index="threeItem.index"
                >
                  {{ threeItem.title }}
                </el-menu-item>
              </el-submenu>
              <el-menu-item
                v-else
                :index="subItem.index"
                :key="subItem.index"
                >{{ subItem.title }}</el-menu-item
              >
            </template>
          </el-submenu>
        </template>
        <template v-else>
          <el-menu-item :index="item.index" :key="item.index">
            <i :class="item.icon"></i>
            <template #title>{{ item.title }}</template>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          icon: "el-icon-user",
          title: "个人中心",
          subs: [
            {
              index: "user",
              title: "个人信息",
            },
            {
              index: "showReserveBook",
              title: "已预约图书",
              role: 1,
            },
            {
              index: "showReturnedBook",
              title: "已归还图书",
              role: 1,
            },
            {
              index: "showTobeList",
              title: "在借图书",
              role: 1,
            },
          ],
        },
        {
          icon: "el-icon-search",
          index: "search",
          title: "图书检索",
        },
        {
          icon: "el-icon-view",
          index: "popularbook",
          title: "图书推荐",
        },
        {
          icon: "el-icon-bell",
          index: "Notification",
          title: "最新通知",
        },
        {
          icon: "el-icon-info",
          index: "about",
          title: "关于本馆",
        },
      ],
    };
  },
  methods: {},
  computed: {
    onRoutes() {
      return this.$route.path.replace("/", "");
    },
    collapse() {
      return this.$store.state.collapse;
    },
    Role() {
      let role = this.$store.state.role;
      return role;
    },
  },
};
</script>

<style scoped>
.sidebar {
  display: block;
  position: absolute;
  left: 0;
  top: 70px;
  bottom: 0;
  overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
  width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
  width: 250px;
}
.sidebar > ul {
  height: 100%;
}
</style>
