<template>
<div class="Gamification">
  
  
  <!-- Dashboard Navigation Bar -->
  <div class="dashboard-nav">
    <button @click="navigateTo('ImpactCalculator')">Back to Calculator</button>
    <!-- Additional buttons can be added here if needed -->
  </div>

    <header>
      <h1>Challenge Center</h1>
    </header>

    <main>
      <div class="button-container">
        <div class="button-group left">
          <button class="square-button">Challenge Inbox</button>
          <button class="square-button" @click="fetchPersonalChallenges">Challenges in Progress</button>
          <button class="square-button">Send Challenges</button>
        </div>
        <div class="button-group right">
          <button class="square-button">User Profile</button>
          <button class="square-button" @click="fetchUserBadges">Badges</button>
          <button class="square-button" @click="toggleEcoPoints">{{ ecoPointsText }}</button>
        </div>
      </div>
    </main>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showModal = false">&times;</span>
        <h2>Challenges in Progress</h2>
        <table>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Status</th>
          </tr>
          <tr v-for="challenge in challenges" :key="challenge.challenge_id">
            <td>{{ challenge.name }}</td>
            <td>{{ challenge.description }}</td>
            <td>{{ challenge.status }}</td>
          </tr>
        </table>
      </div>
    </div>

    <div v-if="showBadgesModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showBadgesModal = false">&times;</span>
        <h2 class="modal-title">Your Badges</h2>
        <div class="badges-container">
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
import { mapGetters } from 'vuex';
import axios from 'axios';



export default {
  name: 'ChallengeCenter',
  computed: {
    ...mapGetters(['currentUser']),
  },
  data() {
    return {
      ecoPoints: 0, // Initial value of eco points
      ecoPointsText: 'Eco-points', // Initial text of the button
      challenges: [],  // Store challenges here
      showModal: false,  // Control modal visibility
      badges: [],  // Store badges here
      showBadgesModal: false  // Control badges modal visibility
    };
  },
  methods: {
    navigateTo(routeName) {
      this.$router.push({ name: routeName });
    },
    toggleEcoPoints() {
      if (this.ecoPointsText === 'Eco-points') {
        // Update eco points value (for demonstration, you can update it dynamically in your actual app)
        this.ecoPoints = 0; // Change this value to the desired eco points
        this.ecoPointsText = `You have ${this.ecoPoints} eco points`;
      } else {
        this.ecoPointsText = 'Eco-points';
      }
      // esteban commits for api requests and handling the data
    },

    fetchPersonalChallenges() {
      console.log('Fetching personal challenges...');
      if (!this.currentUser || !this.currentUser.userId) {
        console.error('User ID is not available.');
        return;
      }

      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_personal_challenges/${this.currentUser.userId}`;
      console.log(this.currentUser.userId)

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

      fetchUserBadges() {
        // Replace with your actual API call to fetch badges
        const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_badges/${this.currentUser.userId}`;

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
      
      getBadgeImagePath(badgeName) {
        // Requires the image from the assets folder so webpack can process it
        return require(`@/assets/Badges/${badgeName}.png`);
      },




  }
}
</script>


<style scoped>
.Gamification {
  font-family: 'Roboto', sans-serif; /* Consistency in typography */
  color: #333; /* Darker text for better readability */
  background: #e4fcec; /* Consistent green background across the app */
  padding: 2rem;
  border-radius: 10px; /* Rounded corners for the outer container */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  max-width: 800px; /* Limiting max width for better layout control */
  margin: 2rem auto; /* Centering the main container */
}


.dashboard-nav {
  background-color: #4CAF50; /* Consistent green color */
  padding: 10px;
  text-align: center;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.dashboard-nav button {
  background-color: #8BC34A;
  color: white;
  border: none;
  padding: 8px 16px;
  margin: 0 5px;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s, transform 0.1s;
}

.dashboard-nav button:hover {
  background-color: #7CB342;
  transform: translateY(-2px);
}

header {
  background: linear-gradient(to right, #4CAF50, #8BC34A); /* Green gradient header */
  color: white;
  padding: 1rem 0;
  border-radius: 8px 8px 0 0; /* Rounded top corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for header */
  text-align: center;
  font-size: 2.5rem; /* Prominent header size */
}

main {
  padding: 20px;
  display: flex;
  flex-direction: column; /* Ensures vertical layout of content */
  align-items: center; /* Center aligns the child elements */
}

.button-container {
  display: flex;
  justify-content: space-around; /* Evenly spaces the button groups */
  flex-wrap: wrap; /* Allows button groups to wrap on smaller screens */
  width: 100%; /* Full width to utilize space */
}

.button-group {
  display: flex;
  flex-direction: column;
  align-items: center; /* Centering buttons in their groups */
  padding: 10px;
}

.square-button {
  width: 150px; /* Smaller width for better fit */
  height: 150px; /* Maintaining square shape */
  margin: 10px;
  border: none;
  background-color: #8BC34A; /* Lighter green for buttons */
  cursor: pointer;
  border-radius: 10px; /* Rounded corners for buttons */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Consistent shadow styling */
  transition: background-color 0.3s, transform 0.1s; /* Smooth transition for interactive feedback */
}

.square-button:hover {
  background-color: #7CB342; /* Slightly darker green on hover */
  transform: translateY(-2px); /* Subtle lift effect on hover */
}

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

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
}

.close {
  float: right;
  font-size: 28px;
  cursor: pointer;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #4CAF50;
  color: white;
}

.badges-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 1rem;
}

.badge-image {
  max-width: 250px; /* Increase the size as needed */
  margin: 1rem; /* Adjust spacing around images */
  border: 3px solid #4CAF50; /* Optional border */
  border-radius: 50%; /* Circular badges */
  /* If you want the images to be responsive to the size of the container, you can also use width in percentage, like width: 25%; */
}



</style>
