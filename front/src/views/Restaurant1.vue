<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px;height:80vh;overflow:auto;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>商铺</a-breadcrumb-item>
        <a-breadcrumb-item>学一食堂</a-breadcrumb-item>
      </a-breadcrumb>
      <!--      <div :style="{ padding: '24px', background: '#fff', minHeight: '580px' }">-->
      <!--&lt;!&ndash;        <a-row type="flex" justify="space-around">&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>&ndash;&gt;-->
      <!--&lt;!&ndash;                  <a @click="showDrawer">&ndash;&gt;-->
      <!--&lt;!&ndash;                    www.instagram.com&ndash;&gt;-->
      <!--&lt;!&ndash;                  </a>&ndash;&gt;-->
      <!--&lt;!&ndash;                </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;        </a-row>&ndash;&gt;-->
      <!--&lt;!&ndash;        <a-row type="flex" style="margin-top: 25px" justify="space-around">&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;          <a-col span="5">&ndash;&gt;-->
      <!--&lt;!&ndash;            <a-card hoverable>&ndash;&gt;-->
      <!--&lt;!&ndash;              <template #cover>&ndash;&gt;-->
      <!--&lt;!&ndash;                <img alt="example" src="https://p0.meituan.net/iphoenix/5feab57263af405b10bb0d44a9d399851354587.jpg@732w_412h_80Q_1e_1c" />&ndash;&gt;-->
      <!--&lt;!&ndash;              </template>&ndash;&gt;-->
      <!--&lt;!&ndash;              <a-card-meta title="Europe Street beat">&ndash;&gt;-->
      <!--&lt;!&ndash;                <template #description>www.instagram.com</template>&ndash;&gt;-->
      <!--&lt;!&ndash;              </a-card-meta>&ndash;&gt;-->
      <!--&lt;!&ndash;            </a-card>&ndash;&gt;-->
      <!--&lt;!&ndash;          </a-col>&ndash;&gt;-->
      <!--&lt;!&ndash;        </a-row>&ndash;&gt;-->


      <!--      </div>-->
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
        <!--        TODO-->
        <div v-for="(food,index) in data" :key="food" style="display:inline-block;">
          <div style="height:200px;width:100px;">
            <a-card hoverable style="width:20%;">
              <template #cover>
                <img
                    style="height:100px;width:100px"
                    alt="example"
                    :src="food.foodUrl"
                />
              </template>
              <a-card-meta :title="food.foodName">
                <template #description>{{ food.foodPrice }}</template>
              </a-card-meta>
            </a-card>

            <br v-if="index % 4 == 0"/>
          </div>
        </div>
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
          <description-item title="Full Name" content="Lily"/>
        </a-col>
        <a-col :span="12">
          <description-item title="Account" content="AntDesign@example.com"/>
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item title="City" content="HangZhou"/>
        </a-col>
        <a-col :span="12">
          <description-item title="Country" content="China🇨🇳"/>
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item title="Birthday" content="February 2,1900"/>
        </a-col>
        <a-col :span="12">
          <description-item title="Website" content="-"/>
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
      <a-divider/>
      <p :style="pStyle">Company</p>
      <a-row>
        <a-col :span="12">
          <description-item title="Position" content="Programmer"/>
        </a-col>
        <a-col :span="12">
          <description-item title="Responsibilities" content="Coding"/>
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="12">
          <description-item title="Department" content="XTech"/>
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
      <a-divider/>
      <p :style="pStyle">Contacts</p>
      <a-row>
        <a-col :span="12">
          <description-item title="Email" content="ant-design-vue@example.com"/>
        </a-col>
        <a-col :span="12">
          <description-item title="Phone Number" content="+86 181 0000 0000"/>
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
export default {
  data() {
    return {
      collapsed: true,
      data: [],
      columns: [],
      storeID: 1,
    };
  },
  created() {
    this.getData();
  },
  methods: {
    async getData() {
      const {data: res} = await this.$http.post("api/getStoreInformation/", {storeID: this.storeID});
      console.log(res)
      // if (res.success == false) {
      //   this.$message.error(res.message);
      // }
      // else {
      //   this.$store.commit("login", { userName: this.param.userName, userID: res.userID });//注意一下，store貌似只能传一个参数，建议传个对象过去。
      //   //获取存入的userID的方式：this.$store.state.userID   (注意是this.$store.state.XXX，千万别落什么东西)
      //   //console.log(this.$store.state)
      //   this.$message.success(res.message);
      //   this.$router.push({ path: "/home" });
      // }
      this.data = res.food
      console.log(this.data)
    },

  },
};
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
