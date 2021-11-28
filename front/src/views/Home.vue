<template>
  <div>
    <a-layout id="components-layout-demo-side" style="min-height: 100vh;overflow:auto;">
    <my-menu/>
      <a-layout>
    <router-view v-slot="{ Component }">
      <transition name="move" mode="out-in">
        <keep-alive >
          <component :is="Component" />
        </keep-alive>
      </transition>
    </router-view>
      </a-layout>
    </a-layout>
  </div>
</template>

<script>
import MyMenu from '../components/Menu'
export default {
  components:{
    MyMenu,
  },
  data() {
    return {
      collapsed: true,
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
