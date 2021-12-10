<template>
  <div>
    <a-spin :spinning="spinning">
      <div
        v-for="store in stores"
        :key="store"
        style="margin:0px"
      >
        <my-store :restaurant="store" />
      </div>
      <div v-if="stores.length==0">
        <a-empty description="暂无食堂" />
      </div>
    </a-spin>
  </div>
</template>
<script>
import MyStore from '@/components/restaurant/RestaurantCard'
export default {
  data() {
    return {
      collapsed: true,
      stores: [],
      spinning: true,
    };
  },
  components: {
    MyStore,
  },
  created() {
    this.spinning = true
    this.$store.commit('setPath', { name: '商铺' })
    this.$store.commit('pushPath', { name: '所有餐厅', to: '/home/restaurants' })
    this.getStoreList();
  },
  activated() {
    this.$store.commit('setPath', { name: '商铺' })
    this.$store.commit('pushPath', { name: '所有餐厅', to: '/home/restaurants' })
    this.getStoreList();
  },
  methods: {
    async getStoreList() {
      try {
        const { data: res } = await this.$http.post("api/getStores/");
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.stores = res.store;
        }
      } catch (error) {
        this.$message.error("网络异常");
      } finally {
        this.spinning = false
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
