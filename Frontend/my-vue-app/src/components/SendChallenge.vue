<template>
  <!-- Main container for the send challenge component -->
  <div class="send-challenge">
    <!-- Title -->
    <h2>Create Community Challenges</h2>
    <!-- Content container -->
    <div>

      <!-- Challenge Dropdown -->
    <div class="input-group">
      <!-- Label for Challenge Dropdown -->
      <div class="left-dropdown">
        <label for="challenge">Challenge:</label>
        <!-- Vue Select component for selecting challenges -->
        <vue-select v-model="selectedChallenge" :options="challenges" placeholder="Type to search" class="custom-select"></vue-select>
      </div>
      </div>

      <!-- User Dropdown -->
      <div class="input-group">
        <!-- Label for User Dropdown -->
        <div class="left-dropdown">
          <!--
          <label for="user">User:</label>
           Vue Select component for selecting users
          <vue-select v-model="selectedUser" :options="users" placeholder="Type to search" class="custom-select"></vue-select> -->
        </div>
      </div>
      <!-- Message Textbox -->
    <div class="input-group">
      <label for="message">Message:</label>
      <textarea id="message" class="input-field" rows="4" cols="50" placeholder="Write Your Message Here" v-model="message"></textarea>
    </div>

      <!-- Submit Button -->
      <button class="submit-button" @click="sendChallenge()">Send Community Challenge!</button>

      <!-- Your content goes here -->
    </div>
  </div>
</template>

<script>
import VueSelect from 'vue3-select'; // Import Vue 3 Select
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  computed: {
        ...mapGetters(['currentUser']),
        // Use a computed property to react to changes in currentUser
        userID() {
            return this.currentUser ? this.currentUser.userId : null;
        }
    },
  name: 'SendChallenge',
  components: {
    VueSelect
  },
  data() {
    return {
      selectedChallenge: '',
      selectedUser: '',
      message: '',
      challenges: [
    { value: 1, label: 'Daily Quick Win: Use a paper straw [5 points]' },
    { value: 2, label: 'Weekly Warrior: Do not use any single-use water bottles for an entire week[50 points]' },
    { value: 3, label: 'Monthly Master: Avoid single-use plastics for an entire month[200 points]' },
    { value: 4, label: 'Yearly Hero: Reduce your yearly personal waste by 50% [1000 points]' }
  ],  
    //users: ['Esteban Linarez', 'Kyle Kaufman', 'Preston DeLeo', 'Kani Ahmed', 'Pranav Dhinakar'] // Sample data for users
    };
  },
  methods: {
    sendChallenge() {
  // Check if a challenge is selected
  if (this.selectedChallenge && this.selectedChallenge.value) {
      // Access the value property of selectedChallenge
      const selectedChallengeValue = this.selectedChallenge.value;
      console.log(`Sending challenge "${selectedChallengeValue}" with message: "${this.message}"`);
    if (!this.userID) {
      console.error('Id is empty');
      return;
    }
    const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/create_community_challenge`;
    axios.post(url, {
      challenge_id: selectedChallengeValue, // Use the ID of the selected challenge
      created_by: this.userID
    })
    .then(response => {
      if (response.status === 201) {
        console.log(response.data);
        this.content = response.data;
        console.log(this.content);
      } else {
        console.error('Post not found.');
      }
    })
    .catch(error => {
      console.error("Error:", error.response);
    });
    // Reset selected challenge, user, and message after sending
    this.selectedChallenge = '';
    this.selectedUser = '';
    this.message = '';
  } else {
    // Display an error message if either challenge is not selected
    console.error('Please select both a challenge and a user before sending.');
  }
  }
  }
}
</script>

<style scoped>
/* Styles specific to this component */

/* Title style */
.centered-title {
  font-size: 2.5em;
  text-align: left; /* Align the title to the left */
}

/* Container for input groups */
.input-group {
  margin-bottom: 20px; /* Add spacing between each input group */
  text-align: left; /* Align the content within the input group to the left */
}

/* Left-aligned dropdown label style */
.left-dropdown {
  display: block; /* Use block layout */
  margin-bottom: 10px; /* Add spacing between each dropdown */
  text-align: left; /* Align the dropdown label to the left */
}

/* Custom styles for Vue Select */
.custom-select .vs__search {
  width: 100%; /* Make the input box stretch to the entire width within the Vue Select dropdown */
}

/* Textarea style */
.input-field {
  width: 100%; /* Make textarea stretch to the entire width */
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* Submit button style */
.submit-button {
  /* Align the button to the right */
  float: center;
  
  /* Set width and height to make it square */
  width: 100px;
  height: 100px;
  
  /* Optional: Add padding for better visual appearance */
  padding: 10px;
  
  /* Optional: Set background color */
  background-color: #4CAF50;
  
  /* Optional: Set text color */
  color: white;
  
  /* Optional: Set border and border-radius */
  border: none;
  border-radius: 5px;
  
  /* Optional: Add hover effect */
  transition: background-color 0.3s ease;
}

/* Add hover effect */
.submit-button:hover {
  background-color: #45a049; /* Change background color on hover */
}
</style>
