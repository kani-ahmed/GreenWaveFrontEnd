<!-- NavBar.vue -->
<template>
  <!-- Navigation bar template -->
  <nav>
    <ul>
      <!-- Home link -->
      <li><router-link to="/" exact-active-class="active">Home</router-link></li>
      <!-- Impact Calculator link (visible if user is logged in) -->
      <li v-if="isLoggedIn"><router-link to="/calculator" active-class="active">Impact Calculator</router-link></li>
      <!-- Challenge Center link (visible if user is logged in) -->
      <li v-if="isLoggedIn"><router-link to="/gamification" active-class="active">Challenge Center</router-link></li>
      <!-- Social Media link (visible if user is logged in) -->
      <li v-if="isLoggedIn"><router-link to="/socialmedia" active-class="active">Social Media</router-link></li>
      <!-- Send Challenge link (visible if user is not logged in) -->
      <li v-if="isLoggedIn"><router-link to="/sendchallenge" active-class="active">Create Community Challenges</router-link></li>
      <!-- Login link (visible if user is not logged in) -->
      <li v-if="!isLoggedIn"><router-link to="/login" active-class="active">Login</router-link></li>
      <!-- Register link (visible if user is not logged in) -->
      <li v-if="!isLoggedIn"><router-link to="/register" active-class="active">Register</router-link></li>
      <!-- Profile link (visible if user is logged in) -->
      <li v-if="isLoggedIn"><router-link to="/profile" active-class="active">Profile</router-link></li>
      <!-- Logout button (visible if user is logged in) -->
      <li v-if="isLoggedIn"><button @click="logout">Logout</button></li>
    </ul>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'; 

export default {
  computed: {
    ...mapGetters(['currentUser']), // Map currentUser getter from Vuex store
    isLoggedIn() {
      return !!this.currentUser; // Check if user is logged in
    }
  },
  methods: {
    ...mapActions(['logoutUser']), // Map logoutUser action from Vuex store
    logout() {
      this.logoutUser(); // Call logoutUser action when logout button is clicked
    }
  }
}
</script>

<style scoped>
nav {
  background-color: #4CAF50; /* Background color for the navigation bar */
  padding: 10px; /* Padding around the navigation bar */
}

ul {
  list-style-type: none; /* Remove bullet points from the list */
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
  display: flex; /* Display list items horizontally */
  justify-content: space-around; /* Distribute items evenly along the main axis */
  align-items: center; /* Align items vertically in the center */
}

li {
  display: inline; /* Display list items inline */
}

a {
  color: white; /* Text color for links */
  text-decoration: none; /* Remove underline from links */
  padding: 10px; /* Padding around links */
  display: inline-block; /* Display links as block elements */
}

.active {
  background-color: #1632bd; /* Background color for active link */
  border-radius: 4px; /* Rounded corners for active link */
  padding: 10px; /* Padding around active link */
}

button {
  background: none; /* Transparent background for button */
  border: none; /* No border for button */
  color: white; /* Text color for button */
  cursor: pointer; /* Cursor style */
  font: inherit; /* Use parent font */
  padding: 10px; /* Padding around button */
}
</style>