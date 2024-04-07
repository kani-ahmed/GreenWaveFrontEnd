<template>
<div class="Gamification">
    <header>
      <h1>Challenge Center</h1>
    </header>
    <main>
      <div class="button-container">
        <div class="button-group left">
          <button class="square-button">Challenge Inbox</button>
          <button class="square-button">Challenges in Progress</button>
          <button class="square-button">Send Challenges</button>
        </div>
        <div class="button-group right">
          <button class="square-button">User Profile</button>
          <button class="square-button">Badges</button>
          <button class="square-button" @click="toggleEcoPoints">{{ ecoPointsText }}</button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'ChallengeCenter',
  data() {
    return {
      ecoPoints: 0, // Initial value of eco points
      ecoPointsText: 'Eco-points' // Initial text of the button
    };
  },
  methods: {
    toggleEcoPoints() {
      if (this.ecoPointsText === 'Eco-points') {
        // Update eco points value (for demonstration, you can update it dynamically in your actual app)
        this.ecoPoints = 0; // Change this value to the desired eco points
        this.ecoPointsText = `You have ${this.ecoPoints} eco points`;
      } else {
        this.ecoPointsText = 'Eco-points';
      }
    }
  }
}
</script>

<style scoped>
/* Add your styles here */
.challenge-center {
  background-color: #eaf6ff; /* Light blue */
}

header {
  color: #000; /* Black text color */
  padding: 10px;
  text-align: center;
}

main {
  padding: 20px;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.button-group {
  display: flex;
  flex-direction: column;
}

.left {
  align-items: flex-start;
}

.right {
  align-items: flex-end;
}

.square-button {
  width: 200px;
  height: 200px;
  margin: 5px;
  border: none;
  background-color: #ddd;
  cursor: pointer;
}
</style>