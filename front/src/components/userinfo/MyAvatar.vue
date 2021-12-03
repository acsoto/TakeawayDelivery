<template>
  <div class="avatar">
    <a-avatar
      style="color: #f56a00; backgroundColor: #fde3cf"
      :size="size"
      v-if="iconParam.userIconUrl==''"
    >
      {{$store.state.username}}
    </a-avatar>
    <a-avatar
      :size="size"
      :src="iconParam.userIconUrl"
      v-else
      alt="无法加载"
    />
    <div class="button">
      <a-button
        style="width:100%"
        @click="iconVisible=true;tempUserIconUrl=iconParam.userIconUrl;"
      >
        上传头像
      </a-button>
    </div>

    <div class="button">
      <a-button
        style="width:100%"
        @click="passwordVisible=true"
      >
        修改密码
      </a-button>
    </div>
    <a-modal
      title="上传头像"
      :visible="iconVisible"
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
      @ok="handlePasswordOk"
      @cancel="passwordVisible=false"
    >
      <p>请输入密码</p>
      <p>
        <a-input
          addon-before="原密码"
          v-model:value="passwordParam.userOldPassword"
          class="prop-value"
        />
      </p>
      <p>
        <a-input
          addon-before="新密码"
          v-model:value="password1"
          class="prop-value"
        />
      </p>
      <p>
        <a-input
          addon-before="确认密码"
          v-model:value="password2"
          class="prop-value"
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
        userIconUrl: this.user.userIconUrl,
      },
    };
  },
  methods: {
    async handleIconOk() {
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
      try {
        if (this.password1 != this.password2) return this.$message.error("两次新密码不相等");
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
  width: 200px;
  margin: 0 auto;
  margin-top: 50px;
}
.button {
  margin: 20px 0px 20px 0px;
}
</style>
