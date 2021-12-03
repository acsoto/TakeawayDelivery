<template>
  <div>
    <div style="text-align: right">
      <a-tooltip
        v-if="!editMode"
        placement="top"
      >
        <template #title>
          <span>编辑个人信息</span>
        </template>
        <a-button
          type="link"
          @click="handleEdit"
        >
          <EditOutlined />
        </a-button>
      </a-tooltip>
      <a-tooltip
        v-if="editMode"
        placement="top"
      >
        <template #title>
          <span>取消修改</span>
        </template>
        <a-button
          @click="handleCancel"
          type="link"
        >
          <CloseOutlined />
        </a-button>
      </a-tooltip>
      <a-tooltip
        v-if="editMode"
        placement="top"
      >
        <template #title>
          <span>确认修改</span>
        </template>
        <a-button
          type="link"
          @click="handleConfirm"
        >
          <CheckOutlined />
        </a-button>
      </a-tooltip>
    </div>
    <div>
      <div class="prop-name">用户名</div>
      <a-input
        v-model:value="thisUser.userName"
        class="prop-value"
        readonly
      />
      <div class="prop-name">用户昵称</div>
      <a-input
        v-if="editMode"
        v-model:value="thisUser.userNickName"
        class="prop-value"
      />
      <a-input
        v-else
        v-model:value="thisUser.userNickName"
        class="prop-value"
        readonly
      />
      <div class="prop-name">电话号码</div>
      <a-input
        v-if="editMode"
        v-model:value="thisUser.userTel"
        class="prop-value"
      />
      <a-input
        v-else
        v-model:value="thisUser.userTel"
        class="prop-value"
        readonly
      />
      <div class="prop-name">地址</div>
      <a-input
        v-if="editMode"
        v-model:value="thisUser.userAddress"
        class="prop-value"
      />
      <a-input
        v-else
        v-model:value="thisUser.userAddress"
        class="prop-value"
        readonly
      />
    </div>
  </div>
</template>
<script>
import { EditOutlined, CheckOutlined, CloseOutlined } from '@ant-design/icons-vue';
export default {
  props: ['user'],
  data() {
    return {
      thisUser: {},
      tempUser: {},
      a: "",
      editMode: false,
    };
  },
  components: {
    EditOutlined,
    CheckOutlined,
    CloseOutlined,
  },
  created() {
  },
  methods: {
    handleEdit() {
      this.tempUser.userName = this.thisUser.userName;
      this.tempUser.userNickName = this.thisUser.userNickName;
      this.tempUser.userTel = this.thisUser.userTel;
      this.tempUser.userAddress = this.thisUser.userAddress;
      this.$message.info("已进入编辑模式");
      this.editMode = true;
    },
    handleCancel() {
      this.thisUser.userName = this.tempUser.userName;
      this.thisUser.userNickName = this.tempUser.userNickName;
      this.thisUser.userTel = this.tempUser.userTel;
      this.thisUser.userAddress = this.tempUser.userAddress;
      this.$message.info("已退出编辑模式");
      this.editMode = false;
    },
    async handleConfirm() {
      
      try {
        this.thisUser.userID=this.$store.state.userID;
        const { data: res } = await this.$http.post("api/changeInformation/", this.thisUser);
        //console.log(res)
        if (res.success == false) {
          this.$message.error(res.message);
        }
        else {
          this.$message.success(res.message);
          this.editMode = false;
        }
      } catch (error) {
        this.$message.error("网络异常");
      }
    },

  },
  watch: {
    user() {
      this.thisUser = this.user
    }
  }
};
</script>
<style scoped>
.prop-name {
  margin-top: 15px;
  margin-bottom: 6px;
  font-weight: bold;
  font-size: 20px;
  font-family: '等线';
}
.prop-special-value {
  margin-left: 10px;
  font-family: Serif;
  font-size: 18px;
  color: #304683;
}
.prop-value {
  font-size: 18px;
  font-family: '等线';
}
</style>