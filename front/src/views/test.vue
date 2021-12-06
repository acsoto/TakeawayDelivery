<template>
  <div>
    <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
      <!--          Bill is a cat.-->
      <el-carousel
        :interval="4000"
        type="card"
        height="200px"
      >
        <el-carousel-item
          v-for="item in 6"
          :key="item"
        >
          <h3 class="medium">
            <img src="https://img.meituan.net/phoenix/d681fd63f884f6f5fd9fd5493e65f86c4428480.jpg@740w_416h_1e_1c">
          </h3>
        </el-carousel-item>
      </el-carousel>
    </div>
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

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
