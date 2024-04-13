// src/store/index.js
import { createStore } from 'vuex';
import axios from 'axios';
import router from '../router';  // Import router

const store = createStore({
  state() {
    return {
      currentUser: null
    };
  },
  mutations: {
    setCurrentUser(state, userData) {
      state.currentUser = userData;
    }
  },
  actions: {
    loginUser({ commit }, credentials) {
      const loginUrl = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/login';
      axios.post(loginUrl, credentials)
        .then(response => {
          if (response.status === 200 && response.data.user_id) {
            commit('setCurrentUser', {
              userId: response.data.user_id,
              // possibly other user data
            });
            localStorage.setItem('currentUser', JSON.stringify({
              userId: response.data.user_id
            }));
            router.push('/calculator');  // Redirect to Impact Calculator
          } else {
            console.error('Login failed:', response.data);
          }
        })
        .catch(error => {
          console.error('Error during login:', error);
        });
    },
    logoutUser({ commit }) {
      commit('setCurrentUser', null);
      localStorage.removeItem('currentUser');
    }
  },
  getters: {
    currentUser: state => state.currentUser
  }
});

export default store;
