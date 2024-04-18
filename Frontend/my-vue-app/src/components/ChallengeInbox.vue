<template>
  <div class="challenge-inbox">
    <h2>Challenge Inbox</h2>
    <hr class="divider">
    <div class="grid-container">
      <div class="grid-item sender">Sender</div>
      <div class="grid-item challenge">Challenge</div>
      <div class="grid-item accept">Accept/Reject</div>
    </div>
    <!-- Temporary values row -->
    <div class="grid-container" v-for="(challenge, index) in challenges" :key="index">
      <div class="grid-item sender">{{ challenge.sender }}</div>
      <div class="grid-item challenge">{{ challenge.description }}</div>
      <div class="grid-item accept">
        <button @click="acceptChallenge(index)" class="accept-button"><i class="fas fa-check"></i> Accept Challenge</button>
        <button @click="rejectChallenge(index)" class="reject-button"><i class="fas fa-times"></i> Reject Challenge</button>
      </div>
    </div>
    <!-- Your challenge inbox content goes here -->
    <button class="temp-add-challenge" @click="tempAddChallenge('Sender', 'Test Challenge')">Temp Add Challenge</button>
  </div>
</template>

<script>
export default {
  name: 'ChallengeInbox',
  // Any component logic goes here
  data() {
    return {
      challenges: [] // Array to store challenge items
    };
  },
  methods: {
    acceptChallenge(index) {
      // Add logic to handle accepting challenge
      console.log('Accepting challenge:', this.challenges[index]);
      // Remove the accepted challenge from the challenges array
      this.challenges.splice(index, 1);
    },
    rejectChallenge(index) {
      // Add logic to handle rejecting challenge
      console.log('Rejecting challenge:', this.challenges[index]);
      // Remove the rejected challenge from the challenges array
      this.challenges.splice(index, 1);
    },
    tempAddChallenge(sender, challenge) {
      // Add logic to temporarily add a challenge
      this.challenges.push({
        sender: sender,
        description: challenge
      });
    }
  }
}
</script>

<style scoped>
/* Component-specific styles go here */
.title {
  text-align: center;
}

.divider {
  width: 100%;
  margin: auto;
  border-top: 1px solid black;
  margin-bottom: 20px;
}

.grid-container {
  display: flex;
  border: 1px solid black;
  justify-content: space-between; /* Distribute items evenly */
}

.grid-item {
  box-sizing: border-box;
  padding: 10px;
  text-align: center;
  width: calc(33.33% - 20px); /* Each column takes up 1/3 of the container width */
  margin: 0; /* Remove margin to ensure consistency */
}

/* Button styling */
.accept-button {
  background-color: green;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
}

.reject-button {
  background-color: red;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
}

.temp-add-challenge {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: blue;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
}

/* Match padding with headers */
.temporary-values .grid-item {
  padding: 10px;
}

/* Clear floats for temporary values */
.temporary-values:after {
  content: "";
  display: table;
  clear: both;
}
</style>
