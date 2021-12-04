<template>
  <div id="app">
    <keep-alive>
      <router-view v-if="$route.meta.keepAlive" />
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive" />
  </div>
</template>

<script>
export default {};
</script>

<style>
@import './assets/css/main.css';
@import './assets/css/color-dark.css';
</style>
