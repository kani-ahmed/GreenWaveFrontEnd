<template>
  <div id="app">
    <div class="logo-wrapper">
      <img alt="Vue logo" src="./assets/logo.png" style="width: 500px;">
    </div>
    <ImpactCalculator />
  </div>
</template>

<script>
import ImpactCalculator from './components/ImpactCalculator.vue'

export default {
  name: 'App',
  components: {
    ImpactCalculator
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.logo-wrapper {
  background-image: url('@/assets/background.png');
  background-size: cover;
  background-position: center;
  padding: 20px; /* Adjust padding as needed */
}
</style>
