<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>商铺</a-breadcrumb-item>
        <a-breadcrumb-item>所有餐厅</a-breadcrumb-item>
      </a-breadcrumb>

      <div
        v-for="store in stores"
        :key="store"
        style="margin:0px"
      >
        <my-store :restaurant="store" />
      </div>

    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>
<script>
import MyStore from '@/components/restaurant/RestaurantCard'
export default {
  data() {
    return {
      collapsed: true,
      stores: [],
    };
  },
  components: {
    MyStore,
  },
  created() {
    this.getStoreList();
  },
  methods: {
    async getStoreList() {
      try {
        const { data: res } = await this.$http.post("api/getStores/");
        //console.log(res)
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.stores = res.store;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    }
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
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 2000px;
  line-height: 160px;
  background: #364d79;
  overflow: hidden;
}
</style>
