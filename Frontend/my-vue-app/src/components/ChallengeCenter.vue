<template>
  <!-- Container for the Gamification component -->
  <div class="Gamification">
    <!-- Header section -->
    <header>
      <h1>Challenge Center</h1>
    </header>

    <!-- Main content section -->
    <main>
      <!-- Button container for badges and challenges -->
      <div class="button-container">
        <!-- Button group for badges -->
        <div class="button-group top">
          <button class="square-button" @click="fetchUserBadges">Badges</button>
        </div>
        <!-- Button group for challenges -->
        <div class="button-group bottom">
          <button class="square-button" @click="fetchPersonalChallenges">Challenges in Progress</button>
          <button class="square-button" @click="toggleEcoPoints">{{ ecoPointsText }}</button>
        </div>
      </div>
    </main>

    <!-- Modal for displaying challenges in progress -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="showModal = false">&times;</span>
        <!-- Title for the modal -->
        <h2>Challenges in Progress</h2>
        <!-- Table to display challenges -->
        <table>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Status</th>
          </tr>
          <!-- Loop through challenges and display details -->
          <tr v-for="challenge in challenges" :key="challenge.challenge_id">
            <td>{{ challenge.name }}</td>
            <td>{{ challenge.description }}</td>
            <td>{{ challenge.status }}</td>
          </tr>
        </table>
      </div>
    </div>

    <!-- Modal for displaying user badges -->
    <div v-if="showBadgesModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="showBadgesModal = false">&times;</span>
        <!-- Title for the modal -->
        <h2 class="modal-title">Your Badges</h2>
        <!-- Container for displaying badges -->
        <div class="badges-container">
          <!-- Loop through badges and display images -->
          <img
              v-for="badge in badges"
              :key="badge.id"
              :src="getBadgeImagePath(badge)"
              :alt="badge.name"
              class="badge-image"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'; // Importing Vuex mapGetters
import axios from 'axios'; // Importing Axios for making HTTP requests



export default {
  name: 'ChallengeCenter', // Component name
  computed: {
    ...mapGetters(['currentUser']), // Mapping currentUser getter from Vuex store
    // Ensure userID is available for all methods
    userID() { // Computed property to get the userID
      return this.currentUser ? this.currentUser.userId : null; // If currentUser exists, return its userID, otherwise return null
    }
  },
  data() {
    return {
      ecoPoints: 0, // Initial eco points
      ecoPointsText: 'Eco-points', // Text displayed for eco points
      challenges: [], // Array to store challenges
      showModal: false, // Flag to control display of challenge modal
      badges: [], // Array to store user badges
      showBadgesModal: false // Flag to control display of badges modal
    };
  },
  methods: {
    navigateTo(routeName) { // Method to navigate to a specified route
      this.$router.push({ name: routeName }); // Pushing route to router with specified name
    },
    toggleEcoPoints() { // Method to toggle display of eco points
      if (!this.userID) { // If userID is not available
        alert("Please log in to access eco points."); // Show alert
        return;
      }
      if (this.ecoPointsText === 'Eco-points') { // If eco points are currently displayed
        // Fetch impact details and update eco points
        this.getImpactDetails().then(() => {
          // Assuming impact score is part of the impactDetails
          if (this.impactDetails && this.impactDetails.impact_score !== undefined) {
            this.ecoPoints = this.impactDetails.impact_score; // Update eco points
            this.ecoPointsText = `You have ${this.ecoPoints} eco points`; // Update display text
          } else {
            console.error("Impact score is not available.");
            this.ecoPointsText = 'No impact score available'; // Display error message
          }
        }).catch(error => {
          console.error('Failed to fetch impact details:', error);
          this.ecoPointsText = 'Failed to load eco points'; // Display error message
        });
      } else {
        this.ecoPointsText = 'Eco-points'; // Reset to default text when toggled again
      }
    },

    async getImpactDetails() { // Method to fetch impact details
      if (!this.userID) { // If userID is not available
        console.error('No user ID available to fetch impact details.');
        return Promise.reject('No user ID provided'); // Reject promise
      }

      try {
        const response = await axios.get(`https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_impact/${this.userID}`);
        if (response.data && Array.isArray(response.data) && response.data.length > 0) {
          this.impactDetails = response.data[0]; // Store impact details
          console.log('Impact Details:', this.impactDetails);
          return Promise.resolve(); // Resolve promise
        } else {
          console.error('Unexpected response format:', response.data);
          return Promise.reject('Invalid response format'); // Reject promise
        }
      } catch (error) {
        console.error('Error fetching impact details:', error);
        return Promise.reject(error); // Reject promise
      }
    },

    fetchPersonalChallenges() { // Method to fetch personal challenges
      if (!this.userID) { // If userID is not available
        console.error('User ID is not available.');
        return;
      }
      console.log('Fetching personal challenges...');

      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_personal_challenges/${this.userID}`;

      axios.get(url)
        .then(response => {
          if (response.status === 200) {
            console.log("Fetch successful!");
            this.challenges = response.data;  // Store fetched challenges
            this.showModal = true;  // Show the modal
          } else {
            console.error('Challenges not found.');
          }
        })
        .catch(error => {
          console.error("Error:", error.response);
        });
      },

      fetchUserBadges() { // Method to fetch user badges
        if (!this.userID) { // If userID is not available
          console.error('User ID is not available.');
          return;
        }
        // Replace with your actual API call to fetch badges
        const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_badges/${this.userID}`;

        axios.get(url)
          .then(response => {
            if (response.status === 200) {
              this.badges = response.data.badges;  // Store fetched badges
              this.showBadgesModal = true;  // Show the badges modal
            } else {
              console.error('Badges not found.');
            }
          })
          .catch(error => {
            console.error("Error:", error.response);
          });
      },

      getBadgeImagePath(badgeName) { // Method to get badge image path
        // Requires the image from the assets folder so webpack can process it
        return require(`@/assets/Badges/${badgeName}.png`); // Return the path to the badge image
      },
  }
}
</script>

<style scoped>
/* Scoped styles for Gamification component */
.Gamification {
  font-family: 'Roboto', sans-serif;
  color: #333;
  background: #e4fcec;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 2rem auto;
}

/* Header styles */
header {
  background: linear-gradient(to right, #4CAF50, #8BC34A);
  color: white;
  padding: 1rem 0;
  border-radius: 8px 8px 0 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  font-size: 1.5rem;
  position: relative;
}

/* Logout button styles */
.logout-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 15px;
  background: #FF6347;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  border: none;
}

/* Main content styles */
main {
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Button container styles */
.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

/* Button group styles */
.button-group {
  display: flex;
  justify-content: center;
  padding: 10px;
  margin-bottom: 20px;
}

/* Square button styles */
.square-button {
  width: 150px;
  height: 150px;
  margin: 10px;
  border: none;
  background-color: #8BC34A;
  cursor: pointer;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s, transform 0.1s;
}

/* Square button hover styles */
.square-button:hover {
  background-color: #7CB342;
  transform: translateY(-2px);
}

/* Modal styles */
.modal {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Modal content styles */
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
}

/* Close button styles */
.close {
  float: right;
  font-size: 28px;
  cursor: pointer;
}

/* Table styles */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

/* Header row styles */
th {
  background-color: #4CAF50;
  color: white;
}

/* Badges container styles */
.badges-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 0.1rem;
}

/* Badge image styles */
.badge-image {
  max-width: 250px;
  margin: 1rem;
  border: 3px solid #4CAF50;
  border-radius: 50%;
}
</style>
