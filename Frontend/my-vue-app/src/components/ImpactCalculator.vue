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
      }
    },
    generateImpactScore() {
      this.impactScore = "GENERATED SCORE";
      console.log("Impact Score generated");
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