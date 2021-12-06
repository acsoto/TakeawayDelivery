<template>
  <div>

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
    <div v-if="!food.hasCommented">
      <my-comment
        :comment="comment"
        @handleEvaluate="handleEvaluate"
      />
    </div>
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
      comment: {}
    };
  },
  computed: {


  },
  created() {
    this.getFoodInfo();
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
      }
    },
    async handleDelete(comment) {
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
      }
    },
    async handleEvaluate(comment) {
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
      }
    },
  },
  watch: {
  },
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
