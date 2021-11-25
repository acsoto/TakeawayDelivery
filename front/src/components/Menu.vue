<template>
  <a-layout-sider v-model="collapsed" collapsible @collapse="handleCollapse">

    <div class="logo" />
    <a-menu theme="dark" :default-selected-keys="['1']" mode="inline">
      <a-sub-menu key="sub1">
        <template v-slot:title>
          <UserOutlined />
          <span v-if="collapsed">个人中心</span>
        </template>
        <a-menu-item key="1">
          <router-link to="/home/userinfo">
            个人信息
          </router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="/home/orderquery">
            订单查询
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <router-link to="/home/userstar">
            我的最爱
          </router-link>
        </a-menu-item>
        <a-menu-item key="4" @click="showDrawer">
          修改信息
        </a-menu-item>
        <a-menu-item key="5">
          修改密码
        </a-menu-item>
        <a-menu-item key="6">
          用户注销
        </a-menu-item>
        <a-menu-item key="7">
          <router-link to="/login">
            用户登出
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub2">
        <template v-slot:title>
          <a-icon type="desktop" />
          <ShoppingCartOutlined />
          <span v-if="collapsed">商铺</span>
        </template>
        <a-menu-item key="8">
          <router-link to="/home/restaurant1">
            学一食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="9">
          <router-link to="/home/restaurant2">
            学二食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="10">
          <router-link to="/home/restaurant3">
            学三食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="11">
          <router-link to="/home/restaurant4">
            学四食堂
          </router-link>
        </a-menu-item>
        <a-menu-item key="12">
          <router-link to="/home/restaurant5">
            学五食堂
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub3">
        <template v-slot:title><a-icon type="user" />
          <CommentOutlined />
          <span v-if="collapsed">讨论区</span>
        </template>
        <a-menu-item key="13">
          <router-link to="/home/discussion">
            菜品贴
          </router-link>
        </a-menu-item>
        <a-menu-item key="14">
          与我有关的
        </a-menu-item>
        <a-menu-item key="15">
          我发布的
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub4">
        <template v-slot:title><a-icon type="team" />
          <CarOutlined />
          <span v-if="collapsed">我接的单</span>
        </template>
        <a-menu-item key="16">
          <router-link to="ordernow">
            当前订单
          </router-link>
        </a-menu-item>
        <a-menu-item key="17">
          历史订单
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub5">
        <template v-slot:title><a-icon type="team" />
          <SettingOutlined />
          <span v-if="collapsed">系统设置</span>
        </template>
        <a-menu-item key="18">
          <router-link to="developmentteam">
            开发团队
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <a-menu-item key="19">
        <CoffeeOutlined />
        <span>暂未想好写什么的一栏</span>
      </a-menu-item>
    </a-menu>
  </a-layout-sider>
  <a-drawer
      title="Create a new account"
      :width="720"
      :visible="visible"
      :body-style="{ paddingBottom: '80px' }"
      :footer-style="{ textAlign: 'right' }"
      @close="onClose"
  >
    <a-form :model="form" :rules="rules" layout="vertical">
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="Name" name="name">
            <a-input v-model:value="form.name" placeholder="Please enter user name" />
          </a-form-item>
        </a-col>
        <a-col :span="12">
          <a-form-item label="Url" name="url">
            <a-input
                v-model:value="form.url"
                style="width: 100%"
                addon-before="http://"
                addon-after=".com"
                placeholder="please enter url"
            />
          </a-form-item>
        </a-col>
      </a-row>
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="Owner" name="owner">
            <a-select v-model:value="form.owner" placeholder="Please a-s an owner">
              <a-select-option value="xiao">Xiaoxiao Fu</a-select-option>
              <a-select-option value="mao">Maomao Zhou</a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
        <a-col :span="12">
          <a-form-item label="Type" name="type">
            <a-select v-model:value="form.type" placeholder="Please choose the type">
              <a-select-option value="private">Private</a-select-option>
              <a-select-option value="public">Public</a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
      </a-row>
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="Approver" name="approver">
            <a-select v-model:value="form.approver" placeholder="Please choose the approver">
              <a-select-option value="jack">Jack Ma</a-select-option>
              <a-select-option value="tom">Tom Liu</a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
        <a-col :span="12">
          <a-form-item label="DateTime" name="dateTime">
            <a-date-picker
                v-model:value="form.dateTime"
                style="width: 100%"
                :get-popup-container="trigger => trigger.parentNode"
            />
          </a-form-item>
        </a-col>
      </a-row>
      <a-row :gutter="16">
        <a-col :span="24">
          <a-form-item label="Description" name="description">
            <a-textarea
                v-model:value="form.description"
                :rows="4"
                placeholder="please enter url description"
            />
          </a-form-item>
        </a-col>
      </a-row>
    </a-form>
      <a-button style="margin-right: 8px" @click="onClose">Cancel</a-button>
      <a-button type="primary" @click="onClose">Submit</a-button>
  </a-drawer>
  <!--    <a-layout-header style="background: #fff; padding: 0">-->
  <!--      <i class="el-icon-back" @click="() => (collapsed = !collapsed)" />-->
  <!--    </a-layout-header>-->

</template>

<script>
import { defineComponent, reactive, ref } from 'vue';
import { UserOutlined, ShoppingCartOutlined, CommentOutlined, CarOutlined, CoffeeOutlined, SettingOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  name: "Menu",
  data() {
    return {
      collapsed: true,
    };
  },
  methods:{
    handleCollapse(collapsed){
      console.log(collapsed);
      this.collapsed = !this.collapsed;
    },
  },
  components: {
    UserOutlined,
    ShoppingCartOutlined,
    CommentOutlined,
    CarOutlined,
    CoffeeOutlined,
    SettingOutlined,
  },
  setup() {
    const form = reactive({
      name: '',
      url: '',
      owner: '',
      type: '',
      approver: '',
      dateTime: '',
      description: '',
    });
    const rules = {
      name: [{
        required: true,
        message: 'Please enter user name',
      }],
      url: [{
        required: true,
        message: 'please enter url',
      }],
      owner: [{
        required: true,
        message: 'Please select an owner',
      }],
      type: [{
        required: true,
        message: 'Please choose the type',
      }],
      approver: [{
        required: true,
        message: 'Please choose the approver',
      }],
      dateTime: [{
        required: true,
        message: 'Please choose the dateTime',
        type: 'object',
      }],
      description: [{
        required: true,
        message: 'Please enter url description',
      }],
    };
    const visible = ref(false);

    const showDrawer = () => {
      visible.value = true;
    };

    const onClose = () => {
      visible.value = false;
    };
    return {
      form,
      rules,
      visible,
      showDrawer,
      onClose,
    };
  },
});
</script>

<style scoped>
.icons-list :deep(.anticon) {
  margin-right: 6px;
  font-size: 24px;
}
</style>
