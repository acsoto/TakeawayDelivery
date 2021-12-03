<template>
  <div>
    <a-button type="primary">
      <a-icon type="edit" />
      Search
    </a-button>
    <div class="prop-name">用户名</div>
    <a-input
      v-if="editMode"
      :value="thisUser.userName"
      class="prop-value"
    />
    <div
      v-else
      class="prop-value"
    >
      {{thisUser.userName}}
    </div>
    <div class="prop-name">用户昵称</div>
    <a-input
      v-if="editMode"
      :value="thisUser.userNickName"
      class="prop-value"
    />
    <div
      v-else
      class="prop-value"
    >
      {{thisUser.userNickName}}
    </div>
    <div class="prop-name">电话号码</div>
    <a-input
      v-if="editMode"
      :value="thisUser.userTel"
      class="prop-value"
    />
    <div
      v-else
      class="prop-value"
    >
      {{thisUser.userTel}}
    </div>
    <div class="prop-name">地址</div>
    <a-input
      v-if="editMode"
      :value="thisUser.userAddress"
      class="prop-value"
    />
    <div
      v-else
      class="prop-value"
    >
      {{thisUser.userAddress}}
    </div>
  </div>
</template>
<script>
export default {
  props: ['user'],
  data() {
    return {
      thisUser: {},
      editMode: false,
    };
  },
  created() {
  },
  methods: {
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