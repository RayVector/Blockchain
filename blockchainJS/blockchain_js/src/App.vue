<template>
  <div id="app" class="mt-5 ml-5">
    <Home></Home>
  </div>
</template>

<script>
  import Home from "./components/Home";

  export default {
    components: {Home}
  }
</script>

<style lang="stylus">
  html {
    height: 95vh
    width: 100%
  }
  body {
    height: 100%;
    width: 100%;
    background-color: #494949 !important;
  }
</style>