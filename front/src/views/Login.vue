<template>
  <div
    class="login-body"
    content="width=device-width, initial-scale=1.0"
  >
    <div class="login-window">
      <div class="login-content">
        <p class="login-title">登录</p>
        <div class="login-form">
          <form>

            <input
              type="text"
              name="userName"
              class="login-param"
              placeholder="用户名"
              required
              v-model="param.userName"
              @keyup.enter="submitForm()"
            >

            <input
              type="userPassword"
              name="userPassword"
              class="login-param"
              placeholder="密码"
              required
              v-model="param.userPassword"
              @keyup.enter="submitForm()"
            >

            <input
              class="login-submit"
              type="submit"
              readonly
              @click="submitForm()"
              value="登录"
            >
          </form>
        </div>
        <div class="login-hint">没有账号?
          <router-link to="/register">点击注册</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script >
export default {
  data() {
    return {
      param: {
        userName: "",
        userPassword: "",
      },
      paramTitle: {
        userName: "用户名",
        userPassword: "密码",
      }
    };
  },
  created() {

  },
  methods: {

    async submitForm() {

      for (var i in this.param) {
        if (this.param[i].trim().length == 0)
          return this.$message.error(this.paramTitle[i] + "未填写")
      }
      const { data: res } = await this.$http.post("api/login/", this.param);
      //console.log(res)
      if (res.success == false) {
        this.$message.error(res.message);
      }
      else {
        this.$store.commit("login", { userName: this.param.userName, userID: res.userID });//注意一下，store貌似只能传一个参数，建议传个对象过去。
        //获取存入的userID的方式：this.$store.state.userID   (注意是this.$store.state.XXX，千万别落什么东西)
        //console.log(this.$store.state)
        this.$message.success(res.message);
        this.$router.push({ path: "/home" });
      }
    }
  },
}
</script>

<style scoped>
.login-body {
  display: flex;
  justify-content: center;
  height: 100%;
  background-image: linear-gradient(to left, #79defd, #ffffff);
}
.login-window {
  background-color: #ffffff;
  width: 350px;
  height: 550px;
  position: relative;
  display: flex;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  top: 100px;
}
.login-content {
  width: 300px;
  height: 450px;
  overflow: hidden;
}
.login-title {
  font: 900 40px bolder;
  margin: 60px 0;
  text-align: center;
  /* 设置字体间距 */
  letter-spacing: 5px;
}
.login-param {
  width: 100%;
  margin-bottom: 20px;
  outline: none;
  border: 0;
  padding: 10px;
  border-bottom: 2px solid rgb(60, 60, 70);
  font: 900 16px bolder;
}
.login-submit {
  width: 100%;
  color: black;
  margin-bottom: 20px;
  outline: none;
  border: 0;
  text-align: center;
  padding: 10px;
  /*border-bottom: 2px solid rgb(60,60,70);*/
  font: 900 16px bolder;
  background-image: linear-gradient(to left, #79defd, #ffffff);
}
.login-hint {
  margin: 23px;
}
</style>
