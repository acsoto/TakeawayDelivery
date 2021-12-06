<template>
  <div>
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
    <div
      v-for="food in store.food"
      :key="food"
    >
      <food-buy
        :food="food"
        @getTotal="getTotal"
      />
    </div>
    <div
      v-if="total>0"
      class="total"
      style="display:flex;justify-content:space-between;align-items: center;"
    >
      <div>总计：{{total}}元</div>

      <a-button @click="setOrder">下单</a-button>

    </div>
  </div>
</template>

<script>
import RestaurantInfo from '@/components/restaurant/RestaurantInfo'
import FoodBuy from '@/components/restaurant/FoodBuy'
export default {
  components: {
    RestaurantInfo,
    FoodBuy,
  },
  data() {
    return {
      store: {},
      total: 0,
    };
  },
  computed: {


  },
  mounted() {
    this.getStoreInfo();
  },
  methods: {
    async getStoreInfo() {
      try {
        const { data: res } = await this.$http.post("api/getStoreInformation/", { storeID: this.$route.query.storeID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.store = res;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
    getTotal() {
      var total = 0;
      for (var i = 0; i < this.store.food.length; i++) {
        if (this.store.food[i].foodNum) total += this.store.food[i].foodNum * this.store.food[i].foodPrice;
      }
      this.total = total;
    },
    async setOrder() {
      try {
        const { data: res } = await this.$http.post("api/setOrders/", { userID: this.$store.state.userID, foodList: this.store.food });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.$router.push({ path: "/home/restaurants" });
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
@media screen and (min-width: 1201px) {
  .total {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 80%;
  }
}

@media screen and (max-width: 1200px) {
  .total {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 100%;
  }
}
</style>
