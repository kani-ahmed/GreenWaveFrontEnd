<template>
  <div class="impact-calculator">
    <!-- Header -->
    <header>
      <h1>Impact Calculator</h1>
    </header>

    <!-- Image Actions -->
    <div class="image-actions">

      <div class="image-action">
        <div class="action-label">Log Water Intake</div>
        <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="addBottle($refs.bottlePicker.value)" />
        <select ref="bottlePicker" name="bottle" class="child bottle" id="bottlepicker">
          <!-- Bottle options -->
          <option value="pick">Pick a bottle!</option>
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

      <div class="image-action">
        <div class="action-label">View Total Impact</div>
        <img src="@/assets/leaf.png" alt="Leaf Image" @click="displayImpactScore()" />
        <!-- Removed the regular "Generate Score" button -->
        <div v-if="showImpactScore" class="results">
          <div id="scoreDisplay" class="display">{{ impactScore }}</div>
        </div>
      </div>

      <div class="image-action">
        <div class="action-label">View Total Savings</div>
        <img src="@/assets/saving.png" alt="Saving Image" @click="displaySavings()" />
        <!-- Removed the regular "Click To Get Your Savings!" button -->
        <div v-if="showSavings" class="results">
          <div id="savingsDisplay" class="display">{{ savingsAmount }}</div>
        </div>
      </div>
    </div>
  </div>
  <toast-component ref="toast" :message="toastMessage" />
  <div v-if="loading" class="loading-overlay">
    Loading...
  </div>
</template>


<script>

import axios from 'axios';
import { mapGetters } from 'vuex';
import ToastComponent from './ToastComponent.vue';

export default {
  name: 'ImpactCalculator',
  components: {
    ToastComponent,
  },
  computed: {
    ...mapGetters(['currentUser']),
    // Use a computed property to react to changes in currentUser
    userID() {
      return this.currentUser ? this.currentUser.userId : null;
    }
  },
  data() {
    return {
      loading: false,
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
      bottleTypeMap: {
        'dp8': 'single-use',
        'dp12': 'single-use',
        'dp16.9': 'single-use',
        'rp17': 'refillable',
        'rp25': 'refillable',
        'rm12': 'refillable',
        'rm17': 'refillable',
        'rm25': 'refillable'
      },
      savingsClickCount: 0,
      impactScore: '',
      savingsAmount: '',
      showImpactScore: false,
      showSavings: false,
      bottleType: '',
      lastAddedBottleType: '',
      impactDetails: {},
      toastMessage: '',
    };
  },
  methods: {

    navigateTo(page) {
      this.$router.push({ name: page });
    },

    addBottle(bottleType) {
      if (!this.userID) {
        this.toastMessage = "Please log in to log water usage.";
        this.$refs.toast.showToast(3000, 'error', this.toastMessage);
        return;
      }
      if (bottleType !== "pick") {
        this.bottleCounts[bottleType]++;
        this.lastAddedBottleType = bottleType;  // store the actual bottle type code
        this.bottleType = this.bottleTypeMap[bottleType]; // Map the bottle type for API call
        console.log(`${this.bottleCounts[bottleType]} ${bottleType} added.`);
        console.log("Current Bottle Counts:", this.bottleCounts);
        console.log("Mapped Bottle Type for API:", this.bottleType);

        // Call logWaterUsage to send data to the backend
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

    // this function will make the API call to get the data
    async logWaterUsage() {
      this.loading = true;
      try {
        const response = await axios.post('https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/log_water_usage', {
          user_id: this.userID,
          bottle_type: this.bottleType,
          count: this.bottleCounts[this.lastAddedBottleType]
        });
        console.log(`Logged ${this.bottleCounts[this.lastAddedBottleType]} ${this.bottleType} bottles.`);
        console.log(response.data);

        // Reset the count for this bottle type after logging
        this.bottleCounts[this.lastAddedBottleType] = 0;

        // Set a success message and specify the type as 'success'
        this.toastMessage = 'Water usage logged successfully!';
        this.$refs.toast.showToast(3000, 'success', this.toastMessage);

      } catch (error) {
        console.error("Error during logWaterUsage:", error);

        // Set an error message and specify the type as 'error'
        this.toastMessage = 'Failed to log water usage.';
        this.$refs.toast.showToast(3000, 'error', this.toastMessage);
      } finally {
        this.loading = false;
      }
    },

    // Methods to fetch and display data when clicked
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

// Updated getImpactDetails method to return a Promise
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
  }
}
</script>

<style scoped>

/* Main layout and typography */
.impact-calculator {
  font-family: 'Roboto', sans-serif;
  color: #333;
  /*background: #f0f0f0; /* Subtle background color for the whole calculator */
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 2rem auto;
  background: #e4fcec;
  /* New green color for the impact calculator background */
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
  z-index: 1;
  /* Assuming this is lower than the image-actions */
  position: relative;
  /* For positioning the logo if needed */
}

h1 {
  margin: 0;
  font-size: 2.5rem;
  /* Larger font size for the title */
}

/* Adding a textured or patterned background to the top part with the logo */
header::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('@/assets/background.png');
  /* Path to your background texture or pattern */
  opacity: 0.2;
  /* Adjust the opacity to not overpower the header text */
  border-radius: 8px 8px 0 0;
}

/* Styles for Image Actions */
.image-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  /* Wrap items on smaller screens */
  gap: 1rem;
  /* Spacing between action items */
  padding: 1rem;
  /* Padding within the actions container */
  background: white;
  /* White background for the action area */
  border-radius: 8px;
  /* Rounded corners for the action area */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* Shadow for depth */
  margin-top: -1rem;
  /* Pull the action area up to overlap with the header */
  z-index: 2;
  /* Higher than the header */
  position: relative;
  /* z-index only works on positioned elements */
}


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
  color: #4CAF50; /* You can adjust the color to fit your design */
  text-align: center;
  margin-bottom: 5px; /* Spacing between the label and the image */
}



.image-action img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  cursor: pointer;
  margin-bottom: 10px;
  transition: transform 0.1s, box-shadow 0.1s;
  /* Add box-shadow to the transition */
  border-radius: 10px;
  /* Optional: if you want rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  /* Soft shadow for depth */
}

/* Button-like styles for images */
.image-action img:active {
  transform: scale(0.97);
  /* Slightly smaller scale for a subtle click effect */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  /* Smaller shadow for the pressed state */
}


.image-action button {
  margin-top: 10px;
  padding: 8px 12px;
  border: none;
  /* Remove border for a cleaner look */
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s, transform 0.1s, box-shadow 0.1s;
  /* Add box-shadow to the transition */
  background-image: linear-gradient(to top, #f5f5f5, #ffffff);
  /* Subtle gradient effect */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  /* Soft shadow for depth */
}

/* Button clicking effect */
.image-action button:active {
  background-image: linear-gradient(to top, #e6e6e6, #f5f5f5);
  /* Darker gradient for the pressed state */
  transform: translateY(2px);
  /* Moves the button down to simulate a press */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  /* Smaller shadow for the pressed state */
}

.image-action select {
  padding: 10px 15px;
  /* Slightly larger padding for a touch-friendly interface */
  border: 2px solid #ccc;
  /* Solid border that matches the theme */
  border-radius: 5px;
  /* Rounded corners */
  background-color: white;
  /* Background color */
  font-size: 16px;
  /* Larger font size for better readability */
  cursor: pointer;
  width: 100%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Subtle shadow for depth */
  appearance: none;
  /* Remove default styling */
  background-image:
    linear-gradient(45deg, transparent 50%, green 50%),
    linear-gradient(135deg, green 50%, transparent 50%),
    linear-gradient(to right, #fff, #fff);
  /* Custom arrow */
  background-position:
    calc(100% - 20px) calc(1em + 2px),
    calc(100% - 15px) calc(1em + 2px),
    100% 0;
  /* Arrow position */
  background-size:
    5px 5px,
    5px 5px,
    2.5em 2.5em;
  /* Arrow size */
  background-repeat: no-repeat;
  transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  /* Smooth transition for interactive states */
}

.image-action select:hover {
  border-color: #a5a5a5;
  /* Darken border on hover */
}

.image-action select:focus {
  border-color: #88c057;
  /* Green border color for focus */
  box-shadow: 0 0 8px rgba(136, 192, 87, 0.8);
  /* Glowing effect to match focus */
  outline: none;
  /* Remove the default focus outline */
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5em;
}


/* Styles from Results.vue */
.results {
  text-align: center;
  margin-top: 20px;
  font-family: 'Roboto', sans-serif;
}


.display {
  font-size: 24px;
  font-weight: bold;
  color: white;
  /* Default text color */
  background-color: #3a3a3c;
  /* Neutral dark background */
  padding: 12px 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  margin: 10px 0;
  display: inline-block;
  animation: fadeInUp 0.5s ease-out;
}

#scoreDisplay {
  background-color: #4CAF50;
  /* Green for impact score */
}

#savingsDisplay {
  background-color: #2196F3;
  /* Blue for savings amount */
}

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
