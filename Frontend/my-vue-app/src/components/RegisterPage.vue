<template>
  <div class="RegisterPage">
    <header>
      <h1>Green Wave</h1>
    </header>

    <div class="register-form">
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    register() {
      const apiUrl = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/register';
      const userData = {
        username: this.username,
        email: this.email,
        password: this.password
      };

      axios.post(apiUrl, userData)
          .then(response => {
            if (response.status === 201) {
              console.log("Registration successful!");
              this.$router.push('/calculator');
            } else {
              console.error('Registration failed:', response.data);
              alert('Registration failed');
            }
          })
          .catch(error => {
            console.error('Error during registration:', error.response.data);
            alert('Error during registration');
          });
    }
  }
};
</script>

<style scoped>
header {
  position: relative;
  text-align: center;
  padding: 20px;
  background-color: #4CAF50;
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
  background-image: url('@/assets/background.png');
  opacity: 0.2;
  border-radius: 8px 8px 0 0;
}

.RegisterPage {
  font-family: 'Roboto', sans-serif;
  color: #333;
  background: #e4fcec;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 2rem auto;
}

.register-form {
  background: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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