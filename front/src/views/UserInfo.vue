<template>
  <div>
    <!-- <a-layout-header style="background: #fff; padding: 0">
      <PlusCircleTwoTone
        style="font-size: xxx-large"
        @click="increase"
      />
      <MinusCircleTwoTone
        style="font-size: xxx-large"
        @click="decline"
      />
      <ShoppingTwoTone
        style="font-size: xxx-large"
        @click="testOnclick"
      />
      <a-badge
        :count="count"
        show-zero
      >
        <a
          href="#"
          class="head-example"
        />
      </a-badge>
    </a-layout-header> -->
    <a-layout-content style="margin: 0 16px;height:90vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>个人中心</a-breadcrumb-item>
        <a-breadcrumb-item>个人信息</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
        <!--        TODO-->

        <a-row
          type="flex"
          justify="center"
        >
          <a-col
            justify="center"
            :span="10"
          >
            <my-avatar :user="user" />
          </a-col>
          <a-col
            justify="center"
            :span="10"
          >
            <my-info :user="user" />
          </a-col>
        </a-row>
      </div>
    </a-layout-content>
  </div>
</template>
<script>
import { ShoppingTwoTone, PlusCircleTwoTone, MinusCircleTwoTone } from '@ant-design/icons-vue';
import { defineComponent, ref } from "vue";
import MyAvatar from '@/components/userinfo/MyAvatar'
import MyInfo from '@/components/userinfo/MyInfo'
export default defineComponent({
  data() {
    return {
      collapsed: true,
      user: { userOrders: [], userStars: [], userIconUrl: "", },
      columns: [],
      userID: this.$store.state.userID,

    };
  },
  components: {
    // ShoppingTwoTone,
    // PlusCircleTwoTone,
    // MinusCircleTwoTone,
    MyAvatar,
    MyInfo,
  },
  // setup() {
  //   const count = ref(0);

  //   const decline = () => {
  //     if (count.value >= 1) {
  //       count.value--;
  //     }
  //   };

  //   const increase = () => {
  //     count.value++;
  //   };

  //   return {
  //     count,
  //     show: ref(true),
  //     decline,
  //     increase,
  //   };
  // },
  created() {
    this.getUserInfo();
  },
  methods: {
    // testOnclick() {
    //   window.alert("You Clicked Me!!!");
    // },
    async getUserInfo() {
      try {
        const { data: res } = await this.$http.post("api/getInformation/", { userID: this.userID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.user = res
          this.$forceUpdate()
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
  },
});
</script>

<style>
#components-layout-demo-side .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
</style>
