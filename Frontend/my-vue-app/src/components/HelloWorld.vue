<template>
  <!-- html formatting for feature 1 page -->
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>
    <div class="actions">
      <button @click="addBottle"> Add Bottle </button>
      <div class="score" @click="generateImpactScore">
        Click To Generate Your Impact Score {{ username }}!
      </div>
      <div class="savings" @click="getSavings">
        Click To Get Your Savings {{ username }}!
      </div>
    </div>
  </div>
</template>


<style scoped>
/* css formatting for feature 1 page */
.impact-calculator header {
  text-align: center;
}

.actions {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.actions>* {
  margin: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.score {
  background-color: limegreen;
}

.savings {
  background-color: lightgreen;
  transform: rotate(45deg);
}
</style>


<script>
export default {
  name: 'ImpactCalculator',
  data() {
    return {
      username: 'USERNAME',
      bottlesAdded: 0,
    };
  },
  methods: {
    addBottle() {
      this.bottlesAdded++;
      // Further logic to handle bottle addition
    },
    generateImpactScore() {
      // Logic to generate impact score
      console.log("HELLO");
    },
    getSavings() {
      // Logic to calculate savings
    }
  }
}
</script>
