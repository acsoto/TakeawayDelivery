<template>
  <a-layout id="components-layout-demo-side" style="min-height: 100vh">
    <a-layout-sider v-model="collapsed" collapsible>
      <div class="logo" />
      <a-menu theme="dark" :default-selected-keys="['1']" mode="inline">
        <a-sub-menu key="sub1">
          <template v-slot:title>
            <a-icon type="pie-chart" ></a-icon>
            <span>个人中心</span>
          </template>
          <a-menu-item key="1">
            <!--          <i class="el-icon-delete"></i>-->
            个人信息
          </a-menu-item>
          <a-menu-item key="2">
            订单查询
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
            <span>商铺</span>
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
          <template v-slot:title><a-icon type="user" /><span>讨论区</span></template>
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
          <template v-slot:title><a-icon type="team" /><span>我接的单</span></template>
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
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0" />
      <a-layout-content style="margin: 0 16px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>User</a-breadcrumb-item>
          <a-breadcrumb-item>Bill</a-breadcrumb-item>
        </a-breadcrumb>
        <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
<!--          Bill is a cat.-->
            <el-carousel :interval="4000" type="card" height="200px">
              <el-carousel-item v-for="item in 6" :key="item">
                <h3 class="medium">{{ item }}</h3>
              </el-carousel-item>
            </el-carousel>
        </div>
      </a-layout-content>
      <a-layout-footer style="text-align: center">
<!--        Ant Design ©2018 Created by Ant UED-->
        ©2021 Powered by zzh company
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script>
export default {
  data() {
    return {
      collapsed: false,
    };
  },
};
</script>

<style>
#components-layout-demo-side .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
