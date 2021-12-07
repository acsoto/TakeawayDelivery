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
    <div class="background">
      <div style="display:flex;justify-content:space-between;align-items: center;overflow:auto;padding:50px;">
        <my-avatar :user="user" />
        <my-info :user="user" />
      </div>
    </div>
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
    this.$store.commit('pushPath', { name: '个人信息', to: '/home/userinfo' })
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
  }
}
</style>
