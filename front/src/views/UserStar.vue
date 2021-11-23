<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0" >
    </a-layout-header>
    <a-layout-content style="margin: 0 16px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>个人中心</a-breadcrumb-item>
        <a-breadcrumb-item>我的最爱</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
        <a-row type="flex" justify="space-around">
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©2021 Powered by zzh company
    </a-layout-footer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      collapsed: true,
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
