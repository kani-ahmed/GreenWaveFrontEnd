<template>
  <div class="Homepage">
    <header>
      <h1>Green Wave</h1>
    </header>

    <div class="login-form">
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit" :disabled="isAuthLoading">Login</button>
        <div v-if="isAuthLoading">Logging in...</div>
        <div v-if="loginErrorMessage">{{ loginErrorMessage }}</div>
      </form>
    </div>
    <button @click="goToRegister">Register</button>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  computed: {
    ...mapState({
      isAuthLoading: state => state.isLoading,
      loginErrorMessage: state => state.loginError
    })
  },
  methods: {
    ...mapActions(['loginUser']),

    login() {
      this.loginUser({
        username: this.username,
        password: this.password
      }).catch(error => {
        console.error('Login error:', error.message);
      });
    },

    goToRegister() {
      this.$router.push('/register');
    }
  }
}
</script>



<style scoped>
  header {
    position: relative;
    text-align: center;
    padding: 20px;
    background-color: #4CAF50; /* Primary green background */
    color: white;
    margin: 0;
  }

  header::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('@/assets/background.png'); /* Verify this path */
    opacity: 0.2; 
    border-radius: 8px 8px 0 0; /* Match the border-radius of your header if any */
  }

  .Homepage {
    font-family: 'Roboto', sans-serif;
    color: #333;
    background: #e4fcec; /* Light green background for the whole page */
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    max-width: 800px;
    margin: 2rem auto;
  }

  .login-form {
    background: white;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
    margin: 50px auto;
    width: 300px;
  }

  .form-group {
    margin-bottom: 15px;
  }

  .form-group label {
    display: block;
  }

  .form-group input {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
  }

  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }

  button:hover {
    opacity: 0.8;
  }
</style>
