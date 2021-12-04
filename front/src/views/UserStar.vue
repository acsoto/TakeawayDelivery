<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>个人中心</a-breadcrumb-item>
        <a-breadcrumb-item>我的最爱</a-breadcrumb-item>
      </a-breadcrumb>
      <div v-if="stars.length==0">
        <a-empty />
      </div>
      <div v-else>
        <div
          v-for="food in stars"
          :key="food"
        >
          <food-card
            :food="food"
            @getData="getData"
          />
        </div>
      </div>

    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©2021 Powered by zzh company
    </a-layout-footer>
  </div>
</template>
<script>
import FoodCard from '@/components/star/FoodCard'
export default {
  data() {
    return {
      collapsed: true,
      stars: [],
      userID: this.$store.state.userID,
    };
  },
  components: {
    FoodCard,
  },
  created() {
    this.getData();
  },
  methods: {
    async getData() {
      try {
        const { data: res } = await this.$http.post("api/getInformation/", { userID: this.userID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.stars = res.userStars
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },

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
