<template>
  <div>
    <a-spin :spinning="spinning">
      <div v-if="hots.length==0">
        <a-empty description="暂无收藏食物" />
      </div>
      <div v-else>
        <div
          v-for="(food,index) in hots"
          :key="food"
        >
          <food-card
            :food="food"
            @getData="getData"
            :hot_rank="index+1"
          />
        </div>
      </div>
    </a-spin>
  </div>
</template>
<script>
import FoodCard from '@/components/star/HotFoodCard'
export default {
  data() {
    return {
      collapsed: true,
      hots: [],
      userID: this.$store.state.userID,
      spinning: true,
    };
  },
  components: {
    FoodCard,
  },
  created() {
    this.spinning = true
    this.$store.commit('setPath', { name: '商铺' })
    this.$store.commit('pushPath', { name: '热菜榜单', to: '/home/hotfood' })
    this.getData();
  },
  activated() {
    this.$store.commit('setPath', { name: '商铺' })
    this.$store.commit('pushPath', { name: '热菜榜单', to: '/home/hotfood' })
    this.getData();
  },
  methods: {
    async getData() {
      try {
        const { data: res } = await this.$http.post("api/getTopFoodList/", {});
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.hots = res.food
        }
      } catch (error) {
        this.$message.error("网络异常");
      } finally {
        this.spinning = false
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
