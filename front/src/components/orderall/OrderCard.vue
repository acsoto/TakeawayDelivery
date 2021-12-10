 <template>
  <div class="background">

    <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
      <div style="margin:10px;display:flex;justify-content:space-between;align-items: center;">
        <img
          alt="example"
          :src="thisOrder.orderUserIcon"
          style="width:150px;height:150px;margin:0px;border-radius: 10px;"
        />
        <div style="margin-left:20px;">
          <div class="name">收货人:{{thisOrder.orderUserNickName}}</div>
          <div class="value"><span
              style="margin-right:10px; cursor: pointer;"
              @click="$router.push({ path: '/home/restaurant',
            query: {
              storeID: thisOrder.storeID,
            },});"
            >{{thisOrder.storeName}} to {{thisOrder.orderUserAddress}}</span>
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
          </div>
          <div
            class="value"
            v-if="thisOrder.orderCompleted!=0"
          >电话：{{thisOrder.orderUserTel}}</div>
          <div class="value">总价:{{thisOrder.totalPrice}}</div>
          <div class="value">预计送达时间:{{thisOrder.forecastTime.toFixed(2)}}分钟</div>
        </div>
      </div>
      <div style="text-align:center;">
        <div>
          <a-button @click="visible=true">
            查看详情
          </a-button>
        </div>
        <div style="margin-top:10px;">
          <a-popconfirm
            title="您确认要接下订单吗？"
            ok-text="确认"
            cancel-text="取消"
            @confirm="takeOrder"
            v-if="thisOrder.orderCompleted==0"
          >
            <a-button type="primary">
              接下订单
            </a-button>
          </a-popconfirm>
        </div>
        <div>{{thisOrder.orderDate}}</div>
      </div>
    </div>

    <a-modal
      :title="'订单总额'+thisOrder.totalPrice+'元'"
      :visible="visible"
      width="50vw"
      ok-text="确认"
      cancel-text="取消"
      @ok="visible=false"
      @cancel="visible=false"
    >
      <div
        v-for="food in thisOrder.food"
        :key="food"
      >
        <food-card :food="food" />
      </div>
    </a-modal>
  </div>
</template>


<script>
import FoodCard from '@/components/FoodCard'
export default {

  props: ['order'],
  components: {
    FoodCard,
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
  methods: {
    async takeOrder() {
      try {
        const { data: res } = await this.$http.post("api/takeOrder/", { userID: this.$store.state.userID, orderID: this.thisOrder.orderID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.thisOrder.orderCompleted = 1;
          this.$store.commit('setChange', { name: 'orderNow', value: true })
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
  },
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