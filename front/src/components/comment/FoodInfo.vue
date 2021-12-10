<template>
  <div class="background">
    <div class="food-card">
      <div>
        <div style="margin:20px;">
          <div>
            <span class="name">{{thisFood.foodName}}</span>

            <br />
            <strong
              class="value"
              style="cursor: pointer;"
              @click="$router.push({ path: '/home/restaurant',
            query: {
              storeID: thisFood.storeID,
            },});"
            >{{thisFood.storeName}}</strong><br />
            <strong class="value">{{thisFood.foodPrice}}元</strong>
            <a-tooltip
              v-if="!thisFood.hasStared"
              placement="top"
            >
              <template #title>
                <span>收藏</span>
              </template>
              <a-button
                type="link"
                @click="setStar"
              >
                <StarOutlined />
              </a-button>
            </a-tooltip>
            <a-tooltip
              v-else
              placement="top"
            >
              <template #title>
                <span>取消收藏</span>
              </template>
              <a-button
                type="link"
                @click="unStar"
              >
                <StarFilled />
              </a-button>
            </a-tooltip><br />
            <strong class="value">
              <a-rate
                v-model:value="thisFood.foodScore"
                disabled
              />（{{thisFood.foodCount}}个评价）
            </strong><br />
          </div>
        </div>
      </div>
      <div
        class="image"
        style="margin:20px;"
      >
        <img
          :src="thisFood.foodUrl"
          style="width:200px;height:200px;border-radius:10px;margin-right:20px;"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { StarOutlined, StarFilled } from '@ant-design/icons-vue';
export default {
  components: {
    StarOutlined,
    StarFilled,
  },
  props: ['food'],
  data() {
    return {
      thisFood: this.food,
    };
  },
  created() {

  },
  methods: {
    async setStar() {
      try {
        const { data: res } = await this.$http.post("api/setStar/", { userID: this.$store.state.userID, foodID: this.thisFood.foodID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.thisFood.hasStared = true;
          this.$store.commit('setChange', { name: 'star', value: true })
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
    async unStar() {
      try {
        const { data: res } = await this.$http.post("api/unStar/", { userID: this.$store.state.userID, foodID: this.thisFood.foodID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.thisFood.hasStared = false;
          this.$store.commit('setChange', { name: 'star', value: true })
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
.food-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.name {
  font-size: 40px;
  font-weight: 800;
}
.value {
  font-size: 20px;
}

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
