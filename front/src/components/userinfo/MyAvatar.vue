<template>
  <div class="avatar">

    <img
      v-if="iconParam.userIconUrl==undefined"
      style="width:200px; height:200px; border-radius:50%; "
      src="https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto"
    />
    <img
      v-else
      style="width:200px; height:200px; border-radius:50%; "
      :src="iconParam.userIconUrl"
    />
    <div class="button">
      <a-button @click="iconVisible=true;tempUserIconUrl=iconParam.userIconUrl;">
        上传头像
      </a-button>
    </div>

    <div class="button">
      <a-button @click="openPasswordModal">
        修改密码
      </a-button>
    </div>
    <a-modal
      title="上传头像"
      :visible="iconVisible"
      ok-text="确认"
      cancel-text="取消"
      @ok="handleIconOk"
      @cancel="iconVisible=false;iconParam.userIconUrl=tempUserIconUrl;"
    >
      <p>请输入新的头像的URL</p>
      <a-input
        v-model:value="iconParam.userIconUrl"
        class="prop-value"
      />
    </a-modal>

    <a-modal
      title="修改密码"
      :visible="passwordVisible"
      ok-text="确认"
      cancel-text="取消"
      @ok="handlePasswordOk"
      @cancel="passwordVisible=false"
    >
      <p>请输入密码</p>
      <p>
        <a-input-password
          addon-before="原密码"
          v-model:value="passwordParam.userOldPassword"
          class="prop-value"
          @keyup.enter="handlePasswordOk"
        />
      </p>
      <p>
        <a-input-password
          addon-before="新密码"
          v-model:value="password1"
          class="prop-value"
          @keyup.enter="handlePasswordOk"
        />
      </p>
      <p>
        <a-input-password
          addon-before="确认密码"
          v-model:value="password2"
          class="prop-value"
          @keyup.enter="handlePasswordOk"
        />
      </p>
    </a-modal>
  </div>
</template>

<script>

export default {
  name: "NewLogin",
  props: ['user'],
  data() {
    return {
      size: 200,
      iconVisible: false,
      passwordVisible: false,
      password1: "",
      password2: "",
      tempUserIconUrl: "",
      passwordParam: { userID: this.$store.state.userID, userOldPassword: "", userPassword: "" },
      iconParam: {
        userID: this.$store.state.userID, userName: this.user.userName,
        userNickName: this.user.userNickName,
        userTel: this.user.userTel,
        userAddress: this.user.userAddress,
        userIconUrl: undefined,
      },
    };
  },
  methods: {
    openPasswordModal() {
      this.passwordVisible = true
      this.password1 = ""
      this.password2 = ""
      this.passwordParam.userOldPassword = ""
    },
    async handleIconOk() {
      if (this.iconParam.userIconUrl == undefined || this.iconParam.userIconUrl.trim().length == 0) return this.$message.error("请输入新的头像URL");
      try {
        const { data: res } = await this.$http.post("api/changeInformation/", this.iconParam);
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.iconVisible = false;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
    async handlePasswordOk() {
      if (this.password1 != this.password2) return this.$message.error("两次新密码不相等");
      if (this.passwordParam.userOldPassword.trim().length == 0) return this.$message.error("请输入旧密码");
      if (this.password1.trim().length == 0) return this.$message.error("请设置新密码");
      if (this.password1 == this.passwordParam.userOldPassword) return this.$message.warning("密码并未更改");
      try {
        this.passwordParam.userPassword = this.password1
        const { data: res } = await this.$http.post("api/changePassword/", this.passwordParam);
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.passwordVisible = false;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },
  },
  watch: {
    user() {
      this.iconParam.userNickName = this.user.userNickName
      this.iconParam.userTel = this.user.userTel
      this.iconParam.userAddress = this.user.userAddress
      this.iconParam.userIconUrl = this.user.userIconUrl
    }
  }
}
</script>

<style scoped>
.avatar {
  width: 50%;
  min-width: 200px;
  margin: 0 auto;
  margin-top: 50px;
  text-align: center;
}
.button {
  margin: 20px 0px 20px 0px;
}
</style>
