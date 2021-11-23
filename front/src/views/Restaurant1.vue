<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0" >
    </a-layout-header>
    <a-layout-content style="margin: 0 16px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>商铺</a-breadcrumb-item>
        <a-breadcrumb-item>学一食堂</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '580px' }">
        <a-row type="flex" justify="space-around">
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>
                  <a @click="showDrawer">
                    www.instagram.com
                  </a>
                </template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
        </a-row>
        <a-row type="flex" style="margin-top: 25px" justify="space-around">
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
          <a-col span="5">
            <a-card hoverable>
              <template #cover>
                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />
              </template>
              <a-card-meta title="Europe Street beat">
                <template #description>www.instagram.com</template>
              </a-card-meta>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©2021 Powered by zzh company
    </a-layout-footer>
    <a-drawer width="640" placement="right" :closable="false" :visible="visible" @close="onClose">
      <p :style="[pStyle, pStyle2]">User Profile</p>
      <p :style="pStyle">Personal</p>
      <a-row>
        <a-col :span="12">
          <description-item title="Full Name" content="Lily" />
        </a-col>
        <a-col :span="12">
          <description-item title="Account" content="AntDesign@example.com" />
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item title="City" content="HangZhou" />
        </a-col>
        <a-col :span="12">
          <description-item title="Country" content="China🇨🇳" />
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item title="Birthday" content="February 2,1900" />
        </a-col>
        <a-col :span="12">
          <description-item title="Website" content="-" />
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item
              title="Message"
              content="Make things as simple as possible but no simpler."
          />
        </a-col>
      </a-row>
      <a-divider />
      <p :style="pStyle">Company</p>
      <a-row>
        <a-col :span="12">
          <description-item title="Position" content="Programmer" />
        </a-col>
        <a-col :span="12">
          <description-item title="Responsibilities" content="Coding" />
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item title="Department" content="XTech" />
        </a-col>
        <a-col :span="12">
          <description-item title="Supervisor">
            <template #content><a>Lin</a></template>
          </description-item>
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="24">
          <description-item
              title="Skills"
              content="C / C + +, data structures, software engineering, operating systems, computer networks, databases, compiler theory, computer architecture, Microcomputer Principle and Interface Technology, Computer English, Java, ASP, etc."
          />
        </a-col>
      </a-row>
      <a-divider />
      <p :style="pStyle">Contacts</p>
      <a-row>
        <a-col :span="12">
          <description-item title="Email" content="ant-design-vue@example.com" />
        </a-col>
        <a-col :span="12">
          <description-item title="Phone Number" content="+86 181 0000 0000" />
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="24">
          <description-item title="Github">
            <template #content>
              <a href="https://github.com/vueComponent/ant-design-vue">
                github.com/vueComponent/ant-design-vue
              </a>
            </template>
          </description-item>
        </a-col>
      </a-row>
    </a-drawer>
  </div>
</template>
<script>
import descriptionItem from './Restaurant2';
import { defineComponent, ref } from 'vue';
export default defineComponent({
  data() {
    return {
      collapsed: true,
    };
  },
  components: {
    descriptionItem,
  },

  setup() {
    const visible = ref(false);
    const pStyle = {
      fontSize: '16px',
      color: 'rgba(0,0,0,0.85)',
      lineHeight: '24px',
      display: 'block',
      marginBottom: '16px',
    };
    const pStyle2 = {
      marginBottom: '24px',
    };

    const showDrawer = () => {
      visible.value = true;
    };

    const onClose = () => {
      visible.value = false;
    };

    return {
      visible,
      pStyle,
      pStyle2,
      showDrawer,
      onClose,
    };
  },
});
</script>

<style>
#components-layout-demo-side .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
