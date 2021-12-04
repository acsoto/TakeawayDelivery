<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>商铺</a-breadcrumb-item>
        <a-breadcrumb-item>
          <router-link to="/home/restaurants">
            所有餐厅
          </router-link>
        </a-breadcrumb-item>
        <a-breadcrumb-item>{{store.storeName}}</a-breadcrumb-item>
      </a-breadcrumb>

      <restaurant-info :restaurant="store" />

    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>

<script>
import RestaurantInfo from '@/components/restaurant/RestaurantInfo'
export default {
  components: {
    RestaurantInfo,
  },
  data() {
    return {
      store: {},
    };
  },
  created() {
    this.getStoreInfo();
  },
  methods: {
    async getStoreInfo() {
      try {
        const { data: res } = await this.$http.post("api/getStoreInformation/", { storeID: this.$route.query.storeID });
        console.log(res)
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.store = res;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    }
  },
  watch: {
  },
}
</script>

<style scoped>
</style>
