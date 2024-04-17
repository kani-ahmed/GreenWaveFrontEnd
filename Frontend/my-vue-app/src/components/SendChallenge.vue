<template>
  <!-- Main container for the send challenge component -->
  <div class="send-challenge">
    <!-- Title -->
    <h2>Send Challenges</h2>
    <!-- Content container -->
    <div>

      <!-- Challenge Dropdown -->
      <div class="input-group">
        <!-- Label for Challenge Dropdown -->
        <div class="left-dropdown">
          <label for="challenge">Challenge:</label>
          <!-- Vue Select component for selecting challenges -->
          <vue-select v-model="selectedChallenge" :options="challenges" placeholder="Type to search" class="custom-select"></vue-select>
        </div>
      </div>

      <!-- User Dropdown -->
      <div class="input-group">
        <!-- Label for User Dropdown -->
        <div class="left-dropdown">
          <label for="user">User:</label>
          <!-- Vue Select component for selecting users -->
          <vue-select v-model="selectedUser" :options="users" placeholder="Type to search" class="custom-select"></vue-select>
        </div>
      </div>

      <!-- Message Textbox -->
      <div class="input-group">
        <!-- Label for Message Textbox -->
        <label for="message">Message:</label>
        <!-- Textarea for typing the message -->
        <textarea id="message" class="input-field" rows="4" cols="50" placeholder="Write Your Message Here" v-model="message"></textarea>
      </div>

      <!-- Submit Button -->
      <button class="submit-button">Submit</button>

      <!-- Your content goes here -->
    </div>
  </div>
</template>

<script>
import VueSelect from 'vue3-select'; // Import Vue 3 Select

export default {
  name: 'SendChallenge',
  components: {
    VueSelect
  },
  data() {
    return {
      selectedChallenge: '',
      selectedUser: '',
      message: '',
      challenges: ['Daily Quick Win: Use a paper straw [5 points]', 'Weekly Warrior: Do not use any single-use water bottles for an entire week[50 points]', 'Monthly Master: Avoid single-use plastics for an entire month[200 points]', 'Yearly Hero: Reduce your yearly personal waste by 50% [1000 points]'], // Sample data for challenges
      users: ['Esteban Linarez', 'Kyle Kaufman', 'Preston DeLeo', 'Kani Ahmed', 'Pranav Dhinakar'] // Sample data for users
    };
  }
}
</script>

<style scoped>
/* Styles specific to this component */

/* Title style */
.centered-title {
  font-size: 2.5em;
  text-align: left; /* Align the title to the left */
}

/* Container for input groups */
.input-group {
  margin-bottom: 20px; /* Add spacing between each input group */
  text-align: left; /* Align the content within the input group to the left */
}

/* Left-aligned dropdown label style */
.left-dropdown {
  display: block; /* Use block layout */
  margin-bottom: 10px; /* Add spacing between each dropdown */
  text-align: left; /* Align the dropdown label to the left */
}

/* Custom styles for Vue Select */
.custom-select .vs__search {
  width: 100%; /* Make the input box stretch to the entire width within the Vue Select dropdown */
}

/* Textarea style */
.input-field {
  width: 100%; /* Make textarea stretch to the entire width */
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* Submit button style */
.submit-button {
  float: right; /* Align the button to the right */
}
</style>
