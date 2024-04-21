<template>
  <!-- Challenge Inbox component template -->
  <div class="challenge-inbox">
    <!-- Title -->
    <h2>Challenge Inbox</h2>
    <!-- Divider -->
    <hr class="divider">
    <!-- Header row -->
    <div class="grid-container">
      <div class="grid-item sender">Sender</div>
      <div class="grid-item challenge">Challenge</div>
      <div class="grid-item accept">Accept/Reject</div>
    </div>
    <!-- Dynamic challenge rows -->
    <div class="grid-container" v-for="(challenge, index) in challenges" :key="index">
      <div class="grid-item sender">{{ challenge.sender }}</div>
      <div class="grid-item challenge">{{ challenge.description }}</div>
      <div class="grid-item accept">
        <!-- Accept and Reject buttons -->
        <button @click="acceptChallenge(index)" class="accept-button"><i class="fas fa-check"></i> Accept Challenge</button>
        <button @click="rejectChallenge(index)" class="reject-button"><i class="fas fa-times"></i> Reject Challenge</button>
      </div>
    </div>
    <!-- Temporary add challenge button -->
    <button class="temp-add-challenge" @click="tempAddChallenge('Sender', 'Test Challenge')">Temp Add Challenge</button>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'ChallengeInbox',
  computed: {
    ...mapGetters(['currentUser']),
    userID() {
      return this.currentUser ? this.currentUser.userId : null;
    },
  },
  data() {
    return {
      challenges: [] // Array to store challenge items
    };
  },
  methods: {
    acceptChallenge(index) {
      console.log('Accepting challenge:', this.challenges[index]);
      this.challenges.splice(index, 1);
    },
    rejectChallenge(index) {
      console.log('Rejecting challenge:', this.challenges[index]);
      this.challenges.splice(index, 1);
    },
    tempAddChallenge(sender, description) {
      this.challenges.push({ sender, description });
    },

    async joinPersonalChallenge() {
      if (!this.userID) {
        console.error("User ID is empty");
        return;
      }
      const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/join_personal_challenge';
      try {
        const response = await axios.post(url, {
          user_id: this.userID,
          challenge_id: this.challenge_id
        });
        if (response.status === 200) {
          console.log(response.data);
          const challenge = response.data;
          this.challenges.push(challenge);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  },

  async joinCommunityChallenge() {
    if (!this.userID) {
      console.error("User ID is empty");
      return;
    }
    const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/join_community_challenge';
    try {
      const response = await axios.post(url, {
        user_id: this.userID,
        challenge_id: this.challenge_id
      });
      if (response.status === 200) {
        console.log(response.data);
        const challenge = response.data;
        this.challenges.push(challenge);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }
}
</script>



<style scoped>
/* Component-specific styles go here */
.title {
  text-align: center; /* Center-align title */
}

.divider {
  width: 100%; /* Full width divider */
  margin: auto; /* Center divider horizontally */
  border-top: 1px solid black; /* Solid black border */
  margin-bottom: 20px; /* Bottom margin */
}

.grid-container {
  display: flex; /* Flexbox layout */
  border: 1px solid black; /* Solid black border */
  justify-content: space-between; /* Distribute items evenly */
}

.grid-item {
  box-sizing: border-box; /* Border-box sizing */
  padding: 10px; /* Padding around grid items */
  text-align: center; /* Center-align text */
  width: calc(33.33% - 20px); /* Each column takes up 1/3 of the container width */
  margin: 0; /* Remove margin to ensure consistency */
}

/* Button styling */
.accept-button {
  background-color: green; /* Green background for accept button */
  color: white; /* White text color */
  border: none; /* No border */
  padding: 10px; /* Padding around button */
  cursor: pointer; /* Cursor pointer */
  border-radius: 5px; /* Border radius */
}

.reject-button {
  background-color: red; /* Red background for reject button */
  color: white; /* White text color */
  border: none; /* No border */
  padding: 10px; /* Padding around button */
  cursor: pointer; /* Cursor pointer */
  border-radius: 5px; /* Border radius */
}

.temp-add-challenge {
  position: fixed; /* Fixed position */
  bottom: 20px; /* Bottom distance */
  right: 20px; /* Right distance */
  background-color: blue; /* Blue background for temp add button */
  color: white; /* White text color */
  border: none; /* No border */
  padding: 10px; /* Padding around button */
  cursor: pointer; /* Cursor pointer */
  border-radius: 5px; /* Border radius */
}

/* Match padding with headers */
.temporary-values .grid-item {
  padding: 10px; /* Padding around grid items */
}

/* Clear floats for temporary values */
.temporary-values:after {
  content: ""; /* Empty content */
  display: table; /* Display as table */
  clear: both; /* Clear floats */
}
</style>
