<template>
  <!-- html formatting for feature 1 page -->
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>
    <div class="actions">
      <button class="child bottle">Add bottle!</button>

      <button class="child score" id="score" @click="generateImpactScore">
        
      </button>
      <button class="child savings" id="savings" @click="getSavings">
        Click To Get Your Savings!
      </button>
    </div>
  </div>
</template>


<style scoped>
/* css formatting for feature 1 page */
.impact-calculator header {
  text-align: center;
}


.actions {
  display: inline-block;
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

.child {
  display: inline-block;
  vertical-align: middle;
}

.bottle {
  color: lightgrey;
  background-color: blue;
}

.score {
  color: lightgrey;
  background-color: rgb(89, 151, 89);
}

.savings {
  color: lightgrey;
  background-color: darkgreen;
}
</style>


<script>
export default {
  name: 'ImpactCalculator',
  data() {

    return {
      bottlesAdded: 0,
      showDropdown: false, // Controls the visibility of the dropdown
    };
  },
  methods: {  
    addBottle() {
      this.bottlesAdded++;
      // Further logic to handle bottle addition
    },
    generateImpactScore() {
      document.getElementById("score").innerHTML = "GENERATED SCORE";
      console.log("Impact Score generated");
    },
    getSavings() {
      document.getElementById("savings").innerHTML = "GENERATED SAVINGS";
      console.log("Savings Score generated");
    }
  }
}
</script>
