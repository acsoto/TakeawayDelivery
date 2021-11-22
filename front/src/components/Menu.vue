<template>
  <a-layout-sider v-model="collapsed" collapsible @collapse="handleCollapse">

    <div class="logo" />
    <a-menu theme="dark" :default-selected-keys="['1']" mode="inline">
      <a-sub-menu key="sub1">
        <template v-slot:title>
          <i class="el-icon-user"   />
          <!--            <icon type="pie-chart" />-->
          <span v-if="collapsed">个人中心</span>
        </template>
        <a-menu-item key="1">
          <!--          <i class="el-icon-delete"></i>-->
          <router-link to="/home/userinfo">
            个人信息
          </router-link>
        </a-menu-item>
        <a-menu-item key="2">

          <router-link to="/home/test">
            订单查询
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          我的最爱
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
          用户登出
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub2">
        <template v-slot:title>
          <a-icon type="desktop" />
          <i class="el-icon-shopping-cart-full"  />
          <span v-if="collapsed">商铺</span>
        </template>
        <a-menu-item key="8">
          学一食堂
        </a-menu-item>
        <a-menu-item key="9">
          学二食堂
        </a-menu-item>
        <a-menu-item key="10">
          学三食堂
        </a-menu-item>
        <a-menu-item key="11">
          学四食堂
        </a-menu-item>
        <a-menu-item key="12">
          学五食堂
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub3">
        <template v-slot:title><a-icon type="user" />
          <i class="el-icon-chat-line-round"  />
          <span v-if="collapsed">讨论区</span>
        </template>
        <a-menu-item key="13">
          菜品贴
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
          <i class="el-icon-bicycle"  />
          <span v-if="collapsed">我接的单</span>
        </template>
        <a-menu-item key="16">
          当前订单
        </a-menu-item>
        <a-menu-item key="17">
          历史订单
        </a-menu-item>
      </a-sub-menu>
      <a-menu-item key="18">
        <a-icon type="file" />
        <span>暂未想好写什么的一栏</span>
      </a-menu-item>
    </a-menu>
  </a-layout-sider>
  <!--    <a-layout-header style="background: #fff; padding: 0">-->
  <!--      <i class="el-icon-back" @click="() => (collapsed = !collapsed)" />-->
  <!--    </a-layout-header>-->

</template>

<script>
export default {
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
  }
}
</script>

<style scoped>

</style>
