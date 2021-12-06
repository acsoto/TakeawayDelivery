<template>
  <a-layout-sider
    v-model="collapsed"
    collapsible
    @collapse="handleCollapse"
    :style="{ overflow: 'auto', height: '100vh', left: 0 }"
  >

    <div class="logo" />
    <a-menu
      theme="dark"
      :default-selected-keys="['1']"
      mode="inline"
    >
      <!--      <a-menu-item>-->
      <!--        <a-card hoverable style="width: 240px">-->
      <!--          <template #cover>-->
      <!--            <img alt="example" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />-->
      <!--          </template>-->
      <!--          <a-card-meta title="Europe Street beat">-->
      <!--            <template #description>www.instagram.com</template>-->
      <!--          </a-card-meta>-->
      <!--        </a-card>-->
      <!--        <a-avatar :size="{ xs: 24, sm: 32, md: 40, lg: 64, xl: 80, xxl: 100 }"-->
      <!--                  src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"-->
      <!--                  >-->
      <!--        </a-avatar>-->
      <!--      </a-menu-item>-->
      <a-sub-menu key="sub1">
        <template v-slot:title>
          <UserOutlined />
          <span v-if="collapsed">个人中心</span>
        </template>
        <a-menu-item
          key="1"
          @click="handleClickMenu('个人中心')"
        >
          <router-link to="userinfo">
            个人信息
          </router-link>
        </a-menu-item>
        <a-menu-item
          key="2"
          @click="handleClickMenu('个人中心')"
        >
          <router-link to="orderquery">
            我的订单
          </router-link>
        </a-menu-item>
        <a-menu-item
          key="3"
          @click="handleClickMenu('个人中心')"
        >
          <router-link to="userstar">
            我的最爱
          </router-link>
        </a-menu-item>
        <a-menu-item key="6">
          用户注销
        </a-menu-item>
        <a-menu-item
          key="7"
          @click="$store.commit('logout')"
        >
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
        <a-menu-item
          key="11"
          @click="handleClickMenu('商铺')"
        >
          <router-link to="restaurants">
            所有餐厅
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <!-- <a-sub-menu key="sub3">
        <template v-slot:title>
          <a-icon type="user" />
          <CommentOutlined />
          <span v-if="collapsed">讨论区</span>
        </template>
        <a-menu-item key="13">
          <router-link to="/home/discussion">
            菜品贴
          </router-link>
        </a-menu-item>
        <a-menu-item key="14">
          <router-link to="/home/discussionme">
            与我有关的
          </router-link>
        </a-menu-item>
        <a-menu-item key="15">
          <router-link to="mydiscussion">
            我发布的
          </router-link>
        </a-menu-item>
      </a-sub-menu> -->
      <a-sub-menu key="sub4">
        <template v-slot:title>
          <a-icon type="team" />
          <CarOutlined />
          <span v-if="collapsed">订单查询</span>
        </template>
        <a-menu-item
          key="16"
          @click="handleClickMenu('订单查询')"
        >
          <router-link to="ordernow">
            我接的单
          </router-link>
        </a-menu-item>
        <a-menu-item
          key="17"
          @click="handleClickMenu('订单查询')"
        >
          <router-link to="orders">
            全部订单
          </router-link>
        </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub5">
        <template v-slot:title>
          <a-icon type="team" />
          <SettingOutlined />
          <span v-if="collapsed">系统设置</span>
        </template>
        <a-menu-item
          key="18"
          @click="handleClickMenu('系统设置')"
        >
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
  methods: {
    handleCollapse() {
      this.collapsed = !this.collapsed;
    },
    handleClickMenu(name) {
      this.$store.commit('setPath', { name: name })
    },
  },
  components: {
    UserOutlined,
    ShoppingCartOutlined,
    // CommentOutlined,
    CarOutlined,
    CoffeeOutlined,
    SettingOutlined,
  },
});
</script>

<style scoped>
.icons-list :deep(.anticon) {
  margin-right: 6px;
  font-size: 24px;
}
::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 0px; /*高宽分别对应横竖滚动条的尺寸*/
  height: 0px; /*没想到吧，滚动条直接被我进行了一个横竖都调成0的动作，虽然可以用但是页面上完全看不到，名存实亡的概念！*/
}
</style>