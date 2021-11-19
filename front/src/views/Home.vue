<template>
  <div>
    <div
      class="home-body"
      onload="dis()"
    >

      <nav class="shell">
        <ul class="buttons">
          <li class="li">
            <span id="userInfoz">个人信息</span>
            <ul>
              <li
                @click="test()"
                id="idtest"
              >个人信息</li>
              <li
                @click="test1()"
                id="id_order_now"
              >当前订单</li>
              <li
                @click="test2()"
                id="id_order_history"
              >历史订单</li>
              <li
                @click="test3()"
                id="likes"
              >个人收藏夹</li>
              <li
                @click="test4()"
                id="userInfo"
              >修改登录用户密码</li>
              <li
                @click="test5()"
                id="logoff"
              >注销用户</li>
              <li
                @click="test6()"
                id="logff"
              >登出当前用户</li>
            </ul>
          </li>

          <li class="li">
            商铺速览
            <ul>
              <li>学一食堂</li>
              <li>学二食堂</li>
              <li>学三食堂</li>
              <li>学四食堂</li>
              <li>学五食堂</li>
            </ul>
          </li>

          <li class="li">
            评价列表
            <ul>
              <li id="sssss">菜品评价</li>
              <li>速递员评价</li>
              <li>我的评价</li>
            </ul>
          </li>

          <li class="li">
            我接的单
            <ul>
              <li>当前订单</li>
              <li>历史订单</li>
              <li>收到的评价</li>
            </ul>
          </li>
        </ul>

      </nav>

      <table
        id="table"
        class="hovertable"
        border="1"
      >
        <tr>
          <th>ID</th>
          <th>NAME</th>
          <th>TEL</th>
          <th>ADDRESS</th>
        </tr>
        <tr
          onmouseover="this.style.backgroundColor='#ffff66';"
          onmouseout="this.style.backgroundColor='#d4e3e5';"
        >
          <td id="tr1">ID</td>
          <td id="tr2">NAME</td>
          <td id="tr3">TEL</td>
          <td id="tr4">ADDRESS</td>
        </tr>
        <!--    <tr onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">-->
        <!--        <td>Item 2A</td><td>Item 2B</td><td>Item 2C</td>-->
        <!--    </tr>-->
        <!--    <tr onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">-->
        <!--        <td>Item 3A</td><td>Item 3B</td><td>Item 3C</td>-->
        <!--    </tr>-->
        <!--    <tr onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">-->
        <!--        <td>Item 4A</td><td>Item 4B</td><td>Item 4C</td>-->
        <!--    </tr>-->
        <!--    <tr onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">-->
        <!--        <td>Item 5A</td><td>Item 5B</td><td>Item 5C</td>-->
        <!--    </tr>-->
      </table>

      <table
        id="table1"
        class="hovertable"
        border="1"
      >
        <tr>
          <th>ORDER_NOW</th>
        </tr>
        <tr
          onmouseover="this.style.backgroundColor='#ffff66';"
          onmouseout="this.style.backgroundColor='#d4e3e5';"
        >
          <td id="tr1_1">ID</td>
        </tr>

      </table>
      <table
        id="table2"
        class="hovertable"
        border="1"
      >
        <tr>
          <th>ORDER_HISTORY</th>
        </tr>
        <tr
          onmouseover="this.style.backgroundColor='#ffff66';"
          onmouseout="this.style.backgroundColor='#d4e3e5';"
        >
          <td id="tr1_2">ID</td>
        </tr>

      </table>
      <table
        id="table3"
        class="hovertable"
        border="1"
      >
        <tr>
          <th>LIKES</th>
        </tr>
        <tr
          onmouseover="this.style.backgroundColor='#ffff66';"
          onmouseout="this.style.backgroundColor='#d4e3e5';"
        >
          <td id="tr1_3">ID</td>
        </tr>

      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

    };
  },
  created() {

  },
  methods: {
    dis() {
      document.getElementById("table").style.display = 'none';
      document.getElementById("table1").style.display = 'none';
      document.getElementById("table2").style.display = 'none';
      document.getElementById("table3").style.display = 'none';
    },
    test() {
      document.getElementById("table").style.display = 'block';
      document.getElementById("table1").style.display = 'none';
      document.getElementById("table2").style.display = 'none';
      document.getElementById("table3").style.display = 'none';

      // window.location.href="http://localhost:8080/userInfo.html";
      //alert("test");
    },
    test1() {
      document.getElementById("table").style.display = 'none';
      document.getElementById("table2").style.display = 'none';
      document.getElementById("table3").style.display = 'none';
      document.getElementById("table1").style.display = 'block';
      // window.location.href="http://localhost:8080/order_now.html";
      // alert("test1");
    },
    test2() {
      document.getElementById("table").style.display = 'none';
      document.getElementById("table1").style.display = 'none';
      document.getElementById("table3").style.display = 'none';
      document.getElementById("table2").style.display = 'block';
      // window.location.href="http://localhost:8080/order_history.html";
      // alert("test2");
    },
    test3() {
      document.getElementById("table").style.display = 'none';
      document.getElementById("table1").style.display = 'none';
      document.getElementById("table2").style.display = 'none';
      document.getElementById("table3").style.display = 'block';
      // window.location.href="http://localhost:8080/order_now.html";
      // alert("test3");
    },
    test4() {
       this.$router.push({ path: "/userinfo" });
    },
    test5() {
       this.$router.push({ path: "/logout" });
    },
    test6() {
       this.$router.push({ path: "/login" });
    },
  },
}
</script>

<style scoped>
* {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.home-body {
  height: 100vh;
  display: flex;
  align-items: center;
  /*justify-content: center;*/
  /*background-color: #d3dafa;*/
  background-image: linear-gradient(to left, #79defd, #ffffff);
}
.shell {
  position: fixed;
  width: 280px;
  height: 650px;
  background-color: #79defd;
}
.buttons {
  margin: 60px 0;
  color: #ffffff;
}
.li {
  letter-spacing: 2px;
  font: 600 17px "";
  padding: 16px 52px;
  transition: 1s;
}
.li::after {
  content: "";
  position: absolute;
  left: 20px;
  margin-top: -22px;
  display: block;
  width: 20px;
  height: 20px;
  background-color: #ffffff;
  border-radius: 50%;
}
.buttons > li:hover {
  background-color: #5bbad7;
}

.li ul {
  width: 0;
  height: 530px;
  padding: 60px 0;
  position: absolute;
  top: 0;
  right: 0;
  overflow: hidden;
  background-color: #3b91ac;
  transition: 1s;
}

.li ul li {
  padding: 16px 24px;
  transition: 1s;
}

.li:hover ul {
  width: 228px;
}
.li ul li:hover {
  background-color: #7fc6dc;
}
.hovertable {
  margin-left: 500px;
  /*height: 600px;*/
  /*width: 600px;*/
}
</style>
    <style type="text/css" scoped>
table.hovertable {
  font-family: verdana, arial, sans-serif;
  font-size: 11px;
  color: #333333;
  border-width: 1px;
  border-color: #999999;
  border-collapse: collapse;
}
table.hovertable th {
  background-color: #c3dde0;
  width: 150px;
  /*border-width: 1px;*/
  padding: 8px;
  border-style: solid;
  border-color: #a9c6c9;
}
table.hovertable tr {
  background-color: #d4e3e5;
  width: 150px;
}
table.hovertable td {
  /*border-width: 1px;*/
  width: 150px;
  padding: 8px;
  border-style: solid;
  border-color: #a9c6c9;
}
</style>