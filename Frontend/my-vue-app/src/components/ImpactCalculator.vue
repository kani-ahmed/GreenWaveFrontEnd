<template>
  <div class="impact-calculator">
    <AppHeader />
    <ImageActions :bottle-counts="bottleCounts" @add-bottle="addBottle" @generate-score="generateImpactScore" @get-savings="getSavings" />
    <ResultsSection :impact-score="impactScore" :savings-amount="savingsAmount" />
  </div>
</template>

<script>
import AppHeader from './Header.vue'
import ImageActions from './ImageActions.vue'
import ResultsSection from './Results.vue'

export default {
  name: 'ImpactCalculator',
  components: {
    AppHeader,
    ImageActions,
    ResultsSection
  },
  data() {
    return {
      bottleCounts: {
        'dp8': 0,
        'dp12': 0,
        'dp16.9': 0,
        'rp17': 0, 
        'rp25': 0,
        'rm12': 0,
        'rm17': 0,
        'rm25': 0
      },
      impactScore: '',
      savingsAmount: '',
    };
  },
  methods: {
    addBottle(bottleType) {
      if (bottleType !== "pick") {
        this.bottleCounts[bottleType]++;
        console.log(`${this.bottleCounts[bottleType]} ${bottleType} added.`);
        console.log("Current Bottle Counts:", this.bottleCounts);
      }
    },
    //generateImpactScore() {
    //  this.impactScore = "GENERATED SCORE";
    //  console.log("Impact Score generated"); 
    //}
    generateImpactScore() {
      // Points assigned to each bottle type
      const pointsPerBottle = {
        'dp8': 1,    // 8 oz bottle = 1 point
        'dp12': 3,   // 12 oz = 3 points
        'dp16.9': 5, // 16 oz = 5 points
        // The rest don't contribute to the total points
      };

      // Calculate the total impact score
      let score = 0;
      for (const bottleType in this.bottleCounts) {
        if (Object.hasOwnProperty.call(pointsPerBottle, bottleType)) {
          score += this.bottleCounts[bottleType] * pointsPerBottle[bottleType];
        }
      }

      // Update the impactScore state
      this.impactScore = score;
      console.log("Impact Score generated:", this.impactScore);
    },
    getSavings() {
      this.savingsAmount = "GENERATED SAVINGS";
      console.log("Savings Score generated");
    }
  }
}
</script>

<style scoped>
.impact-calculator {
  text-align: center;
}
</style>