 <template>
  <div class="background">
    <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
      <div
        style="margin:10px;display:flex;justify-content:space-between;align-items: center;cursor: pointer;"
        @click="$router.push({ path: '/home/food',
            query: {
              foodID: thisFood.foodID,
            },});"
      >
        <img
          alt="example"
          :src="thisFood.foodUrl"
          style="width:75px;height:75px;margin:0px;border-radius: 10px;"
        />
        <div style="margin-left:20px;">
          <div class="name">{{thisFood.foodName}}</div>
          <div class="value">{{thisFood.foodPrice}}元</div>
        </div>
      </div>
      <div style="text-align:center;">
        {{hot_rank}}
        <!--        <a-popconfirm-->
        <!--          title="您确认要取消收藏吗？"-->
        <!--          ok-text="确认"-->
        <!--          cancel-text="取消"-->
        <!--          @confirm="handleUnstar"-->
        <!--        >-->
        <!--&lt;!&ndash;          <a-button type="primary">&ndash;&gt;-->
        <!--&lt;!&ndash;            详情&ndash;&gt;-->
        <!--&lt;!&ndash;          </a-button>&ndash;&gt;-->
        <!--        </a-popconfirm>-->
      </div>
    </div>
  </div>
</template>


<script>
export default {

  props: ['food', 'hot_rank'],
  data() {
    return {
      num: 0,
      thisFood: this.food,
    };
  },
  created() {
  },
  methods: {
    async handleUnstar() {

      try {
        const { data: res } = await this.$http.post("api/unStar/", { userID: this.$store.state.userID, foodID: this.thisFood.foodID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.$emit('getData')
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
  },
  watch: {
    food() {
      this.thisFood = this.food;
    }
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
.name {
  font-size: 30px;
  font-weight: 700;
}
.value {
  font-size: 20px;
}
</style>