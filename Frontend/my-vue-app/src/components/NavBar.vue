<!-- NavBar.vue -->
<template>
  <nav>
    <ul>
      <li><router-link to="/" exact-active-class="active">Home</router-link></li>
      <li v-if="isLoggedIn"><router-link to="/calculator" active-class="active">Impact Calculator</router-link></li>
      <li v-if="isLoggedIn"><router-link to="/gamification" active-class="active">Challenge Center</router-link></li>
      <li v-if="!isLoggedIn"><router-link to="/login" active-class="active">Login</router-link></li>
      <li v-if="!isLoggedIn"><router-link to="/register" active-class="active">Register</router-link></li>
      <li v-if="isLoggedIn"><router-link to="/profile" active-class="active">Profile</router-link></li>
      <li v-if="isLoggedIn"><button @click="logout">Logout</button></li>
    </ul>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['currentUser']),
    isLoggedIn() {
      return !!this.currentUser;
    }
  },
  methods: {
    ...mapActions(['logoutUser']),
    logout() {
      this.logoutUser();
    }
  }
}
</script>

<style scoped>
nav {
  background-color: #4CAF50;
  padding: 10px;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

li {
  display: inline;
}

a {
  color: white;
  text-decoration: none;
  padding: 10px;
  display: inline-block;
}

.active {
  background-color: #1632bd;
  border-radius: 4px;
  padding: 10px;
}

button {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  font: inherit;
  padding: 10px;
}
</style>