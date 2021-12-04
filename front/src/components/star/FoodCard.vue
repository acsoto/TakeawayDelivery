 <template>
  <div class="background">
    <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
      <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
        <img
          alt="example"
          :src="thisFood.foodUrl"
          style="width:75px;height:75px;margin:0px;border-radius: 10px;"
        />
        <div style="margin-left:20px;">
          <div class="name">{{thisFood.foodName}}</div>
          <div class="value">{{thisFood.foodPrice}}</div>
        </div>
      </div>
      <div style="text-align:center;">
        <a-button
          type="primary"
          @click="handleUnstar"
        >
          取消收藏
        </a-button>
      </div>
    </div>
  </div>
</template>


<script>
export default {

  props: ['food'],
  data() {
    return {
      thisFood: this.food,
    };
  },
  created() {
  },
  methods: {
    async handleUnstar() {
      try {
        const { data: res } = await this.$http.post("api/unstar/", { userID: this.$store.state.userID, foodID: this.thisFood.foodID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success("取消收藏成功");
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
  }
}

@media screen and (max-width: 1200px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 100%;
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