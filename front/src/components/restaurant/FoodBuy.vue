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
          style="width:150px;height:150px;margin:0px;border-radius: 10px;"
        />
        <div style="margin-left:20px;">
          <div class="name">{{thisFood.foodName}}</div>
          <div class="value">{{thisFood.foodPrice}}</div>
          <a-rate
            v-model:value="thisFood.foodScore"
            disabled
          /><span class="value">（{{thisFood.foodCount}}个评价）</span>
        </div>
      </div>
      <div>
        <a-input-number
          id="inputNumber"
          v-model:value="thisFood.foodNum"
          @change="$emit('getTotal')"
          :min="0"
        />
        <div v-if="thisFood.foodNum">小计:{{thisFood.foodNum*thisFood.foodPrice}}元</div>
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
    this.thisFood.foodNum = 0;
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