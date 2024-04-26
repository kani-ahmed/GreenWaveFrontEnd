<template>
  <div>
    <button @click="showModal = true">Create Challenge</button>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Create Challenges</h2>
        <div class="toggle-button">
          <button class="toggle-btn" :class="{ active: showPersonal }" @click="showPersonal = true">Personal Challenge</button>
          <button class="toggle-btn" :class="{ active: !showPersonal }" @click="showPersonal = false">Community Challenge</button>
        </div>

        <div v-if="showPersonal">
          <div class="form-group">
            <label for="challenge-title">Challenge Title:</label>
            <input type="text" id="challenge-title" v-model="challengeTitle" placeholder="Enter challenge title" class="form-control">
          </div>

          <div class="form-group">
            <label for="challenge-description">Challenge Description:</label>
            <textarea id="challenge-description" v-model="challengeDescription" placeholder="Enter challenge description" class="form-control"></textarea>
          </div>

          <div class="form-group">
            <label for="eco-points">Eco Point Reward:</label>
            <input type="number" id="eco-points" v-model="ecoPoints" placeholder="Enter Eco Points" class="form-control">
          </div>

          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="start-date">Start Date:</label>
              <input type="date" id="start-date" v-model="startDate" class="form-control">
            </div>
            <div class="form-group col-md-6">
              <label for="end-date">End Date:</label>
              <input type="date" id="end-date" v-model="endDate" class="form-control">
            </div>
          </div>

          <button class="btn btn-success" @click="createPersonalChallenge">Send Personal Challenge!</button>
        </div>

        <div v-else>
          <div class="form-group">
            <label for="community-challenge-title">Challenge Title:</label>
            <input type="text" id="community-challenge-title" v-model="communityChallengeTitle" placeholder="Enter challenge title" class="form-control">
          </div>

          <div class="form-group">
            <label for="community-challenge-description">Challenge Description:</label>
            <textarea id="community-challenge-description" v-model="communityChallengeDescription" placeholder="Enter challenge description" class="form-control"></textarea>
          </div>

          <div class="form-group">
            <label for="community-eco-points">Eco Point Reward:</label>
            <input type="number" id="community-eco-points" v-model="communityEcoPoints" placeholder="Enter Eco Points" class="form-control">
          </div>

          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="community-start-date">Start Date:</label>
              <input type="date" id="community-start-date" v-model="communityStartDate" class="form-control">
            </div>
            <div class="form-group col-md-6">
              <label for="community-end-date">End Date:</label>
              <input type="date" id="community-end-date" v-model="communityEndDate" class="form-control">
            </div>
          </div>

          <button class="btn btn-success" @click="createCommunityChallenge">Send Community Challenge!</button>
        </div>

        <button class="btn btn-secondary" @click="showModal = false">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters(['currentUser']),
    userID() {
      return this.currentUser ? this.currentUser.userId : null;
    }
  },
  data() {
    return {
      showModal: false,
      showPersonal: true,
      challengeTitle: '',
      challengeDescription: '',
      ecoPoints: null,
      startDate: '',
      endDate: '',
      communityChallengeTitle: '',
      communityChallengeDescription: '',
      communityEcoPoints: null,
      communityStartDate: '',
      communityEndDate: ''
    };
  },
  methods: {
    async createPersonalChallenge() {
      if (this.challengeTitle && this.challengeDescription && this.ecoPoints && this.startDate && this.endDate) {
        if (!this.userID) {
          console.error('User ID is empty');
          return;
        }

        try {
          const url = 'http://127.0.0.1:5000/create_personal_challenge';
          const response = await axios.post(url, {
            user_id: this.userID,
            name: this.challengeTitle,
            description: this.challengeDescription,
            eco_points: this.ecoPoints,
            start_date: this.startDate,
            end_date: this.endDate
          });

          if (response.status === 201) {
            console.log(response.data);
            this.showModal = false;
          } else {
            console.error('Challenge not sent.');
          }
        } catch (error) {
          console.error('Error sending challenge:', error);
        }
      } else {
        console.error('Please fill in all fields.');
      }
    },

    async createCommunityChallenge() {
      if (this.communityChallengeTitle && this.communityChallengeDescription && this.communityEcoPoints && this.communityStartDate && this.communityEndDate) {
        if (!this.userID) {
          console.error('User ID is empty');
          return;
        }

        try {
          const url = 'http://127.0.0.1:5000/create_community_challenge';
          const response = await axios.post(url, {
            name: this.communityChallengeTitle,
            description: this.communityChallengeDescription,
            eco_points: this.communityEcoPoints,
            start_date: this.communityStartDate,
            end_date: this.communityEndDate,
            created_by: this.userID
          });

          if (response.status === 201) {
            console.log('Response:', response.data);
            this.showModal = false;
          } else {
            console.error('Challenge not sent. Status:', response.status);
          }
        } catch (error) {
          console.error('Error sending challenge:', error);
        }
      } else {
        console.error('Please fill in all fields.');
      }
    }
  }
}
</script>

<style scoped>
.modal {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.toggle-button {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.toggle-btn {
  padding: 10px 20px;
  margin: 0 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.toggle-btn.active {
  background-color: #4CAF50;
  color: white;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-row {
  display: flex;
  justify-content: space-between;
}

.form-row .form-group {
  flex: 1;
  margin-right: 10px;
}

.form-row .form-group:last-child {
  margin-right: 0;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-success {
  background-color: #4CAF50;
  color: white;
}

.btn-success:hover {
  background-color: #45a049;
}

.btn-secondary {
  background-color: #ccc;
  color: black;
  margin: 10px;
}

.btn-secondary:hover {
  background-color: #b3b3b3;
}
</style>