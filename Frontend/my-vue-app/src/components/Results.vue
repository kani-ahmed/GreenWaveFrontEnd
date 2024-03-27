<template>
  <div class="results">
    <div id="scoreDisplay">{{ impactScore }}</div>
    <div id="savingsDisplay">{{ savingsAmount }}</div>
  </div>
</template>

<script>
export default {
  name: 'ResultsSection',
  props: ['impactScore', 'savingsAmount']
}
</script>

<style scoped>
.results {
  text-align: center;
  margin-top: 20px;
}

#scoreDisplay, #savingsDisplay {
  font-size: 20px;
  font-weight: bold;
}
</style>