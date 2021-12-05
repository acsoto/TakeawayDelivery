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
        <a-breadcrumb-item>{{food.foodName}}</a-breadcrumb-item>
      </a-breadcrumb>

      <food-info :food="food" />
      <div
        v-for="evaluate in foodEvaluates"
        :key="evaluate"
      >
        <user-comment :comment="evaluate" />
      </div>
      <div v-if="!food.hasCommented">
        <my-comment :comment="comment"/>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>

<script>
import FoodInfo from '@/components/comment/FoodInfo'
import UserComment from '@/components/comment/UserComment'
import MyComment from '@/components/comment/MyComment'
export default {
  components: {
    UserComment,
    FoodInfo,
    MyComment,
  },
  data() {
    return {
      food: {},
      foodEvaluates: {},
      total: 0,
      comment:{ }
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
        const { data: res } = await this.$http.post("api/getEvaluateFood/", { userID: this.$store.state.userID, foodID: this.$route.query.foodID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.food = res.food;
          this.foodEvaluates = res.foodEvaluates;
          this.comment=res.comment;
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
</style>
