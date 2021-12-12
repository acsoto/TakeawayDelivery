<template>
  <div>
    <a-spin :spinning="spinning">
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
      <div v-if="!user.commentMyself">
        <my-comment
          :comment="comment"
          @handleEvaluate="handleEvaluate"
        />
      </div>
    </a-spin>
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
      comment: {},
      spinning: true,
    };
  },
  computed: {


  },
  created() {
    this.spinning = true
    this.getUserInfo();
  },
  activated() {
    this.spinning = true
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
          this.user = res.user;
          this.userEvaluates = res.userEvaluate;
          this.comment = res.comment;
          this.$store.commit('pushPath', { name: res.user.userNickName, to: window.location.pathname + window.location.search })
        }
      } catch (error) {
        this.$message.error("网络异常");
      } finally {
        this.spinning = false
      }
    },
    async handleDelete(comment) {
      this.spinning = true
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
      } finally {
        this.spinning = false
      }
    },
    async handleEvaluate(comment) {
      this.spinning = true
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
      } finally {
        this.spinning = false
      }
    },
  },
  watch: {
    $route(to) {
      if (to.path == "/home/user") {
        this.spinning = true
        this.getUserInfo();
      }
    }
  }
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
</style>
