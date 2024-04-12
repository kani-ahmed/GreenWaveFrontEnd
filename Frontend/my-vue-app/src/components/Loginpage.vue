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
        <button type="submit">Login</button>
      </form>
    </div>
  </div>

  <button @click="goToRegister">Register</button>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      const apiUrl = 'http://127.0.0.1:8000/login'; // Adjust according to your API
      const userData = {
        username: this.username,
        password: this.password
      };
      
      axios.post(apiUrl, userData)
        .then(response => {
          if (response.status === 200) {
            console.log("Login successful!");
            this.$router.push('/calculator');
          } else {
            console.error('Login failed:', response.data);
            alert('Login failed');
          }
        })
        .catch(error => {
          console.error('Error during login:', error.response.data);
          alert('Login error');
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
