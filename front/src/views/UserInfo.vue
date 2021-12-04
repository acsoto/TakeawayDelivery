<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
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
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
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
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
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
    ShoppingTwoTone,
    PlusCircleTwoTone,
    MinusCircleTwoTone,
    MyAvatar,
    MyInfo,
  },
  setup() {
    const count = ref(0);

    const decline = () => {
      if (count.value >= 1) {
        count.value--;
      }
    };

    const increase = () => {
      count.value++;
    };

    return {
      count,
      show: ref(true),
      decline,
      increase,
    };
  },
  created() {
    this.getUserInfo();
  },
  methods: {
    testOnclick() {
      window.alert("You Clicked Me!!!");
    },
    async getUserInfo() {
      const { data: res } = await this.$http.post("api/getInformation/", { userID: this.userID });
      console.log(res)
      // if (res.success == false) {
      //   this.$message.error(res.message);
      // }
      // else {
      //   this.$store.commit("login", { userName: this.param.userName, userID: res.userID });//注意一下，store貌似只能传一个参数，建议传个对象过去。
      //   //获取存入的userID的方式：this.$store.state.userID   (注意是this.$store.state.XXX，千万别落什么东西)
      //   //console.log(this.$store.state)
      //   this.$message.success(res.message);
      //   this.$router.push({ path: "/home" });
      // }
      this.user = res
      this.$forceUpdate()
      console.log(this.user)
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
