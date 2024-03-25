<template>
  <!-- html formatting for feature 1 page -->
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>
    <div class="actions">
        <select name="bottle" class = "child bottle" id="bottle">
          <option value="Add Bottle">Add a bottle!</option>
          <option value="Disposable Plastic 8oz">Disposable Plastic 8oz</option>
          <option value="Disposable Plastic 12oz">Disposable Plastic 12oz</option>
          <option value="Disposable Plastic 16.9oz">Disposable Plastic 16.9oz</option>
          <option value="Reuseable Plastic 17 oz">Reuseable Plastic 17 oz</option>
          <option value="Reuseable Plastic 25 oz">Reuseable Plastic 25 oz</option>
          <option value="Reuseable Metal 12 oz">Reuseable Metal 12 oz</option>
          <option value="Reuseable Metal 17 oz">Reuseable Metal 17 oz</option>
          <option value="Reuseable Metal 25 oz">Reuseable Metal 25 oz</option>
        </select>

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
