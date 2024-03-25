<template>
  <!-- html formatting for feature 1 page -->
  <div class="impact-calculator">
    <header>
      <h1>Impact Calculator</h1>
    </header>


    <div class="actions">



      <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="addBottle" />
      <img src="@/assets/leaf.png" alt="Leaf Image" @click="generateImpactScore" />
      <img src="@/assets/saving.png" alt="Saving Image" @click="getSavings" />

      
      
      <div id="score"></div>
      <div id="savings"></div>


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
