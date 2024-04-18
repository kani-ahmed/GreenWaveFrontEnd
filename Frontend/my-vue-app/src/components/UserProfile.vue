<template>
  <!-- User profile component template -->
  <div class="user-profile">
    <h2>User Profile</h2>
    <!-- Display user information -->
    <p><strong>Username:</strong> {{ profile.username }}</p>
    <p><strong>Email:</strong> {{ profile.email }}</p>
    <p><strong>Eco Points:</strong> {{ profile.eco_points }}</p>
    <!-- Check if privacy settings and notifications are set, otherwise display default message -->
    <p><strong>Privacy Settings:</strong> {{ profile.preferences ? profile.preferences.privacy_settings : 'Not set' }}</p>
    <p><strong>Receive Notifications:</strong> {{ profile.preferences ? profile.preferences.receive_notifications : 'Not set' }}</p>
    <!-- Display profile picture if available -->
    <img :src="profile.profile_picture" alt="Profile Picture" v-if="profile.profile_picture">
    <!-- Toast component for displaying messages -->
    <toast-component v-if="showToast" :message="toastMessage" />
  </div>
</template>


<script>
import axios from 'axios';
import {mapGetters} from 'vuex';
import ToastComponent from './ToastComponent.vue';

export default {
  name: 'UserProfile',
  components: {
    ToastComponent,
  },
  computed: {
    ...mapGetters(['currentUser']),
    // Use a computed property to react to changes in currentUser
    userID() {
      return this.currentUser ? this.currentUser.userId : null;
    },
    // Computed property to access user privacy settings or display default if not set
    userPrivacySettings() {
      return this.profile.preferences ? this.profile.preferences.privacy_settings : 'Default setting';
    },
    // Computed property to access user notifications setting or display default if not set
    userNotificationsSetting() {
      return this.profile.preferences ? this.profile.preferences.receive_notifications : false;
    },
  },
  data() {
    return {
      // Initialize profile data and toast properties
      profile: {
        username: '',
        email: '',
        eco_points: 0,
        preferences: {
          privacy_settings: '',
          receive_notifications: false,
        },
        profile_picture: '',
      },
      toastMessage: '', // Toast message to display
      showToast: false, // Flag to control toast visibility
    };
  },
  methods: {
    // Method to fetch user profile data
    fetchUserProfile() {
      // Display toast message if user is not logged in
      if (!this.userID) {
        this.toastMessage = 'User not logged in.';
        this.showToast = true;
        return;
      }
      // Fetch user profile data from backend API
      axios.get(`https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/view_profile/${this.userID}`)
          .then(response => {
            // Update profile data with fetched data
            this.profile = {
              ...this.profile, // spread the default profile to preserve structure
              ...response.data,
              preferences: response.data.preferences || this.profile.preferences // safeguard against undefined preferences
            };
            console.log(this.profile);
          })
          .catch(error => {
            // Display error message if there's an error fetching user profile
            this.toastMessage = 'Error fetching user profile: ' + error.message;
            this.showToast = true;
            console.error('API error:', error);
          });
    }
  },
  created() {
    // Call method to fetch user profile data when component is created
    this.fetchUserProfile();
  }
}
</script>

<style scoped>
.user-profile {
  padding: 20px; /* Padding around user profile */
  background-color: #f4f4f4; /* Background color */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow effect */
  margin: 20px auto; /* Center horizontally with margin */
  max-width: 800px; /* Set the maximum width of the user profile */
  text-align: center; /* Align text content in the user profile to the center */
}

img {
  max-width: 100px; /* Limit the maximum width of images to 100 pixels */
  border-radius: 50%; /* Apply a circular border radius to images */
  margin-top: 20px; /* Add top margin to images for spacing */
}

p {
  color: #333; /* Set the color of paragraph text */
  line-height: 1.6; /* Set the line height of paragraphs for better readability */
}

.toast-component {
  position: fixed; /* Set the position of the toast component as fixed */
  bottom: 20px; /* Position the toast component 20 pixels from the bottom of the viewport */
  right: 20px; /* Position the toast component 20 pixels from the right of the viewport */
  z-index: 1000; /* Set the z-index of the toast component to ensure it appears above other content */
}
</style>
