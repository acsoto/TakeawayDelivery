<template>
  <div class="background">
    <div class="food-card">
      <div>
        <div style="margin:20px;">
          <div>
            <span class="name">{{thisFood.foodName}}</span> <br />
            <strong class="value">{{thisFood.foodPrice}}</strong><br />
            <strong class="value">
              <a-rate
                :default-value="thisFood.foodScore"
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
export default {
  components: {
  },
  props: ['food'],
  data() {
    return {
      thisFood: this.food,
    };
  },
  created() {

  },
  methods: {},
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
</style>
