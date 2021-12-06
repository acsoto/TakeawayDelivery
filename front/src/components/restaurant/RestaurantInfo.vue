<template>
  <div class="background">
    <div class="restaurant-card">
      <div>
        <div style="margin:20px;">
          <div>
            <span class="name">{{thisRestaurant.storeName}}</span> <br />
            <strong class="value">{{thisRestaurant.storeAddress}}</strong><br />
            <strong class="value">{{thisRestaurant.storeTel}}</strong><br />
            <strong class="value">
              <a-rate
                v-model:value="thisRestaurant.score"
                disabled
              />（{{thisRestaurant.count}}个评价）
            </strong><br />
          </div>
        </div>
      </div>
      <div
        class="image"
        style="margin:20px;"
      >
        <img
          :src="thisRestaurant.storeUrl"
          style="width:200px;height:200px;border-radius:10px;margin-right:20px;"
        />
      </div>

    </div>
  </div>
</template>

<script>
export default {
  components: {
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
