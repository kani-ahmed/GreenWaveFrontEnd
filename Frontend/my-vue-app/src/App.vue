<template>
  <div id="app">
    <div class="logo-wrapper">
      <img alt="Vue logo" src="./assets/logo.png" style="width: 500px;">
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

body {
  background-color: #e4fcec; /* Sets the background color for the whole page */
  margin: 0; /* Removes any default margin that may cause white spaces around the edges */
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-color: #e4fcec; /* New green color for the app background */
}

</style>

