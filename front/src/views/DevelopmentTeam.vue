<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0" >
    </a-layout-header>
    <a-layout-content style="margin: 0 16px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>系统设置</a-breadcrumb-item>
        <a-breadcrumb-item>开发团队</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
        <!--        TODO-->
        <div>
          <a-carousel arrows dots-class="slick-dots slick-thumb">
            <template #customPaging="props">
              <a>
                <img :src="getImgUrl(props.i)" />
              </a>
            </template>
            <div v-for="item in 4" :key="item">
              <img :src="baseUrl + 'abstract0' + item + '.jpg'" />
            </div>
          </a-carousel>
        </div>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>
<script>
import { defineComponent } from 'vue';
const baseUrl = 'https://raw.githubusercontent.com/vueComponent/ant-design-vue/next/components/vc-slick/assets/img/react-slick/';
export default defineComponent({
  data() {
    return {
      collapsed: true,
    };
  },
  methods:{
  },
  setup() {
    const getImgUrl = i => {
      return `${baseUrl}abstract0${i + 1}.jpg`;
    };
    return {
      baseUrl,
      getImgUrl,
    };
  },
});
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
</style>
