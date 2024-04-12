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
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login() {
        console.log(`Logging in with username: ${this.username} and password: ${this.password}`);
      }
    }
  }
  </script>
  
  <style>
  .Homepage header {
    text-align: center;
    padding: 20px;
    background-color: #4CAF50;
    color: white;
  }
  
  .login-form {
    max-width: 300px;
    margin: 50px auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
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
  