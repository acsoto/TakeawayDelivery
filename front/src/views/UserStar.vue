<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>个人中心</a-breadcrumb-item>
        <a-breadcrumb-item>我的最爱</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
        <div style="width:100%;display:inline-block;">
          <a-row
            type="flex"
            justify="space-around"
          >
            <div
              v-for="food in data"
              :key="food"
              style="width:154px;margin:0px;"
            >
              <a-card
                hoverable
                style="width:154px;height:250px;margin:10px;text-align:center;align:center"
              >
                <template
                  #cover
                  style="width:150px;height:150px;"
                >
                  <img
                    alt="example"
                    :src="food.foodUrl"
                    style="width:154px;height:150px;margin:0px;"
                  />
                </template>
                <a-card-meta :title="food.foodName">
                  <template #description>{{food.foodPrice}}</template>
                </a-card-meta>
              </a-card>
            </div>
          </a-row>
        </div>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©2021 Powered by zzh company
    </a-layout-footer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      collapsed: true,
      data:[],
      columns:[],
      userID:this.$store.state.userID,
    };
  },
created() {
    this.getData();
  },
  methods:{
    async getData()
    {
      const { data: res } = await this.$http.post("api/getInformation/", {userID:this.userID});
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
      this.data=res.userStars
      console.log(this.data)
    },

  },
};
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

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
