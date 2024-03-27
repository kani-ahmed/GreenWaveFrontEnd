<template>
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>

    <div class="image-actions">
      <div class="image-action">
        <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="addBottle" />
        <button class="child bottle" @click="addBottle">Add bottle!</button>
        <!-- Dropdown moved here, directly below the "Add bottle" button -->
        <select name="bottle" class="child bottle" id="bottlepicker">
          <option value="pick">Pick a bottle!</option>
          <!-- Additional bottle options -->
          <option value="dp8">Disposable Plastic 8oz</option>
          <option value="dp12">Disposable Plastic 12oz</option>
          <option value="dp16.9">Disposable Plastic 16.9oz</option>
          <option value="rp17">Reusable Plastic 17 oz</option>
          <option value="rp25">Reusable Plastic 25 oz</option>
          <option value="rm12">Reusable Metal 12 oz</option>
          <option value="rm17">Reusable Metal 17 oz</option>
          <option value="rm25">Reusable Metal 25 oz</option>
        </select>
      </div>
      <div class="image-action">
        <img src="@/assets/leaf.png" alt="Leaf Image" @click="generateImpactScore" />
        <button class="child score" @click="generateImpactScore">Generate Score</button>
      </div>
      <div class="image-action">
        <img src="@/assets/saving.png" alt="Saving Image" @click="getSavings" />
        <button class="child savings" @click="getSavings">Click To Get Your Savings!</button>
      </div>
    </div>

    <div class="results">
      <div id="scoreDisplay">{{ impactScore }}</div>
      <div id="savingsDisplay">{{ savingsAmount }}</div>
    </div>
  </div>
</template>

<style scoped>
/* General styling for the impact calculator */
.impact-calculator header {
  text-align: center;
}

.image-actions {
  display: flex;
  justify-content: center;
  gap: 20px; /* Space between each image-action */
}

.image-action {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center align image and button vertically */
  margin-bottom: 20px;
}

.image-action img {
  width: 100px;
  height: auto;
  cursor: pointer;
}


.image-action button {
  margin-top: 10px; /* Space between image and button */
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

/* New CSS rule for the dropdown to ensure it's styled correctly and aligned under the button */
.image-action select {
  margin-top: 10px; /* Space between button and dropdown */
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  width: 100%; /* Optional: Adjust the width as necessary to match the button above */
}

.image-action img {
  width: 150px; /* Increase the width as needed */
  height: auto; /* Keep height auto to maintain aspect ratio */
  cursor: pointer;
  margin: 0 10px; /* Adjust margin as needed */
}

.dropdown-actions {
  display: flex;
  justify-content: center;
  gap: 20px; /* Adjust if you need more space between the dropdown and any nearby elements */
}

.dropdown-actions select {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

.results {
  text-align: center;
  margin-top: 20px;
}

#scoreDisplay, #savingsDisplay {
  font-size: 20px;
  font-weight: bold;
}
</style>





<script>
export default {
  name: 'ImpactCalculator',
  data() {
    return {
      bottleCounts: { // Object to store counts for each bottle type
        'dp8': 0,
        'dp12': 0,
        'dp16.9': 0,
        'rp17': 0,
        'rp25': 0,
        'rm12': 0,
        'rm17': 0,
        'rm25': 0
      },
      impactScore: '', // Added for displaying impact score
      savingsAmount: '', // Added for displaying savings amount
    };
  },
  methods: {
    addBottle(bottleType) {
      // Increase the count for the specified bottle type
      if (bottleType == "pick")
      {
        //throw error
      }
      else
      {
        this.bottleCounts[bottleType]++;
        console.log(`${this.bottleCounts[bottleType]} ${bottleType} added.`);
      }
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
