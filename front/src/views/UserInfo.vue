<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0" >
    </a-layout-header>
    <a-layout-content style="margin: 0 16px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>个人中心</a-breadcrumb-item>
        <a-breadcrumb-item>个人信息</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
        <!--        TODO-->

        <a-table :columns="columns" :data-source="data">
          <template #headerCell="{ column }">
            <template v-if="column.key === 'name'">
        <span>
          <smile-outlined />
          Name
        </span>
            </template>
          </template>

          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'name'">
              <a>
                {{ record.name }}
              </a>
            </template>
            <template v-else-if="column.key === 'tags'">
        <span>
          <a-tag
              v-for="tag in record.tags"
              :key="tag"
              :color="tag === 'loser' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'"
          >
            {{ tag.toUpperCase() }}
          </a-tag>
        </span>
            </template>
            <template v-else-if="column.key === 'action'">
        <span>
          <a>Invite 一 {{ record.name }}</a>
          <a-divider type="vertical" />
          <a>Delete</a>
          <a-divider type="vertical" />
          <a class="ant-dropdown-link">
            More actions
            <down-outlined />
          </a>
        </span>
            </template>
          </template>
        </a-table>


      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>
<script>
// import {DownOutlined, SmileOutlined} from "_@ant-design_icons-vue@6.0.1@@ant-design/icons-vue";

// export default {
//   data() {
//     return {
//       collapsed: true,
//     };
//   },
// };
import { SmileOutlined, DownOutlined } from '@ant-design/icons-vue';


export default {
  data() {
    return {
      collapsed: true,
      data:[],
      columns:[],
      userID:this.$store.state.userID,
    };
  },
  components: {
    SmileOutlined,
    DownOutlined,
  },
  created() {
    this.setColumns();
    this.getData();
  },
  methods:{
    async getData()
    {
      const { data: res } = await this.$http.post("api/getInformation/", {userID:this.userID});
      //console.log(res)
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
      this.data.Name=res.userName
      this.data.Age=res.userNickname
      this.data.Address=res.userAddress
      this.data.Tags=res.userNickname
      this.data.Action=res.userNickname
    },
    setColumns()
    {
      this.columns=[{
        name: 'Name',
        dataIndex: 'name',
        key: 'name',
      }, {
        title: 'Age',
        dataIndex: 'age',
        key: 'age',
      }, {
        title: 'Address',
        dataIndex: 'address',
        key: 'address',
      }, {
        title: 'Tags',
        key: 'tags',
        dataIndex: 'tags',
      }, {
        title: 'Action',
        key: 'action',
      }]
    }

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
</style>
