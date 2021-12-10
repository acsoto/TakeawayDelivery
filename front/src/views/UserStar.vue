<template>
  <div>
    <a-spin :spinning="spinning">
      <div v-if="stars.length==0">
        <a-empty description="暂无收藏食物" />
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
    </a-spin>
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
      spinning: true,
    };
  },
  components: {
    FoodCard,
  },
  created() {
    this.spinning = true
    this.$store.commit('setPath', { name: '个人中心' })
    this.$store.commit('pushPath', { name: '我的最爱', to: '/home/userstar' })
    this.getData();
  },
  activated() {
    if (this.$store.state.change['star']) {
      this.$store.commit('setChange', { name: 'star', value: false })
      this.spinning = true
      this.getData();
    }
    this.$store.commit('setPath', { name: '个人中心' })
    this.$store.commit('pushPath', { name: '我的最爱', to: '/home/userstar' })
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
