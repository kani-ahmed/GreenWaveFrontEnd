
<template>
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>

    <div class="actions">
      <!-- Retained from kyle-ktk33 for dropdown selection -->
      <select name="bottle" class="child bottle" id="bottlepicker">
        <option value="pick">Pick a bottle!</option>
        <option value="dp8">Disposable Plastic 8oz</option>
        <option value="dp12">Disposable Plastic 12oz</option>
        <option value="dp16.9">Disposable Plastic 16.9oz</option>
        <option value="rp17">Reusable Plastic 17 oz</option>
        <option value="rp25">Reusable Plastic 25 oz</option>
        <option value="rm12">Reusable Metal 12 oz</option>
        <option value="rm17">Reusable Metal 17 oz</option>
        <option value="rm25">Reusable Metal 25 oz</option>
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
/* General styling for the impact calculator */
.impact-calculator header {
  text-align: center;
}

/* Container for action items, using flexbox for better layout control */
.actions {
  display: flex;
  flex-direction: column; /* Primary direction to stack groups vertically */
  align-items: center; /* Center items horizontally */
  justify-content: center; /* Center items vertically in their container */
}

/* Row container for the image buttons to align them horizontally */
.image-buttons {
  display: flex;
  justify-content: center; /* Center image buttons horizontally */
  margin-bottom: 20px; /* Space between image buttons and the next row */
}

.image-buttons img {
  width: 100px; /* Adjusted width for a better fit */
  height: auto; /* Maintain aspect ratio */
  margin: 0 10px; /* Space between images */
  cursor: pointer;
}

/* Row container for the dropdown and other buttons */
.selection-row {
  display: flex;
  justify-content: center; /* Center elements within the selection row */
  gap: 20px; /* Space between elements */
}

/* Styles for the dropdown and buttons to ensure visual consistency */
.selection-row select,
.selection-row button {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

/* Style adjustments for the display of scores and savings */
#scoreDisplay, #savingsDisplay {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  margin-top: 20px; /* Adds space above the display elements */
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
