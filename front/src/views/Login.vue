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
                type="password"
                name="userPassword"
                class="login-param"
                placeholder="密码"
                required
                v-model="param.userPassword"
                @keyup.enter="submitForm()"
            >
            <a-button @click="submitForm()" style="width:100%;" type="primary">登录</a-button>

          </form>
        </div>
        <div class="login-hint">没有账号?
          <router-link to="/register">点击注册</router-link>
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
      try {
        const {data: res} = await this.$http.post("api/login/", this.param);
        //console.log(res)
        if (res.success == false) {
          this.$message.error(res.message);
        } else {
          this.$store.commit("login", {userName: this.param.userName, userID: res.userID});//注意一下，store貌似只能传一个参数，建议传个对象过去。
          //获取存入的userID的方式：this.$store.state.userID   (注意是this.$store.state.XXX，千万别落什么东西)
          //console.log(this.$store.state)
          this.$message.success(res.message);
          this.$router.push({path: "/home"});
        }
      } catch (error) {
        this.$message.error("网络异常");
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
  background-image: url(~@/assets/img/cat.svg);
}

.login-window {
  background-color: rgb(255, 255, 255, 0.5);
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

<!--<style lang="less" scoped>-->
<!--#userLayout.user-layout-wrapper {-->
<!--  height: 100%;-->

<!--  &.mobile {-->
<!--    .container {-->
<!--      .main {-->
<!--        max-width: 368px;-->
<!--        width: 98%;-->
<!--      }-->
<!--    }-->
<!--  }-->

<!--  .container {-->
<!--    width: 100%;-->
<!--    min-height: 100%;-->
<!--    background: #f0f2f5 url(~@/assets/cat.svg) no-repeat 50%;-->
<!--    background-size: 100%;-->
<!--    //padding: 50px 0 84px;-->
<!--    position: relative;-->

<!--    .user-layout-lang {-->
<!--      width: 100%;-->
<!--      height: 40px;-->
<!--      line-height: 44px;-->
<!--      text-align: right;-->

<!--      .select-lang-trigger {-->
<!--        cursor: pointer;-->
<!--        padding: 12px;-->
<!--        margin-right: 24px;-->
<!--        display: inline-flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        font-size: 18px;-->
<!--        vertical-align: middle;-->
<!--      }-->
<!--    }-->

<!--    .user-layout-content {-->
<!--      padding: 32px 0 24px;-->

<!--      .top {-->
<!--        text-align: center;-->

<!--        .header {-->
<!--          height: 44px;-->
<!--          line-height: 44px;-->

<!--          .badge {-->
<!--            position: absolute;-->
<!--            display: inline-block;-->
<!--            line-height: 1;-->
<!--            vertical-align: middle;-->
<!--            margin-left: -12px;-->
<!--            margin-top: -10px;-->
<!--            opacity: 0.8;-->
<!--          }-->

<!--          .logo {-->
<!--            height: 44px;-->
<!--            vertical-align: top;-->
<!--            margin-right: 16px;-->
<!--            border-style: none;-->
<!--          }-->

<!--          .title {-->
<!--            font-size: 33px;-->
<!--            color: rgba(0, 0, 0, .85);-->
<!--            font-family: Avenir, 'Helvetica Neue', Arial, Helvetica, sans-serif;-->
<!--            font-weight: 600;-->
<!--            position: relative;-->
<!--            top: 2px;-->
<!--          }-->
<!--        }-->
<!--        .desc {-->
<!--          font-size: 14px;-->
<!--          color: rgba(0, 0, 0, 0.45);-->
<!--          margin-top: 12px;-->
<!--          margin-bottom: 40px;-->
<!--        }-->
<!--      }-->

<!--      .main {-->
<!--        min-width: 260px;-->
<!--        width: 368px;-->
<!--        margin: 0 auto;-->
<!--      }-->

<!--      .footer {-->
<!--        // position: absolute;-->
<!--        width: 100%;-->
<!--        bottom: 0;-->
<!--        padding: 0 16px;-->
<!--        margin: 48px 0 24px;-->
<!--        text-align: center;-->

<!--        .links {-->
<!--          margin-bottom: 8px;-->
<!--          font-size: 14px;-->
<!--          a {-->
<!--            color: rgba(0, 0, 0, 0.45);-->
<!--            transition: all 0.3s;-->
<!--            &:not(:last-child) {-->
<!--              margin-right: 40px;-->
<!--            }-->
<!--          }-->
<!--        }-->
<!--        .copyright {-->
<!--          color: rgba(0, 0, 0, 0.45);-->
<!--          font-size: 14px;-->
<!--        }-->
<!--      }-->
<!--    }-->

<!--    a {-->
<!--      text-decoration: none;-->
<!--    }-->

<!--  }-->
<!--}-->
<!--</style>-->

<!--<template>-->
<!--  <div class="background">-->
<!--    <img src="../assets/img/user.jpg" width="100%" height="100%" alt="" />-->
<!--</div>-->
<!--</template>-->


<!--<script >-->
<!--export default {-->

<!--  created() {-->

<!--  },-->

<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--  .background{-->
<!--    width:100%;-->
<!--    height:100%;  /**宽高100%是为了图片铺满屏幕 */-->
<!--    z-index:-1;-->
<!--    position: absolute;-->
<!--  }-->
<!--  .front{-->
<!--    z-index:1;-->
<!--    position: absolute;-->
<!--  }-->
<!--</style>-->