<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>个人中心</a-breadcrumb-item>
        <a-breadcrumb-item>订单查询</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '500px' }">
        <a-table
          :columns="columns"
          :data-source="data"
        >
          <template #headerCell="{ column }">
            <template v-if="column.key == 'name'">
              <span>
                <smile-outlined />
                Name
              </span>
            </template>
          </template>

          <template #bodyCell="{ column, record }">
            
            <template v-if="column.key == 'action'">
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
            <template v-else-if="column.key === 'orderCompleted'">
              <span >
                <a>{{ record.orderCompleted=='0'?'未送达':'已送达' }}</a>
              </span>
            </template>
          </template>
        </a-table>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©2021 Powered by zzh company
    </a-layout-footer>
  </div>
</template>
<script>
import { SmileOutlined, DownOutlined } from '@ant-design/icons-vue';

export default {
  data() {
    return {
      collapsed: true,
      data: [],
      columns: [],
      userID: this.$store.state.userID,
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
  methods: {
    async getData() {
      const { data: res } = await this.$http.post("api/getInformation/", { userID: this.userID });
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
      this.data = res.userOrders
      console.log(this.data)
    },
    setColumns() {
      this.columns = [{
        title: '订单状态',
        dataIndex: 'orderCompleted',
        key: 'orderCompleted',
      }, {
        title: '派送人',
        dataIndex: 'deliveryUserName',
        key: 'deliveryUserName',
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

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
