<template>
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>

    <div class="actions">
      <!-- Retained from kyle-ktk33 for dropdown selection -->
      <select name="bottle" class="child bottle" id="bottlepicker">
        <option value="Pick Bottle">Pick a bottle!</option>
        <option value="Disposable Plastic 8oz">Disposable Plastic 8oz</option>
        <option value="Disposable Plastic 12oz">Disposable Plastic 12oz</option>
        <option value="Disposable Plastic 16.9oz">Disposable Plastic 16.9oz</option>
        <option value="Reusable Plastic 17 oz">Reusable Plastic 17 oz</option>
        <option value="Reusable Plastic 25 oz">Reusable Plastic 25 oz</option>
        <option value="Reusable Metal 12 oz">Reusable Metal 12 oz</option>
        <option value="Reusable Metal 17 oz">Reusable Metal 17 oz</option>
        <option value="Reusable Metal 25 oz">Reusable Metal 25 oz</option>
      </select>
      <!-- Using images for a more interactive UI, from HEAD -->
      <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="addBottle" />
      <img src="@/assets/leaf.png" alt="Leaf Image" @click="generateImpactScore" />
      <img src="@/assets/saving.png" alt="Saving Image" @click="getSavings" />
      
      <!-- Buttons for actions from kyle-ktk33, possibly as an alternative or additional method to interact with the app -->
      <button class="child bottle" id="bottle" @click="addBottle">Add bottle!</button>
      <button class="child score" id="scoreButton" @click="generateImpactScore">
        Generate Score
      </button>
      <button class="child savings" id="savingsButton" @click="getSavings">
        Click To Get Your Savings!
      </button>

      <!-- Results display -->
      <div id="scoreDisplay">{{ impactScore }}</div>
      <div id="savingsDisplay">{{ savingsAmount }}</div>
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

.actions img {
  width: 375px;
  height: 375px;
  margin: 10px;
}

#score {
  font-size: 20px;
  font-weight: bold;
}
</style>


<script>
export default {
  name: 'ImpactCalculator',
  data() {
    return {
      bottlesAdded: 0,
      impactScore: '', // Added for displaying impact score
      savingsAmount: '', // Added for displaying savings amount
    };
  },
  methods: {
    addBottle() {
      // Assuming your logic for adding a bottle remains the same
      this.bottlesAdded++;
      // Further logic to handle bottle addition
    },
    generateImpactScore() {
      this.impactScore = "GENERATED SCORE"; // Update via Vue reactive data
      console.log("Impact Score generated");
    },
    getSavings() {
      this.savingsAmount = "GENERATED SAVINGS"; // Update via Vue reactive data
      console.log("Savings Score generated");
    }
  }
}

</script>
