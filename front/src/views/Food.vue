<template>
  <div>
    <a-spin :spinning="spinning">
      <food-info :food="food" />
      <div class="background">
        <div v-if="foodEvaluates.length > 0">
          <div
            v-for="evaluate in foodEvaluates"
            :key="evaluate"
          >
            <user-comment
              :comment="evaluate"
              @handleDelete="handleDelete"
            />
          </div>
        </div>
        <div v-else>
          <a-empty description="暂无评论" />
        </div>
      </div>
      <div>
        <my-comment
          :comment="comment"
          @handleEvaluate="handleEvaluate"
        />
      </div>
    </a-spin>
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
      comment: {},
      spinning: true,
    };
  },
  computed: {


  },
  created() {
    this.spinning = true
    this.getFoodInfo();
  },
  activated() {
    this.spinning = true
    this.getFoodInfo()
  },
  methods: {
    async getFoodInfo() {
      try {
        const { data: res } = await this.$http.post("api/getEvaluateFood/", { userID: this.$store.state.userID, foodID: this.$route.query.foodID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.food = res.food;
          this.foodEvaluates = res.foodEvaluate;
          this.comment = res.comment;
          this.$store.commit('pushPath', { name: res.food.foodName, to: window.location.pathname + window.location.search })
        }
      } catch (error) {
        this.$message.error("网络异常");
      } finally {
        this.spinning = false
      }
    },
    async handleDelete(comment) {
      this.spinning = true
      try {
        const { data: res } = await this.$http.post("api/deleteEvaluateFood/", comment);
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.getFoodInfo();
        }
      } catch (error) {
        this.$message.error("网络异常");
      } finally {
        this.spinning = false
      }
    },
    async handleEvaluate(comment) {
      this.spinning = true
      try {
        const { data: res } = await this.$http.post("api/evaluateFood/", comment);
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.getFoodInfo();
        }
      } catch (error) {
        this.$message.error("网络异常");
      } finally {
        this.spinning = false
      }
    },
  },
  watch: {
    $route(to) {
      if (to.path == "/home/food") {
        this.spinning = true
        this.getFoodInfo();
      }
    }
  }
}
</script>

<style scoped>
@media screen and (min-width: 1201px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 80%;
    overflow: auto;
  }
}

@media screen and (max-width: 1200px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 99%;
    overflow: auto;
  }
}
</style>
