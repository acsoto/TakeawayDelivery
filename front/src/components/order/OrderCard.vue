 <template>
  <div class="background">

    <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
      <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
        <img
          alt="example"
          :src="thisOrder.deliveryUserIcon"
          v-if="thisOrder.orderCompleted!=0"
          style="width:150px;height:150px;margin:0px;border-radius: 10px;"
        />
        <img
          alt="example"
          src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Ffb9431a4c99691e54952d85ed034faf9a6b7e4f22d45-xy5FHF_fw658&refer=http%3A%2F%2Fhbimg.b0.upaiyun.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641223060&t=e33fed3c1c2cdfab40bc28d5e0e90ae1"
          v-else
          style="width:150px;height:150px;margin:0px;border-radius: 10px;"
        />
        <div style="margin-left:20px;">
          <a-tag v-if="thisOrder.orderCompleted==0">已下单</a-tag>
          <a-tag
            v-if="thisOrder.orderCompleted==1"
            color="orange"
          >
            配送中
          </a-tag>
          <a-tag
            v-if="thisOrder.orderCompleted==2"
            color="green"
          >
            已送达
          </a-tag>
          <div
            class="name"
            v-if="thisOrder.orderCompleted!=0"
          >配送者:{{thisOrder.deliveryUserNickName}}</div>
          <div
            class="name"
            v-else
          >等待配送者</div>
          <div
            class="value"
            v-if="thisOrder.orderCompleted!=0"
          >电话：{{thisOrder.deliveryUserTel}}</div>
          <div class="value">总价:{{thisOrder.totalPrice}}</div>
        </div>
      </div>
      <div style="text-align:center;">
        <a-button
          type="primary"
          @click="visible=true"
        >
          查看详情
        </a-button>
        <div>{{thisOrder.orderDate}}</div>
      </div>
    </div>

    <a-modal
      :title="'订单总额'+thisOrder.totalPrice+'元'"
      :visible="visible"
      width="50vw"
      @ok="visible=false"
      @cancel="visible=false"
    >
      <div
        v-for="food in thisOrder.food"
        :key="food"
      >
        <food-buy :food="food" />
      </div>
    </a-modal>
  </div>
</template>


<script>
import FoodBuy from '@/components/order/FoodBuy'
export default {

  props: ['order'],
  components: {
    FoodBuy,
  },
  data() {
    return {
      thisOrder: this.order,
      visible: false,
    };
  },
  created() {
    this.thisOrder.foodNum = 0;
  },
  methods: {},
  watch: {
    order() {
      this.thisOrder = this.order;
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