<template>
  <div class="register-body">
    <div class="register-window">
      <div class="register-content">
        <p class="register-title">用户注册</p>
        <div class="register-form">
          <form name="myForm">
            <input
              type="text"
              name="userName"
              class="register-param"
              v-model="param.userName"
              placeholder="您的用户名"
              required
              @keyup.enter="checkParam()"
            >
            <input
              type="text"
              name="userName"
              class="register-param"
              v-model="param.userNickname"
              placeholder="您的昵称"
              required
              @keyup.enter="checkParam()"
            >
            <input
              id="pw1"
              type="password"
              name="password1"
              class="register-param"
              v-model="param.password1"
              placeholder="您的密码"
              required
              @keyup.enter="checkParam()"
            >
            <input
              id="pw2"
              type="password"
              name="password2"
              class="register-param"
              v-model="param.password2"
              placeholder="重复一遍您的密码"
              required
              @keyup.enter="checkParam()"
            >
            <input
              type="text"
              name="userTel"
              class="register-param"
              v-model="param.userTel"
              placeholder="您的电话"
              required
              @keyup.enter="checkParam()"
            >
            <!--        <input type="text" name="userAddress" class="e" placeholder="您的住址" required>-->
            <select
              name="userAddress"
              class="register-param"
              v-model="param.userAddress"
              required
            >
              <option
                value=""
                disabled
                selected
              >请选择您的住址</option>
              <option value="学院路-15公寓">学院路-15公寓</option>
              <option value="学院路-13公寓">学院路-13公寓</option>
              <option value="学院路-大运村">学院路-大运村</option>
              <option value="学院路-3公寓">学院路-3公寓</option>
              <option value="学院路-12公寓">学院路-12公寓</option>
              <option value="学院路-20公寓">学院路-20公寓</option>
              <option value="沙河校区">沙河校区</option>
            </select>
            <input
              class="register-submit"
              value="注册"
              readonly
              @click="checkParam()"
            >
            <input
              class="register-submit"
              value="返回登陆"
              readonly
              @click="back2Welcome()"
            >
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      param: {
        userName: "",
        userNickname: "",
        password1: "",
        password2: "",
        userTel: "",
        userAddress: "",
      },
      paramTitle: {
        userName: "用户名",
        userNickname: "用户昵称",
        password1: "密码",
        password2: "重复密码",
        userTel: "电话",
        userAddress: "住址",
      }
    };
  },
  created() {

  },
  methods: {
    async checkParam() {
      for (var i in this.param) {
        if (this.param[i].trim().length == 0)
          return this.$message.error(this.paramTitle[i] + "未填写")
      }

      if (this.param.password1 !== this.param.password2) {
        return this.$message.error("请重新检查，两次输入的密码不一致！");
      }
      else {
        this.param.userPassword = this.param.password1;
        try {
          const { data: res } = await this.$http.post("/api/register/", this.param);
          if (res.success == false) {
            this.$message.error(res.message);
          }
          else {
            this.$store.commit("login", { username: this.param.username, userID: res.userID });
            this.$message.success(res.message);
            this.$router.push({ path: "/home" });
          }
        } catch (error) {
          this.$message.error("网络异常");
        }
      }
    },
    back2Welcome() {
      this.$router.push({ path: "/login" });
    }
  },
}
</script>

<style scoped>
.register-body {
  display: flex;
  justify-content: center;
  background-image: linear-gradient(to left, #79defd, #ffffff);
  height: 100%;
}
.register-window {
  background-color: #ffffff;
  width: 600px;
  height: 650px;
  position: relative;
  display: flex;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  top: 20px;
}
.register-content {
  width: 350px;
  height: 700px;
  overflow: hidden;
}
.register-title {
  font: 900 40px bolder;
  margin: 60px 0;
  text-align: center;
  /* 设置字体间距 */
  letter-spacing: 5px;
}
.register-param {
  width: 100%;
  margin-bottom: 20px;
  outline: none;
  border: 0;
  padding: 10px;
  border-bottom: 2px solid rgb(60, 60, 70);
  font: 900 16px bolder;
}
.register-submit {
  text-align: center;
  width: 100%;
  margin-bottom: 20px;
  outline: none;
  border: 0;
  padding: 10px;
  /*border-bottom: 2px solid rgb(60,60,70);*/
  font: 900 16px bolder;
  background-image: linear-gradient(to left, #79defd, #ffffff);
}
</style>