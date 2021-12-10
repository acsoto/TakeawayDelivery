<template>
  <div>
    <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
      <a-carousel
        arrows
        dots-class="slick-dots slick-thumb"
        autoplay="true"
      >
        <template #customPaging="props">
          <a>
            <!--                //有bug的函数-->
            <img
              v-if="props.i==0"
              style="width:40px;height:30px;"
              src="@/assets/img/1.jpg"
            >

            <img
              v-if="props.i==1"
              style="width:40px;height:30px;"
              src="@/assets/img/2.jpg"
            >

            <img
              v-if="props.i==2"
              style="width:40px;height:30px;"
              src="@/assets/img/3.jpg"
            >

            <img
              v-if="props.i==3"
              style="width:40px;height:30px;"
              src="@/assets/img/4.jpg"
            >
          </a>
        </template>
        <!--            <div v-for="item in 4" :key="item">-->
        <!--              <img :src="baseUrl + 'abstract0' + item + '.jpg'"/>-->
        <!--            </div>-->
        <div>
          <img
            style="width:400px;height:300px;"
            src="@/assets/img/1.jpg"
          >
          zzk
        </div>
        <div>
          <img
            style="width:400px;height:300px;"
            src="@/assets/img/2.jpg"
          >
          hxl
        </div>
        <div>
          <img
            style="width:400px;height:300px;"
            src="@/assets/img/3.jpg"
          >
          zzh
        </div>
        <div>
          <img
            style="width:400px;height:300px;"
            src="@/assets/img/4.jpg"
          >
          wyx
        </div>
      </a-carousel>
      <!--        <a-carousel arrows dots-class="slick-dots slick-thumb">-->
      <!--          <template #customPaging="props">-->
      <!--            <a>-->
      <!--              <img :src="getImgUrl(props.i)" />-->
      <!--            </a>-->
      <!--          </template>-->
      <!--          <div v-for="item in 4" :key="item">-->
      <!--            <img :src="baseUrl + 'abstract0' + item + '.jpg'"/>-->
      <!--          </div>-->
      <!--        </a-carousel>-->
    </div>
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
  created() {
    this.$store.commit('setPath', { name: '系统设置' })
    this.$store.commit('pushPath', { name: '开发团队', to: 'developmentteam' })
  },
  methods: {
  },
  setup() {
    const getImgUrl = i => {
      return `../assets/img/1.jpg`;
      // return `${baseUrl}abstract0${i + 1}.jpg`;
    };
    return {
      baseUrl,
      getImgUrl,
    };
  },
});
</script>

<style scoped>
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
.ant-carousel :deep(.slick-dots) {
  position: relative;
  height: auto;
}
.ant-carousel :deep(.slick-slide img) {
  border: 5px solid #fff;
  display: block;
  margin: auto;
  max-width: 80%;
}
.ant-carousel :deep(.slick-arrow) {
  display: none !important;
}
.ant-carousel :deep(.slick-thumb) {
  bottom: 0px;
}
.ant-carousel :deep(.slick-thumb li) {
  width: 60px;
  height: 45px;
}
.ant-carousel :deep(.slick-thumb li img) {
  width: 100%;
  height: 100%;
  filter: grayscale(100%);
}
.ant-carousel :deep .slick-thumb li.slick-active img {
  filter: grayscale(0%);
}
</style>
