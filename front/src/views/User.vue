<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>商铺</a-breadcrumb-item>
        <a-breadcrumb-item>
          <router-link to="/home/restaurants">
            所有餐厅
          </router-link>
        </a-breadcrumb-item>
        <a-breadcrumb-item>{{user.userName}}</a-breadcrumb-item>
      </a-breadcrumb>

      <user-info :user="user" />

      <div class="background">
        <div v-if="userEvaluates.length > 0">
          <div
            v-for="evaluate in userEvaluates"
            :key="evaluate"
          >
            <user-comment
              :comment="evaluate"
              @handleDelete="handleDelete"
            />
          </div>
        </div>
        <div v-else>
          <a-empty description="暂无评论" />
        </div>
      </div>
      <div v-if="!user.hasCommented&&!user.commentMyself">
        <my-comment
          :comment="comment"
          @handleEvaluate="handleEvaluate"
        />
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>

<script>
import UserInfo from '@/components/comment/UserInfo'
import UserComment from '@/components/comment/UserComment'
import MyComment from '@/components/comment/MyComment'
export default {
  components: {
    UserComment,
    UserInfo,
    MyComment,
  },
  data() {
    return {
      user: {},
      userEvaluates: {},
      total: 0,
      comment: {}
    };
  },
  computed: {


  },
  created() {
    this.getUserInfo();
  },
  methods: {
    async getUserInfo() {
      try {
        const { data: res } = await this.$http.post("api/getEvaluateUser/", { postUserID: this.$store.state.userID, userID: this.$route.query.userID });
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          console.log(res)
          this.user = res.user;
          this.userEvaluates = res.userEvaluate;
          this.comment = res.comment;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
    async handleDelete(comment) {
      try {
        const { data: res } = await this.$http.post("api/deleteEvaluateUser/", comment);
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.getUserInfo();
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
    async handleEvaluate(comment) {
      try {
        const { data: res } = await this.$http.post("api/evaluateUser/", comment);
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.getUserInfo();
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
  },
  watch: {
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
