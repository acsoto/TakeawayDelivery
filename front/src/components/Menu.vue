<template>
  <a-layout-sider
    v-model="collapsed"
    collapsible
    @collapse="handleCollapse"
    :style="{ overflow: 'auto', height: '100vh', left: 0 }"
  >

    <div class="logo" />
    <a-menu
      theme="dark"
      mode="inline"
    >
      <template
        v-for="item in items"
        :key="item"
      >
        <template v-if="item.subs">
          <a-sub-menu :key="item">
            <template #title>
              <UserOutlined v-if="item.icon=='UserOutlined'" />
              <ShoppingCartOutlined v-if="item.icon=='ShoppingCartOutlined'" />
              <CommentOutlined v-if="item.icon=='CommentOutlined'" />
              <CarOutlined v-if="item.icon=='CarOutlined'" />
              <CoffeeOutlined v-if="item.icon=='CoffeeOutlined'" />
              <SettingOutlined v-if="item.icon=='SettingOutlined'" />
              <span v-if="collapsed">{{ item.title }}</span>
            </template>
            <template
              v-for="subItem in item.subs"
              :key="subItem"
            >
              <a-menu-item :index="subItem.index">
                <router-link :to="subItem.to">{{ subItem.title }}</router-link>
              </a-menu-item>
            </template>
          </a-sub-menu>
        </template>
      </template>
    </a-menu>
  </a-layout-sider>
</template>

<script>
import { defineComponent, reactive, ref } from 'vue';
import { UserOutlined, ShoppingCartOutlined, CommentOutlined, CarOutlined, CoffeeOutlined, SettingOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  name: "Menu",
  data() {
    return {
      collapsed: true,
      items: [
        {
          icon: "UserOutlined",
          title: "个人中心",
          subs: [
            {
              to: "/home/userinfo",
              title: "个人信息"
            },
            {
              to: "/home/orderquery",
              title: "我的订单"
            },
            {
              to: "/home/userstar",
              title: "我的最爱"
            },
            {
              to: "/login",
              title: "用户注销"
            },
            {
              to: "/login",
              title: "用户登出"
            },
          ]
        },
        {
          icon: "ShoppingCartOutlined",
          title: "商铺",
          subs: [
            {
              to: "/home/restaurants",
              title: "所有餐厅"
            },]

        },
        {
          icon: "CarOutlined",
          title: "订单查询",
          subs: [
            {
              to: "/home/ordernow",
              title: "我接的单"
            },
            {
              to: "/home/orders",
              title: "全部订单"
            },
          ]
        },
        {
          icon: "SettingOutlined",
          title: "系统设置",
          subs: [
            {
              to: "/home/developmentteam",
              title: "开发团队"
            },]
        },
      ]
    };
  },
  methods: {
    handleCollapse(collapsed) {
      this.collapsed = !this.collapsed;
    },
  },
  components: {
    UserOutlined,
    ShoppingCartOutlined,
    CommentOutlined,
    CarOutlined,
    CoffeeOutlined,
    SettingOutlined,
  },

});
</script>

<style scoped>
.icons-list :deep(.anticon) {
  margin-right: 6px;
  font-size: 24px;
}
::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 0px; /*高宽分别对应横竖滚动条的尺寸*/
  height: 0px; /*没想到吧，滚动条直接被我进行了一个横竖都调成0的动作，虽然可以用但是页面上完全看不到，名存实亡的概念！*/
}
</style>
