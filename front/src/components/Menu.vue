<template>
  <a-layout-sider v-model="collapsed" collapsible @collapse="handleCollapse" :style="{ overflow: 'auto', height: '100vh', left: 0 }">

    <div class="logo" />
    <a-menu theme="dark" :default-selected-keys="['1']" mode="inline">
      <a-sub-menu key="sub1">
        <template v-slot:title>
          <UserOutlined />
          <span v-if="collapsed">个人中心</span>
        </template>
        <a-menu-item key="1">
          <router-link to="/home/userinfo">
            个人信息
          </router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="/home/orderquery">
            订单查询
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <router-link to="/home/userstar">
            我的最爱
          </router-link>
        </a-menu-item>
        <a-menu-item key="4">
          修改信息
        </a-menu-item>
        <a-menu-item key="5">
          修改密码
        </a-menu-item>
        <a-menu-item key="6">
          用户注销
        </a-menu-item>
        <a-menu-item key="7">
          <router-link to="/login">
            用户登出
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub2">
        <template v-slot:title>
          <a-icon type="desktop" />
          <ShoppingCartOutlined />
          <span v-if="collapsed">商铺</span>
        </template>
        <a-menu-item key="8">
          <router-link to="/home/restaurant1">
            学一食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="9">
          <router-link to="/home/restaurant2">
            学二食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="10">
          <router-link to="/home/restaurant3">
            学三食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="11">
          <router-link to="/home/restaurant4">
            学四食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="12">
          <router-link to="/home/restaurant5">
            学五食堂
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub3">
        <template v-slot:title><a-icon type="user" />
          <CommentOutlined />
          <span v-if="collapsed">讨论区</span>
        </template>
        <a-menu-item key="13">
          <router-link to="/home/discussion">
            菜品贴
          </router-link>
        </a-menu-item>
        <a-menu-item key="14">
          与我有关的
        </a-menu-item>
        <a-menu-item key="15">
          我发布的
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub4">
        <template v-slot:title><a-icon type="team" />
          <CarOutlined />
          <span v-if="collapsed">我接的单</span>
        </template>
        <a-menu-item key="16">
          当前订单
        </a-menu-item>
        <a-menu-item key="17">
          历史订单
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub5">
        <template v-slot:title><a-icon type="team" />
          <SettingOutlined />
          <span v-if="collapsed">系统设置</span>
        </template>
        <a-menu-item key="18">
          开发团队
        </a-menu-item>
      </a-sub-menu>
      <a-menu-item key="19">
        <CoffeeOutlined />
        <span>暂未想好写什么的一栏</span>
      </a-menu-item>
    </a-menu>
  </a-layout-sider>
  <!--    <a-layout-header style="background: #fff; padding: 0">-->
  <!--      <i class="el-icon-back" @click="() => (collapsed = !collapsed)" />-->
  <!--    </a-layout-header>-->

</template>

<script>
import { defineComponent } from 'vue';
import { UserOutlined, ShoppingCartOutlined, CommentOutlined, CarOutlined, CoffeeOutlined, SettingOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  name: "Menu",
  data() {
    return {
      collapsed: true,
    };
  },
  methods:{
    handleCollapse(collapsed){
      console.log(collapsed);
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
</style>
