<template>
  <div class="background">
    <div class="restaurant-card">
      <div>
        <div style="margin:10px;display: flex;  justify-content: space-between;  align-items: center;">
          <div>
            <span class="name">{{thisRestaurant.storeName}}</span> <br />

            <strong>{{thisRestaurant.storeAddress}}</strong><br />
            <strong>{{thisRestaurant.storeTel}}</strong><br />
            <strong>
              <a-rate
                :default-value="thisRestaurant.score"
                disabled
              />（{{thisRestaurant.count}}个评价）
            </strong><br />
          </div>
          <!-- 进入餐厅详情界面 -->
          <div>
          </div>
        </div>
        <!-- 食物展示栏 -->
        <div>
          <a-row>
            <div
              v-for="food in thisRestaurant.food"
              :key="food"
            >
              <food-card :food="food" />
            </div>
          </a-row>
        </div>
      </div>

      <div style="margin:20px">
        <img
          :src="thisRestaurant.storeUrl"
          style="width:300px;height:300px;border-radius:10px;margin-right:20px;"
        />
      </div>

    </div>
  </div>
</template>

<script>
import FoodCard from '@/components/restaurant/FoodCard'
export default {
  components: {
    FoodCard
  },
  props: ['restaurant'],
  data() {
    return {
      thisRestaurant: this.restaurant,
    };
  },
  created() {

  },
  methods: {},
  watch: {
    restaurant() {
      this.thisRestaurant = this.restaurant;
    }
  },
}
</script>

<style scoped>
.restaurant-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.name {
  font-size: 30px;
  font-weight: 800;
}
@media screen and (min-width: 1201px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    width: 80%;
  }
}

@media screen and (max-width: 1200px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    width: 100%;
  }
}
</style>
