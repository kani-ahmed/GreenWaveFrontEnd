<template>
  <!-- Main container for the send challenge component -->
  <div class="send-challenge">
    <!-- Title -->
    <h2 class = "header">Create Challenges</h2>
    <!-- Content container -->
    <div>
       <!-- Toggle button for personal and community challenges -->
       <div class="toggle-button">
  <button class="toggle-btn" :class="{ active: showPersonal }" @click="showPersonal = true">Personal Challenge</button>
  <button class="toggle-btn" :class="{ active: !showPersonal }" @click="showPersonal = false">Community Challenge</button>
</div>
      <!-- Challenge Dropdown -->
      <div v-if="showPersonal">
    <div class="input-group">
       <!-- Label for Personal Challenge Dropdown -->
      <div class="left-dropdown">
        <label for="challenge" class="dropdown-label personal-label">Personal Challenge:</label>
        <div class="challenge-form">
    <div class="form-group">
      <label for="challenge-title">Challenge Title:</label>
      <input type="text" id="challenge-title" v-model="challengeTitle" placeholder="Enter challenge title">
    </div>

    <div class="form-group">
      <label for="challenge-description">Challenge Description:</label>
      <textarea id="challenge-description" v-model="challengeDescription" placeholder="Enter challenge description"></textarea>
    </div>

    <div class="form-group">
      <label for="eco-points">Eco Point Reward:</label>
      <input type="number" id="eco-points" v-model="ecoPoints" placeholder="Enter Eco Points">
    </div>

    <div class="form-group">
      <label for="duration">Duration:</label>
      <select id="duration" v-model="duration">
        <option value="day">Day</option>
        <option value="week">Week</option>
        <option value="month">Month</option>
        <option value="year">Year</option>
      </select>
    </div>
  </div>

      </div>
      </div>

      <!-- Submit Button -->
      <button class="submit-button" @click="sendPersonalChallenge()">Send Personal Challenge!</button>
    </div>
    <!-- Vue Select component replaced by standard select for community challenges -->
    <div v-else>
      <div class="input-group">
        <div class="left-dropdown">
          <label for="community-challenge-select" class="dropdown-label personal-label">Community Challenge:</label>
          <select id="community-challenge-select" v-model="selectedCommunityChallenge" class="custom-select">
            <option v-for="option in challenges" :value="option.value" :key="option.value">
              {{ option.label }}
            </option>
          </select>
        </div>
      </div>
      <!-- Submit Button -->
      <button class="submit-button" @click="sendCommunityChallenge()">Send Community Challenge!</button>
    </div>

      <!-- Your content goes here -->
    </div>
  </div>
</template>

<script>
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
    
  },
  data() {
    return {
      selectedCommunityChallenge: '',
      selectedPersonalChallenge: '',
      content: null,
      showPersonal: true,
      challenges: [
    { value: 1, label: 'Daily Quick Win: Refuse a plastic straw [5 points]' },
    { value: 2, label: 'Weekly Warrior: Use a refillable water bottle for a week[50 points]' },
    { value: 3, label: 'Monthly Master: Avoid all single-use plastics for a month[200 points]' },
    { value: 4, label: 'Yearly Hero: Reduce personal waste by 50% [1000 points]' }
  ],  
    //users: ['Esteban Linarez', 'Kyle Kaufman', 'Preston DeLeo', 'Kani Ahmed', 'Pranav Dhinakar'] // Sample data for users
    };
  },
  methods: {
    async sendPersonalChallenge() {
  // Check if all input fields have values
  if (
    this.challengeTitle &&
    this.challengeDescription &&
    this.ecoPoints &&
    this.duration
  ) {
    // If all fields have values, log them
    console.log('Challenge Title:', this.challengeTitle);
    console.log('Challenge Description:', this.challengeDescription);
    console.log('Eco Point Reward:', this.ecoPoints);
    console.log('Duration:', this.duration);
    // Get the current date
// Get the current date
const currentDate = new Date();

// Format the current date
const formattedCurrentDate = `${currentDate.getFullYear()}-${String(
  currentDate.getMonth() + 1
).padStart(2, '0')}-${String(currentDate.getDate()).padStart(2, '0')}`;

console.log('Current Date:', formattedCurrentDate);
// Initialize variables for future date calculation
let futureDate = new Date(currentDate);

// Calculate the future date based on the selected duration
switch (this.duration) {
  case 'day':
    futureDate.setDate(currentDate.getDate() + 1);
    break;
  case 'week':
    futureDate.setDate(currentDate.getDate() + 7);
    break;
  case 'month':
    futureDate.setMonth(currentDate.getMonth() + 1);
    break;
  case 'year':
    futureDate.setFullYear(currentDate.getFullYear() + 1);
    break;
  default:
    // Handle invalid duration
    console.error('Invalid duration selected.');
    return;
}

// Format the future date
const formattedFutureDate = `${futureDate.getFullYear()}-${String(
  futureDate.getMonth() + 1
).padStart(2, '0')}-${String(futureDate.getDate()).padStart(2, '0')}`;
console.log('Future Date:', formattedFutureDate);
    // Proceed with sending the personal challenge
    // Access the value property of selectedPersonalChallenge
    if (!this.userID) {
      console.error('Id is empty');
      return;
    }
    try {
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/create_personal_challenge`;
      const response = await axios.post(url, {
        name:this.challengeTitle,
        description:this.challengeDescription,
        eco_points:this.ecoPoints,
        start_date: formattedCurrentDate,
        end_date: formattedFutureDate
      });

      if (response.status === 201) {
        console.log(response.data);
        this.content = response.data; // Make sure to define this.content in your data() function if you want to use it here
        console.log(this.content);
      } else {
        console.error('Challenge not sent.');
      }
    } catch (error) {
      console.error('Error sending challenge:', error);
    }
  } else {
    // If any field is empty, log an error message
    console.error('Please fill in all fields.');
  }
},
    async sendCommunityChallenge() {
      // Check if a challenge is selected
      if (this.selectedCommunityChallenge && this.selectedCommunityChallenge.value) {
        // Access the value property of selectedCommunityChallenge
        const selectedCommunityChallengeValue = this.selectedCommunityChallenge.value;
        console.log(`Sending community challenge "${selectedCommunityChallengeValue}"`);
        if (!this.userID) {
          console.error('Id is empty');
          return;
        }
        try {
          const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/create_community_challenge`;
          const response = await axios.post(url, {
            challenge_id: selectedCommunityChallengeValue, // Use the ID of the selected challenge
            created_by: this.userID
          });

          if (response.status === 200) {
            console.log(response.data);
            this.content = response.data; // Make sure to define this.content in your data() function if you want to use it here
            console.log(this.content);
          } else {
            console.error('Challenge not sent.');
          }
        } catch (error) {
          console.error('Error sending challenge:', error);
        }
      } else {
        console.error('No challenge selected.');
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
  /* Align the button to the center */
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

.input-group {
  display: flex;
  align-items: flex-start; /* Align items at the start of the flex container */
}

.left-dropdown {
  flex: 0 0 auto; /* Prevent this div from growing or shrinking */
  margin-right: 20px; /* Add some space between the label and the form */
}

.challenge-form {
  flex: 1; /* Allow this div to grow and take up remaining space */
}

.form-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 5px;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.header {
  font-size: 2.5em;
  text-align: center; /* Align the title to the left */
  margin-bottom: 20px; /* Add margin between header and content */
}

/* Styling for dropdown labels */
.dropdown-label {
  font-weight: bold;
  font-size: 1.2em;
}

.personal-label {
  color: #4CAF50;
}

.toggle-button {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.toggle-btn {
  padding: 10px 20px;
  margin: 0 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.toggle-btn.active {
  background-color: #4CAF50;
  color: white;
}

::placeholder {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px; /* Adjust font size as needed */
  /* Add any other desired placeholder styles */
}
</style>
