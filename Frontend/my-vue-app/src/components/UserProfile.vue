<template>
  <div class="user-profile">
    <h2>User Profile</h2>
    <p><strong>Username:</strong> {{ profile.username }}</p>
    <p><strong>Email:</strong> {{ profile.email }}</p>
    <p><strong>Eco Points:</strong> {{ profile.eco_points }}</p>
    <p><strong>Privacy Settings:</strong> {{ profile.preferences ? profile.preferences.privacy_settings : 'Not set' }}</p>
    <p><strong>Receive Notifications:</strong> {{ profile.preferences ? profile.preferences.receive_notifications : 'Not set' }}</p>
    <img :src="profile.profile_picture" alt="Profile Picture" v-if="profile.profile_picture">
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
    userPrivacySettings() {
      return this.profile.preferences ? this.profile.preferences.privacy_settings : 'Default setting';
    },
    userNotificationsSetting() {
      return this.profile.preferences ? this.profile.preferences.receive_notifications : false;
    },
  },
  data() {
    return {
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
      toastMessage: '',
      showToast: false,
    };
  },
  methods: {
    fetchUserProfile() {
      if (!this.userID) {
        this.toastMessage = 'User not logged in.';
        this.showToast = true;
        return;
      }
      axios.get(`https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/view_profile/${this.userID}`)
          .then(response => {
            this.profile = {
              ...this.profile, // spread the default profile to preserve structure
              ...response.data,
              preferences: response.data.preferences || this.profile.preferences // safeguard against undefined preferences
            };
            console.log(this.profile);
          })
          .catch(error => {
            this.toastMessage = 'Error fetching user profile: ' + error.message;
            this.showToast = true;
            console.error('API error:', error);
          });
    }
  },
  created() {
    this.fetchUserProfile();
  }
}
</script>

<style scoped>
.user-profile {
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px auto;
  max-width: 800px;
  text-align: center;
}

img {
  max-width: 100px;
  border-radius: 50%;
  margin-top: 20px;
}

p {
  color: #333;
  line-height: 1.6;
}

.toast-component {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}
</style>
