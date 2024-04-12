<template>
    <div class="register-page">
      <h1>Register</h1>
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
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: ''
      }
    },
    methods: {
      register() {
        const apiUrl = 'http://127.0.0.1:8000/register';
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
  }
  </script>
  
  <style>
  /* Header style */
  .header {
    text-align: center;
    padding: 20px;
    background-color: #4CAF50;
    color: white;
  }
  
  /* Form container style */
  .register-form {
    max-width: 300px;
    margin: 50px auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }
  
  /* Form group styling */
  .form-group {
    margin-bottom: 15px;
  }
  
  /* Label styling within the form */
  .form-group label {
    display: block;
  }
  
  /* Input field styling */
  .form-group input {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
  }
  
  /* Button styling */
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  /* Button hover effect */
  button:hover {
    opacity: 0.8;
  }
  </style>
  
  