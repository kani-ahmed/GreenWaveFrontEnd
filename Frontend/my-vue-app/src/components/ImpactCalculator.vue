<template>
  <div class="container">
    <div class="impact-calculator">
      <!-- Header section -->
      <header>
        <h1>Impact Calculator</h1>
      </header>

      <!-- Modal for displaying send challenges -->
      <div v-if="showSendChallengesModall=true" class="modal">
        <div class="modal-content">
          <h2>Choose A Challenge To Log</h2>
          <!-- Buttons for switching between personal and community challenges -->
          <div class="challenge-type-buttons">
            <button @click="filterChallenges('Personal')"
                    :class="{ active: selectedChallengeType === 'Personal' }">
              Personal Challenges
            </button>
            <button @click="filterChallenges('Community')"
                    :class="{ active: selectedChallengeType === 'Community' }">
              Community Challenges
            </button>
          </div>
          <!-- Search fields -->
          <div class="search-fields">
            <input v-model="challengeSearchQuery" placeholder="Search challenges...">
          </div>
          <!-- Table headers -->
          <table>
            <thead>
            <tr>
              <th>Challenge Name</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>
                <select v-model="selectedChallenge">
                  <option class="dropdown" v-for="challenge in filteredChallenges" :key="challenge.id"
                          :value="challenge">
                    {{ challenge.name }}
                  </option>
                </select>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="modal-content">
        <!-- Image Actions section -->
        <div class="image-actions">
          <!-- Image Action for logging water intake -->
          <div class="image-action">
            <div class="action-label">Log Water Intake</div>
            <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="addBottle($refs.bottlePicker.value)"/>
            <!-- Dropdown to select bottle type -->
            <select ref="bottlePicker" name="bottle" class="child bottle" id="bottlepicker">
              <!-- Bottle options -->
              <option value="pick">Pick a bottle!</option>
              <!-- Options for different types of bottles -->
              <option value="dp8">Disposable Plastic 8oz</option>
              <option value="dp12">Disposable Plastic 12oz</option>
              <option value="dp16.9">Disposable Plastic 16.9oz</option>
              <option value="rp17">Reusable Plastic 17 oz</option>
              <option value="rp25">Reusable Plastic 25 oz</option>
              <option value="rm12">Reusable Metal 12 oz</option>
              <option value="rm17">Reusable Metal 17 oz</option>
              <option value="rm25">Reusable Metal 25 oz</option>
            </select>
          </div>

          <!-- Image Action for viewing total impact -->
          <div class="image-action">
            <div class="action-label">View Total Impact</div>
            <img src="@/assets/leaf.png" alt="Leaf Image" @click="displayImpactScore()"/>
            <!-- Display impact score when available -->
            <div v-if="showImpactScore" class="results">
              <div id="scoreDisplay" class="display">{{ impactScore }}</div>
            </div>
          </div>

          <!-- Image Action for viewing total savings -->
          <div class="image-action">
            <div class="action-label">View Total Savings</div>
            <img src="@/assets/saving.png" alt="Saving Image" @click="displaySavings()"/>
            <!-- Display savings amount when available -->
            <div v-if="showSavings" class="results">
              <div id="savingsDisplay" class="display">{{ savingsAmount }}</div>
            </div>
          </div>
        </div>
      </div>
      <toast-component ref="toast" :message="toastMessage"/>
      <div v-if="loading" class="loading-overlay">
        Loading...
      </div>
    </div>
  </div>
</template>


<script>
// Import necessary dependencies
import axios from 'axios';
import {mapGetters} from 'vuex';
import ToastComponent from './ToastComponent.vue';

// Export the Vue component
export default {
  name: 'ImpactCalculator', // Component name
  components: {
    ToastComponent, // Register the ToastComponent
  },
  computed: {
    ...mapGetters(['currentUser']), // Map getters from Vuex store
    // Computed property to get user ID
    userID() {
      return this.currentUser ? this.currentUser.userId : null;
    },
    filteredChallenges() {
      return this.userChallengeStatuses.filter(challenge =>
          challenge.type === this.selectedChallengeType &&
          challenge.name.toLowerCase().includes(this.challengeSearchQuery.toLowerCase())
      );
    },
  },
  created() {
    this.fetchUserChallengeStatuses();
  },
  data() {
    // Initial data for the component
    return {
      loading: false, // Loading state
      bottleCounts: { // Object to store counts of different bottle types
        'dp8': 0,
        'dp12': 0,
        'dp16.9': 0,
        'rp17': 0,
        'rp25': 0,
        'rm12': 0,
        'rm17': 0,
        'rm25': 0
      },
      bottleTypeMap: { // Mapping of bottle types
        'dp8': 'single-use',
        'dp12': 'single-use',
        'dp16.9': 'single-use',
        'rp17': 'refillable',
        'rp25': 'refillable',
        'rm12': 'refillable',
        'rm17': 'refillable',
        'rm25': 'refillable'
      },
      savingsClickCount: 0, // Count of savings clicks
      impactScore: '', // Total impact score
      savingsAmount: '', // Total savings amount
      showImpactScore: false, // Flag to show impact score
      showSavings: false, // Flag to show savings amount
      bottleType: '', // Current selected bottle type
      lastAddedBottleType: '', // Last added bottle type
      impactDetails: {}, // Details of the impact
      toastMessage: '', // Message for toast component

      selectedChallengeType: 'personal',
      sendChallenges: [],
      challengeSearchQuery: '',
      showSendChallengesModall: false,
      selectedChallenge: null,
      userChallengeStatuses: [],
    };
  },
  methods: {
    // Method to navigate to a page
    navigateTo(page) {
      this.$router.push({name: page});
    },
    // Method to add a bottle
    addBottle(bottleType) {
      // Check if user is logged in
      if (!this.userID) {
        this.toastMessage = "Please log in to log water usage.";
        this.$refs.toast.showToast(3000, 'error', this.toastMessage);
        return;
      }
      // Add bottle to counts
      if (bottleType !== "pick") {
        this.bottleCounts[bottleType]++;
        this.lastAddedBottleType = bottleType;  // store the actual bottle type code
        this.bottleType = this.bottleTypeMap[bottleType]; // Map the bottle type for API call
        console.log(`${this.bottleCounts[bottleType]} ${bottleType} added.`);
        console.log("Current Bottle Counts:", this.bottleCounts);
        console.log("Mapped Bottle Type for API:", this.bottleType);

        // Log water usage
        this.logWaterUsage();
      }
    },

    // this mount function will make the API call to get the data
    mounted() {
      if (!this.userID) {
        console.warn("User is not logged in.");
      }
      this.getImpactDetails();
    },

    // Method to log water usage
    async logWaterUsage() {
      this.loading = true;
      try {
        const response = await axios.post('https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/log_water_usage', {
          user_id: this.userID,
          bottle_type: this.bottleType,
          count: this.bottleCounts[this.lastAddedBottleType],
          challenge_type: this.selectedChallenge ? this.selectedChallenge.type.toLowerCase() : null,
          challenge_id: this.selectedChallenge ? this.selectedChallenge.challenge_id : null,
        });
        console.log(`Logged ${this.bottleCounts[this.lastAddedBottleType]} ${this.bottleType} bottles.`);
        console.log(response.data);

        // Reset count after logging
        this.bottleCounts[this.lastAddedBottleType] = 0;

        // Show success message
        this.toastMessage = 'Water usage logged successfully!';
        this.$refs.toast.showToast(3000, 'success', this.toastMessage);

      } catch (error) {
        console.error("Error during logWaterUsage:", error);

        // Show error message
        this.toastMessage = 'Failed to log water usage.';
        this.$refs.toast.showToast(3000, 'error', this.toastMessage);
      } finally {
        this.loading = false;
      }
    },

    // Method to display impact score
    displayImpactScore() {
      this.getImpactDetails().then(() => {
        if (this.impactDetails && this.impactDetails.impact_score !== undefined) {
          this.impactScore = this.impactDetails.impact_score;
          this.showImpactScore = true;
        } else {
          console.error('Impact score is not available.');
          this.showImpactScore = false; // Ensure the UI reflects that data isn't available
        }
      }).catch(error => {
        console.error('Error while fetching and displaying impact score:', error);
      });
    },

    // Method to display savings amount
    displaySavings() {
      this.getImpactDetails().then(() => {
        if (this.impactDetails && this.impactDetails.money_saved !== undefined) {
          this.savingsAmount = `$${this.impactDetails.money_saved}`;
          this.showSavings = true;
        } else {
          console.error('Savings amount is not available.');
          this.showSavings = false; // Ensure the UI reflects that data isn't available
        }
      }).catch(error => {
        console.error('Error while fetching and displaying savings:', error);
      });
    },

    // Method to fetch impact details
    async getImpactDetails() {
      if (!this.userID) {
        console.error('No user ID available to fetch impact details.');
        return Promise.reject('No user ID provided');
      }

      try {
        const response = await axios.get(`https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_impact/${this.userID}`);
        if (response.data && Array.isArray(response.data) && response.data.length > 0) {
          this.impactDetails = response.data[0];
          console.log('Impact Details:', this.impactDetails);
          return Promise.resolve();
        } else {
          console.error('Unexpected response format:', response.data);
          return Promise.reject('Invalid response format');
        }
      } catch (error) {
        console.error('Error fetching impact details:', error);
        return Promise.reject(error);
      }
    },
    // Method to filter challenges based on the selected challenge type
    filterChallenges(challengeType) {
      this.selectedChallengeType = challengeType;
    },

    fetchUserChallengeStatuses() {
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/user_challenge_status/${this.userID}`;
      axios.get(url)
          .then(response => {
            if (response.status === 200) {
              this.userChallengeStatuses = response.data;
            } else {
              console.error('User challenge statuses not found.');
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },
  }
}
</script>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

/* Main layout and typography */
.impact-calculator {
  width: 100%;
  max-width: 800px;
  margin-bottom: 2rem;
  font-family: 'Roboto', sans-serif;
  color: #333;
  /* Background color and styling for the calculator */
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  background: #e4fcec; /* New green background color */
}

/* Header styles */
header {
  background: linear-gradient(to right, #4CAF50, #8BC34A);
  /* Gradient background for the header */
  color: white;
  padding: 1rem 0;
  border-radius: 8px 8px 0 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  z-index: 1; /* Higher stacking order than other elements */
  position: relative; /* Positioning for potential logo placement */
}

h1 {
  margin: 0;
  font-size: 2.5rem; /* Larger font size for the title */
}

/* Adding a textured or patterned background to the top part with the logo */
header::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('@/assets/background.png'); /* Path to your background texture or pattern */
  opacity: 0.2; /* Adjust opacity for readability*/
  border-radius: 8px 8px 0 0;
}

/* Styles for Image Actions */
.image-actions {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap; /* Wrap items on smaller screens */
  gap: 1rem; /* Spacing between action items */
  padding: 1rem; /* Padding within the actions container */
  background: white; /* White background for the action area */
  border-radius: 8px; /* Rounded corners for the action area */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow for depth */
  z-index: 2; /* Higher stacking order than the header */
  position: relative; /* Positioning for z-index */
}

/* Styles for individual image actions */
.image-action {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
  width: 200px;
}

.action-label {
  font-size: 16px;
  font-weight: bold;
  color: #4CAF50; /* Color for the action label */
  text-align: center;
  margin-bottom: 5px; /* Spacing between label and image */
}

/* Styles for action images */
.image-action img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  cursor: pointer;
  margin-bottom: 10px;
  transition: transform 0.1s, box-shadow 0.1s; /* Transition effects */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for depth */
}

/* Button-like styles for images */
.image-action img:active {
  transform: scale(0.97); /* Slightly smaller scale for a subtle click effect */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Shadow for the pressed state */
}

/* Styles for action buttons */
.image-action button {
  padding: 8px 12px;
  border: none; /* Remove border for a cleaner look */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s, transform 0.1s, box-shadow 0.1s; /* Transition effects */
  background-image: linear-gradient(to top, #f5f5f5, #ffffff); /* Gradient effect */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for depth */
}

/* Button clicking effect */
.image-action button:active {
  background-image: linear-gradient(to top, #e6e6e6, #f5f5f5); /* Darker gradient for the pressed state */
  transform: translateY(2px); /* Moves the button down to simulate a press */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Smaller shadow for the pressed state */
}

/* Styles for dropdown select */
.image-action select {
  padding: 10px 15px; /* Slightly larger padding for a touch-friendly interface */
  border: 2px solid #ccc; /* Solid border that matches the theme */
  border-radius: 5px; /* Rounded corners */
  background-color: white; /* Background color */
  font-size: 16px; /* Larger font size for better readability */
  cursor: pointer;
  width: 100%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Shadow for depth */
  appearance: none; /* Remove default styling */
  background-image: linear-gradient(45deg, transparent 50%, green 50%),
  linear-gradient(135deg, green 50%, transparent 50%),
  linear-gradient(to right, #fff, #fff); /* Custom arrow */
  background-position: calc(100% - 20px) calc(1em + 2px),
  calc(100% - 15px) calc(1em + 2px),
  100% 0; /* Arrow position */
  background-size: 5px 5px,
  5px 5px,
  2.5em 2.5em; /* Arrow size */
  background-repeat: no-repeat;
  transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Transition effects */
}

/* Hover styles for select */
.image-action select:hover {
  border-color: #a5a5a5; /* Darken border on hover */
}

/* Focus styles for select */
.image-action select:focus {
  border-color: #88c057; /* Green border color for focus */
  box-shadow: 0 0 8px rgba(136, 192, 87, 0.8); /* Glowing effect to match focus */
  outline: none; /* Remove the default focus outline */
}

/* Loading overlay styles */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  color: white; /* Text color */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5em; /* Font size */
}


/* Styles from Results.vue */
.results {
  width: 100%;
  max-width: 800px;
  text-align: center; /* Center-align text */
  margin-top: 40px; /* Top margin */
  font-family: 'Roboto', sans-serif; /* Font family */
}

/* Styles for display elements */
.display {
  font-size: 24px; /* Font size */
  font-weight: bold; /* Bold font weight */
  color: white; /* Text color */
  background-color: #3a3a3c; /* Background color */
  padding: 12px 20px; /* Padding */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for depth */
  margin: 10px 0; /* Margin */
  display: inline-block; /* Display as inline-block */
  animation: fadeInUp 0.5s ease-out; /* Fade-in animation */
}

#scoreDisplay {
  background-color: #4CAF50; /* Green for impact score */
}

#savingsDisplay {
  background-color: #2196F3; /* Blue for savings amount */
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 95%;
  margin: 10px;
}

.challenge-type-buttons {
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
  width: 100%;
}

.challenge-type-buttons button {
  margin-right: 10px;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #eee;
  cursor: pointer;
  font-size: 18px;
}

.challenge-type-buttons button.active {
  background-color: #4caf50;
  color: white;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  padding: 5px 10px;
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}

.dropdown-menu {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 120px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown:hover .dropdown-menu {
  display: block;
}

.dropdown-item {
  padding: 8px 16px;
  text-decoration: none;
  display: block;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f1f1f1;
}

.search-fields {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.search-fields input {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  outline: none;
  transition: all 0.3s ease;
}

.search-fields input:focus {
  border-color: #4CAF50;
  box-shadow: 0 0 8px rgba(76, 175, 80, 0.5);
}


.send-challenges-button {
  padding: 8px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  background-color: #2196F3;
  color: white;
}

.send-challenges-button:hover {
  background-color: #950bda;
}

select {
  width: 100%;
  padding: 8px 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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

/* Header row styles */
th {
  background-color: #4CAF50;
  color: white;
}

td:first-child {
  width: 70%;
}

/* Styles for the button cell */
td:last-child {
  width: 30%;
  text-align: right;
}

/* Fade-in animation keyframes */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
