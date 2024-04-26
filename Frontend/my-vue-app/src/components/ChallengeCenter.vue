<template>
  <!-- Container for the Gamification component -->
  <div class="Gamification">
    <!-- Header section -->
    <header>
      <h1>Challenge Center</h1>
    </header>

    <!-- Main content section -->
    <main>
      <!-- Button container for badges and challenges -->
      <div class="button-container">
        <!-- Button group for badges -->
        <div class="button-group top">
          <button class="square-button" @click="fetchUserBadges">Badges</button>
        </div>
        <!-- Button group for challenges -->
        <div class="button-group bottom">
          <button class="square-button" @click="openAndShowModal">Challenges in Progress</button>
          <button class="square-button" @click="toggleEcoPoints">{{ ecoPointsText }}</button>
          <button class="square-button" @click="openChallengeInbox">Challenge Inbox</button>
          <button class="square-button" @click="openSendChallenges">Send Challenges</button>
          <button class="square-button" @click="openJoinChallenges">Join Challenges</button>
          <button class="square-button" @click="openCreateChallenges">Create Challenges</button>
        </div>
      </div>
    </main>

    <!-- Modal for displaying challenges in progress -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="showModal = false">&times;</span>
        <!-- Title for the modal -->
        <h2>Challenges in Progress</h2>
        <!-- Filtering for the table -->
        <div class="filter-search">
          <div class="filter-buttons">
            <label>Status:</label>
            <select v-model="selectedStatusInProgressChallenges">
              <option value="">All</option>
              <option value="active">Active</option>
              <option value="Participating">Participating</option>
            </select>
            <label>Challenge Type:</label>
            <select v-model="selectedChallengeTypeInProgress">
              <option value="">All</option>
              <option value="Personal">Personal</option>
              <option value="Community">Community</option>
            </select>
          </div>
          <div class="search-input">
            <label>Search:</label>
            <input type="text" v-model="searchQueryInProgress" placeholder="Search...">
          </div>
        </div>
        <div class="table-container">
          <!-- Table to display challenges -->
          <table>
            <tr>
              <th>Name</th>
              <th>Status</th>
              <th>Challenge Type</th>
              <th>Start Date</th>
              <th>Impact Score</th>
            </tr>
            <!-- Loop through challenges and display details -->
            <tr v-for="challenge in filteredUserChallengeStatuses" :key="challenge.challenge_id">
              <td>{{ challenge.name }}</td>
              <td>
                <span class="status-button" :class="{
                  'status-pending': challenge.status === 'Participating',
                  'status-accepted': challenge.status === 'active'
                }">
                  {{ challenge.status }}
                </span>
              </td>
              <td>
                <span class="challenge-type-button" :class="{
                  'challenge-type-personal': challenge.type === 'Personal',
                  'challenge-type-community': challenge.type === 'Community'
                }">
                  {{ challenge.type }}
                </span>
              </td>
              <td>{{ formatDate(challenge.start_date) }}</td>
              <td>
                <span class="impact-score">{{ challenge.impact_score }}</span>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>

    <!-- Modal for displaying user badges -->
    <div v-if="showBadgesModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="showBadgesModal = false">&times;</span>
        <!-- Title for the modal -->
        <h2 class="modal-title">Your Badges</h2>
        <!-- Container for displaying badges -->
        <div class="badges-container">
          <!-- Loop through badges and display images -->
          <img
              v-for="badge in badges"
              :key="badge.id"
              :src="getBadgeImagePath(badge)"
              :alt="badge.name"
              class="badge-image"
          />
        </div>
      </div>
    </div>

    <!-- Modal for displaying challenge inbox -->
    <div v-if="showChallengeInboxModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="showChallengeInboxModal = false">&times;</span>
        <!-- Title for the modal -->
        <h2>Challenge Inbox</h2>
        <!-- Buttons for switching between sent and received challenges -->
        <div class="toggle-button">
          <button class="toggle-btn" @click="fetchSentChallenges" :class="{ active: selectedChallengeCategory === 'sent' }">
            Sent Challenges
          </button>
          <button class="toggle-btn" @click="fetchReceivedChallenges" :class="{ active: selectedChallengeCategory === 'received' }">
            Received Challenges
          </button>
        </div>
        <!-- Filtering and search -->
        <div class="filter-search">
          <div class="filter-buttons">
            <label>Status:</label>
            <select v-model="selectedStatus">
              <option value="">All</option>
              <option value="pending">Pending</option>
              <option value="accepted">Accepted</option>
              <option value="rejected">Rejected</option>
            </select>
            <label>Type:</label>
            <select v-model="selectedChallengeType">
              <option value="">All</option>
              <option value="Personal">Personal</option>
              <option value="Community">Community</option>
            </select>
          </div>
          <div class="search-input">
            <label>Search:</label>
            <input type="text" v-model="searchQuery" placeholder="Search...">
          </div>
        </div>
        <!-- Table to display challenges -->
        <div class="table-container">
          <table>
            <thead>
            <tr>
              <th>Challenge Name</th>
              <th>{{ selectedChallengeCategory === 'sent' ? 'Receiver Name' : 'Sender Name' }}</th>
              <th>{{ selectedChallengeCategory === 'sent' ? 'Date Sent' : 'Date Received' }}</th>
              <th>Status</th>
              <th>Challenge Type</th>
              <th v-if="selectedChallengeCategory === 'received'">Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-if="filteredChallenges.length === 0">
              <td colspan="6">No challenges to display.</td>
            </tr>
            <tr v-else v-for="challenge in filteredChallenges" :key="challenge.id">
              <td>{{ getChallengeName(challenge) }}</td>
              <td>{{
                  selectedChallengeCategory === 'sent' ? challenge.recipient_username : challenge.sender_username
                }}
              </td>
              <td>{{ formatDate(challenge.timestamp) }}</td>
              <td>
                <span class="status-button" :class="{
                  'status-pending': challenge.status === 'pending',
                  'status-accepted': challenge.status === 'accepted',
                  'status-rejected': challenge.status === 'rejected'
                }">
                  {{ challenge.status }}
                </span>
              </td>
              <td>
                <span class="challenge-type-button" :class="{
                  'challenge-type-personal': challenge.challenge_type === 'Personal',
                  'challenge-type-community': challenge.challenge_type === 'Community'
                }">
                  {{ challenge.challenge_type }}
                </span>
              </td>
              <td v-if="selectedChallengeCategory === 'received'">
                <div class="dropdown" v-if="challenge.status === 'pending'">
                  <button class="dropdown-toggle">Action</button>
                  <div class="dropdown-menu">
                    <a class="dropdown-item" @click="acceptChallenge(challenge)">Accept</a>
                    <a class="dropdown-item" @click="rejectChallenge(challenge)">Reject</a>
                  </div>
                </div>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Modal for displaying send challenges -->
    <div v-if="showSendChallengesModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="closeSendChallengesModal">&times;</span>
        <!-- Title for the modal -->
        <h2>Send Challenges</h2>
        <!-- Buttons for switching between personal and community challenges -->
        <div class="toggle-button">
          <button class="toggle-btn" @click="fetchPersonalChallengesForSending"
                  :class="{ active: selectedSendChallengeType === 'personal' }">
            Personal Challenges
          </button>
          <button class="toggle-btn" @click="fetchCommunityChallengesForSending"
                  :class="{ active: selectedSendChallengeType === 'community' }">
            Community Challenges
          </button>
        </div>
        <!-- Search fields -->
        <div class="search-fields">
          <input v-model="challengeSearchQuery" placeholder="Search challenges...">
          <input v-model="userSearchQuery" placeholder="Search users...">
        </div>
        <!-- Table to display challenges -->
        <table v-if="selectedSendChallengeType === 'personal'">
          <thead>
          <tr>
            <th>Challenge Name</th>
            <th>User</th>
            <th>Action</th>
            <th>Status</th>
          </tr>
          </thead>
          <tbody>
          <tr v-if="filteredSendPersonalChallenges.length === 0">
            <td colspan="4">No personal challenges to display.</td>
          </tr>
          <tr v-else v-for="(challenge) in filteredSendPersonalChallenges" :key="challenge.id">
            <td>{{ challenge.name }}</td>
            <td>
              <select v-model.number="challenge.selectedUser">
                <option :value="null" disabled>Select a user</option>
                <option v-for="user in filteredUsers" :key="user.id" :value="user.user_id">
                  {{ user.username }}
                </option>
              </select>
            </td>
            <td>
              <button class="send-challenges-button" @click="sendChallenge(challenge)">Send</button>
            </td>
            <td>{{ challenge.sendStatus }}</td>
          </tr>
          </tbody>
        </table>
        <table v-else-if="selectedSendChallengeType === 'community'">
          <thead>
          <tr>
            <th>Challenge Name</th>
            <th>User</th>
            <th>Action</th>
            <th>Status</th>
          </tr>
          </thead>
          <tbody>
          <tr v-if="filteredSendCommunityChallenges.length === 0">
            <td colspan="4">No community challenges to display.</td>
          </tr>
          <tr v-else v-for="(challenge) in filteredSendCommunityChallenges" :key="challenge.id">
            <td>{{ challenge.name }}</td>
            <td>
              <select v-model.number="challenge.selectedUser">
                <option :value="null" disabled>Select a user</option>
                <option v-for="user in filteredUsers" :key="user.id" :value="user.user_id">
                  {{ user.username }}
                </option>
              </select>
            </td>
            <td>
              <button class="send-challenges-button" @click="sendChallenge(challenge)">Send</button>
            </td>
            <td>{{ challenge.sendStatus }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal for "Join Challenges" -->
    <div v-if="showJoinChallengesModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="closeJoinChallengesModal">&times;</span>
        <!-- Title for the modal -->
        <h2>Join Challenges</h2>

        <!-- Loading Indicator using vue-spinner -->
        <div v-if="isLoadingJoinChallenges" class="loading-indicator">
        </div>
        <!-- Content to be shown when not loading -->
        <div v-if="isLoadingJoinChallenges === false">
          <!-- Buttons for switching between personal and community challenges -->
          <div class="toggle-button">
            <button class="toggle-btn" @click="fetchPersonalChallengesForSending(); selectedJoinChallengeType = 'personal'"
                    :class="{ active: selectedJoinChallengeType === 'personal' }">
              Personal Challenges
            </button>
            <button class="toggle-btn" @click="fetchCommunityChallengesForSending(); selectedJoinChallengeType = 'community'"
                    :class="{ active: selectedJoinChallengeType === 'community' }">
              Community Challenges
            </button>
          </div>
          <!-- Table to display challenges -->
          <table v-if="selectedJoinChallengeType === 'personal'">
            <thead>
            <tr>
              <th>Challenge Name</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-if="filteredJoinPersonalChallenges.length === 0">
              <td colspan="3">No personal challenges to display.</td>
            </tr>
            <tr v-else v-for="challenge in filteredJoinPersonalChallenges" :key="challenge.id">
              <td>{{ challenge.name }}</td>
              <td>{{ getUserChallengeStatus(challenge) }}</td>
              <td>
                <button v-if="getUserChallengeStatus(challenge) !== 'Participating'" @click="joinChallenge(challenge)">
                  Join
                </button>
                <button v-else disabled>Participating</button>
              </td>
            </tr>
            </tbody>
          </table>
          <table v-else-if="selectedJoinChallengeType === 'community'">
            <thead>
            <tr>
              <th>Challenge Name</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-if="filteredJoinCommunityChallenges.length === 0">
              <td colspan="3">No community challenges to display.</td>
            </tr>
            <tr v-else v-for="challenge in filteredJoinCommunityChallenges" :key="challenge.id">
              <td>{{ challenge.name }}</td>
              <td>{{ getUserChallengeStatus(challenge) }}</td>
              <td>
                <button v-if="getUserChallengeStatus(challenge) !== 'active'" class="send-challenges-button"
                        @click="joinChallenge(challenge)">Join
                </button>
                <button v-else disabled>Participating</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Modal for "Create Challenges" -->
    <div v-if="showCreateChallengesModal" class="modal">
      <div class="modal-content">
        <!-- Close button for the modal -->
        <span class="close" @click="closeCreateChallengesModal">&times;</span>
        <!-- Title for the modal -->
        <h2>Create Challenges</h2>
        <div class="toggle-button">
          <button class="toggle-btn" :class="{ active: showPersonal }" @click="showPersonal = true">Personal Challenge
          </button>
          <button class="toggle-btn" :class="{ active: !showPersonal }" @click="showPersonal = false">Community
            Challenge
          </button>
        </div>

        <div v-if="showPersonal">
          <div class="form-group">
            <label for="challenge-title">Challenge Title:</label>
            <input type="text" id="challenge-title" v-model="challengeTitle" placeholder="Enter challenge title"
                   class="form-control">
          </div>

          <div class="form-group">
            <label for="challenge-description">Challenge Description:</label>
            <textarea id="challenge-description" v-model="challengeDescription"
                      placeholder="Enter challenge description" class="form-control"></textarea>
          </div>

          <div class="form-group">
            <label for="eco-points">Eco Point Reward:</label>
            <input type="number" id="eco-points" v-model="eco_points" placeholder="Enter Eco Points"
                   class="form-control">
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

          <button class="btn btn-success" @click="createPersonalChallenge">Create Personal Challenge!</button>
        </div>

        <div v-else>
          <div class="form-group">
            <label for="community-challenge-title">Challenge Title:</label>
            <input type="text" id="community-challenge-title" v-model="communityChallengeTitle"
                   placeholder="Enter challenge title" class="form-control">
          </div>

          <div class="form-group">
            <label for="community-challenge-description">Challenge Description:</label>
            <textarea id="community-challenge-description" v-model="communityChallengeDescription"
                      placeholder="Enter challenge description" class="form-control"></textarea>
          </div>

          <div class="form-group">
            <label for="community-eco-points">Eco Point Reward:</label>
            <input type="number" id="community-eco-points" v-model="communityEcoPoints" placeholder="Enter Eco Points"
                   class="form-control">
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

          <button class="btn btn-success" @click="createCommunityChallenge">Create Community Challenge!</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'; // Importing Vuex mapGetters
import axios from 'axios';

export default {
  name: 'ChallengeCenter', // Component name
  computed: {
    ...mapGetters(['currentUser']), // Mapping currentUser getter from Vuex store
    // Ensure userID is available for all methods
    userID() { // Computed property to get the userID
      return this.currentUser ? this.currentUser.userId : null; // If currentUser exists, return its userID, otherwise return null
    },
    filteredChallenges() {
      let challenges = this.selectedChallengeCategory === 'sent' ? this.sentChallenges : this.receivedChallenges;
      if (!Array.isArray(challenges)) return [];

      // Filter by status
      if (this.selectedStatus) {
        challenges = challenges.filter(challenge => challenge.status === this.selectedStatus);
      }

      // Filter by challenge type
      if (this.selectedChallengeType) {
        challenges = challenges.filter(challenge => challenge.challenge_type === this.selectedChallengeType);
      }

      // Filter by search query
      if (this.searchQuery) {
        const searchLower = this.searchQuery.toLowerCase();
        challenges = challenges.filter(challenge =>
            (challenge.challenge_name || '').toLowerCase().includes(searchLower) ||
            (challenge.recipient_username || '').toLowerCase().includes(searchLower) ||
            (challenge.sender_username || '').toLowerCase().includes(searchLower)
        );
      }

      return challenges;
    },
    filteredSendPersonalChallenges() {
      return this.sendChallenges.filter(challenge =>
          challenge.challenge_type === 'Personal' &&
          challenge.name.toLowerCase().includes(this.challengeSearchQuery.toLowerCase())
      );
    },
    filteredSendCommunityChallenges() {
      return this.sendChallenges.filter(challenge =>
          challenge.challenge_type === 'Community' &&
          challenge.name.toLowerCase().includes(this.challengeSearchQuery.toLowerCase())
      );
    },
    filteredUsers() {
      return this.users.filter(user =>
          user.username.toLowerCase().includes(this.userSearchQuery.toLowerCase())
      );
    },
    filteredJoinPersonalChallenges() {
      return this.joinChallenges.filter(challenge =>
          challenge.challenge_type === 'Personal' &&
          challenge.name.toLowerCase().includes(this.challengeSearchQuery.toLowerCase())
      );
    },
    filteredJoinCommunityChallenges() {
      return this.joinChallenges.filter(challenge =>
          challenge.challenge_type === 'Community' &&
          challenge.name.toLowerCase().includes(this.challengeSearchQuery.toLowerCase())
      );
    },
    // filtering for challenges in progress
    filteredUserChallengeStatuses() {
      let challenges = this.userChallengeStatuses;
      if (!Array.isArray(challenges)) return [];

      // Filter by status
      if (this.selectedStatusInProgressChallenges) {
        challenges = challenges.filter(challenge => challenge.status === this.selectedStatusInProgressChallenges);
      }

      // Filter by challenge type
      if (this.selectedChallengeTypeInProgress) {
        challenges = challenges.filter(challenge => challenge.type === this.selectedChallengeTypeInProgress);
      }

      // Filter by search query
      if (this.searchQueryInProgress) {
        const searchLower = this.searchQueryInProgress.toLowerCase();
        challenges = challenges.filter(challenge =>
            challenge.name.toLowerCase().includes(searchLower)
        );
      }
      console.log(challenges);
      return challenges;
    },
  },
  created() {
    this.fetchUserChallengeStatuses();
    this.fetchUsers();
    this.fetchCommunityChallengesForSending();
    this.fetchPersonalChallengesForSending();
  },

  data() {
    return {
      ecoPoints: 0, // Initial eco points
      ecoPointsText: 'Eco-points', // Text displayed for eco points
      challenges: [], // Array to store challenges
      showModal: false, // Flag to control display of challenge modal
      badges: [], // Array to store user badges
      showBadgesModal: false, // Flag to control display of badges modal
      showChallengeInboxModal: false,
      selectedChallengeType: '',
      selectedChallengeCategory: 'received',
      selectedStatus: '',
      sentChallenges: [],
      receivedChallenges: [],
      searchQuery: '',
      showSendChallengesModal: false,
      selectedSendChallengeType: 'personal',
      sendChallenges: [],
      challengeSearchQuery: '',
      userSearchQuery: '',
      users: [],
      selectedUsers: [],
      sendStatus: {},
      isLoading: false,
      isLoadingSendChallenges: false,
      showJoinChallengesModal: false,
      selectedJoinChallengeType: 'personal',
      joinChallenges: [],
      userChallengeStatuses: [],
      isLoadingJoinChallenges: false,
      selectedChallengeTypeInProgress: 'Personal',
      selectedStatusInProgressChallenges: '',
      searchQueryInProgress: '',
      showCreateChallengesModal: false,

      showPersonal: true,
      challengeTitle: '',
      challengeDescription: '',
      eco_points: null,
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
    navigateTo(routeName) { // Method to navigate to a specified route
      this.$router.push({name: routeName}); // Pushing route to router with specified name
    },
    openChallengeInbox() {
      Promise.all([
        this.fetchReceivedChallenges(),
        this.fetchSentChallenges()
      ]).then(() => {
        this.showChallengeInboxModal = true;
      });
    },
    openSendChallenges() {
      this.isLoadingSendChallenges = true; // Set loading true when opening send challenges
      Promise.all([
        this.fetchUsers(),
        this.fetchPersonalChallengesForSending(),
        this.fetchCommunityChallengesForSending(),
      ]).then(() => {
        this.showSendChallengesModal = true;
        this.isLoadingSendChallenges = false;  // Set loading false after all promises are settled
      }).catch(() => {
        this.isLoadingSendChallenges = false;  // Ensure to turn off loading even if there's an error
      });
    },
    // use Promise.all for openJoinChallenges
    openJoinChallenges() {
      this.isLoadingJoinChallenges = true;
      Promise.all([
        this.fetchUserChallengeStatuses(),
        this.fetchUsers(),
        this.fetchPersonalChallengesForSending(),
        this.fetchCommunityChallengesForSending(),
      ]).then(() => {
        this.isLoadingJoinChallenges = false;
        this.showJoinChallengesModal = true;
      }).catch(() => {
        this.isLoadingJoinChallenges = false;
      });
    },

    // Method to reset Send Challenges modal data
    resetSendChallengesData() {
      this.challengeSearchQuery = "";
      this.userSearchQuery = "";
      this.filteredSendCommunityChallenges = [];
      this.filteredSendPersonalChallenges = [];
      this.sendChallenges = [];
      this.users = [];
      this.selectedSendChallengeType = 'personal';
    },

    // Method to reset Join Challenges modal data
    resetJoinChallengesData() {
      // Reset any relevant data for join challenges
      this.filteredJoinPersonalChallenges = [];
      this.filteredJoinCommunityChallenges = [];
      this.joinChallenges = [];
      this.userChallengeStatuses = [];
      this.users = [];
      this.selectedJoinChallengeType = 'personal';
    },

    closeSendChallengesModal() {
      this.showSendChallengesModal = false;
      this.resetSendChallengesData(); // Call reset method
    },

    closeJoinChallengesModal() {
      this.showJoinChallengesModal = false;
      this.resetJoinChallengesData(); // Call reset method
    },

    openCreateChallenges() {
      this.showCreateChallengesModal = true;
    },

    closeCreateChallengesModal() {
      this.showCreateChallengesModal = false;
    },

    openAndShowModal() {
      this.fetchUserChallengeStatuses();
      this.showModal = true;
    },

    toggleEcoPoints() { // Method to toggle display of eco points
      if (!this.userID) { // If userID is not available
        alert("Please log in to access eco points."); // Show alert
        return;
      }
      if (this.ecoPointsText === 'Eco-points') { // If eco points are currently displayed
        // Fetch impact details and update eco points
        this.getImpactDetails().then(() => {
          // Assuming impact score is part of the impactDetails
          if (this.impactDetails && this.impactDetails.impact_score !== undefined) {
            this.ecoPoints = this.impactDetails.impact_score; // Update eco points
            this.ecoPointsText = `You have ${this.ecoPoints} eco points`; // Update display text
          } else {
            console.error("Impact score is not available.");
            this.ecoPointsText = 'No impact score available'; // Display error message
          }
        }).catch(error => {
          console.error('Failed to fetch impact details:', error);
          this.ecoPointsText = 'Failed to load eco points'; // Display error message
        });
      } else {
        this.ecoPointsText = 'Eco-points'; // Reset to default text when toggled again
      }
    },

    async getImpactDetails() { // Method to fetch impact details
      if (!this.userID) { // If userID is not available
        console.error('No user ID available to fetch impact details.');
        return Promise.reject('No user ID provided'); // Reject promise
      }

      try {
        const response = await axios.get(`https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_impact/${this.userID}`);
        if (response.data && Array.isArray(response.data) && response.data.length > 0) {
          this.impactDetails = response.data[0]; // Store impact details
          console.log('Impact Details:', this.impactDetails);
          return Promise.resolve(); // Resolve promise
        } else {
          console.error('Unexpected response format:', response.data);
          return Promise.reject('Invalid response format'); // Reject promise
        }
      } catch (error) {
        console.error('Error fetching impact details:', error);
        return Promise.reject(error); // Reject promise
      }
    },

    fetchPersonalChallenges() { // Method to fetch personal challenges
      if (!this.userID) { // If userID is not available
        console.error('User ID is not available.');
        return;
      }
      console.log('Fetching personal challenges...');

      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_personal_challenges/${this.userID}`;

      axios.get(url)
          .then(response => {
            if (response.status === 200) {
              console.log("Fetch successful!");
              this.challenges = response.data;  // Store fetched challenges
              this.showModal = true;  // Show the modal
            } else {
              console.error('Challenges not found.');
            }
          })
          .catch(error => {
            console.error("Error:", error.response);
          });
    },

    fetchUserBadges() { // Method to fetch user badges
      if (!this.userID) { // If userID is not available
        console.error('User ID is not available.');
        return;
      }
      // Replace with your actual API call to fetch badges
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_badges/${this.userID}`;

      axios.get(url)
          .then(response => {
            if (response.status === 200) {
              this.badges = response.data.badges;  // Store fetched badges
              this.showBadgesModal = true;  // Show the badges modal
            } else {
              console.error('Badges not found.');
            }
          })
          .catch(error => {
            console.error("Error:", error.response);
          });
    },

    getBadgeImagePath(badgeName) { // Method to get badge image path
      // Requires the image from the assets folder so webpack can process it
      return require(`@/assets/Badges/${badgeName}.png`); // Return the path to the badge image
    },
    fetchSentChallenges() {
      this.isLoading = true;
      this.selectedChallengeType = '';
      this.selectedStatus = '';
      const personalChallengesUrl = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_sent_personal_challenges/${this.userID}`;
      const communityChallengesUrl = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_sent_community_challenges/${this.userID}`;

      Promise.allSettled([
        axios.get(personalChallengesUrl),
        axios.get(communityChallengesUrl)
      ]).then(results => {
        const personalChallenges = results[0].status === 'fulfilled' ? results[0].value.data.map(challenge => ({
          ...challenge,
          challenge_type: 'Personal'
        })) : [];
        const communityChallenges = results[1].status === 'fulfilled' ? results[1].value.data.map(challenge => ({
          ...challenge,
          challenge_type: 'Community'
        })) : [];

        this.sentChallenges = [...personalChallenges, ...communityChallenges];
        if (results[0].status === 'rejected') {
          console.error('Error fetching personal challenges:', results[0].reason);
        }
        if (results[1].status === 'rejected') {
          console.error('Error fetching community challenges:', results[1].reason);
        }
        this.selectedChallengeCategory = 'sent';
      }).finally(() => {
        this.isLoading = false;
      });
    },

    fetchReceivedChallenges() {
      this.isLoading = true;
      this.selectedChallengeType = '';
      this.selectedStatus = '';
      const personalChallengesUrl = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_received_personal_challenges/${this.userID}`;
      const communityChallengesUrl = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_received_community_challenges/${this.userID}`;

      Promise.allSettled([
        axios.get(personalChallengesUrl),
        axios.get(communityChallengesUrl)
      ]).then(results => {
        const personalChallenges = results[0].status === 'fulfilled' ? results[0].value.data.map(challenge => ({
          ...challenge,
          challenge_type: 'Personal'
        })) : [];
        const communityChallenges = results[1].status === 'fulfilled' ? results[1].value.data.map(challenge => ({
          ...challenge,
          challenge_type: 'Community'
        })) : [];

        this.receivedChallenges = [...personalChallenges, ...communityChallenges];
        if (results[0].status === 'rejected') {
          console.error('Error fetching personal challenges:', results[0].reason);
        }
        if (results[1].status === 'rejected') {
          console.error('Error fetching community challenges:', results[1].reason);
        }
        this.selectedChallengeCategory = 'received';
      }).finally(() => {
        this.isLoading = false;
      });
    },

    acceptChallenge(challenge) {
      const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/accept_challenge';
      axios
          .put(url, {
            challenge_id: challenge.id,
            user_id: this.userID,
            challenge_type: challenge.challenge_type.toLowerCase(),
          })
          .then(response => {
            if (response.status === 200) {
              challenge.status = 'accepted';
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },
    rejectChallenge(challenge) {
      const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/reject_challenge';
      axios
          .put(url, {
            challenge_id: challenge.id,
            user_id: this.userID,
            challenge_type: challenge.challenge_type.toLowerCase(),
          })
          .then(response => {
            if (response.status === 200) {
              challenge.status = 'rejected';
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString();
    },

    fetchPersonalChallengesForSending() {
      this.isLoadingSendChallenges = true;
      this.selectedSendChallengeType = 'personal';
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_personal_challenges/${this.userID}`;
      axios
          .get(url)
          .then(response => {
            if (response.status === 200) {
              this.sendChallenges = response.data.map(challenge => ({
                ...challenge,
                selectedUser: null,
                sendStatus: '',
                challenge_type: 'Personal',
              }));
              this.joinChallenges = response.data.map(challenge => ({
                ...challenge,
                selectedUser: null,
                sendStatus: '',
                challenge_type: 'Personal',
              }));
            } else {
              console.error('Personal challenges not found.');
            }
            this.isLoadingSendChallenges = false;
          })
          .catch(error => {
            console.error('Error:', error.response);
            this.isLoadingSendChallenges = false;
          });
    },
    fetchCommunityChallengesForSending() {
      this.isLoadingSendChallenges = true;
      this.selectedSendChallengeType = 'community';
      const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_community_challenges';
      axios
          .get(url)
          .then(response => {
            if (response.status === 200) {
              this.sendChallenges = response.data.map(challenge => ({
                ...challenge,
                selectedUser: null,
                sendStatus: '',
                challenge_type: 'Community',
              }));
              this.joinChallenges = response.data.map(challenge => ({
                ...challenge,
                selectedUser: null,
                sendStatus: '',
                challenge_type: 'Community',
              }));
            } else {
              console.error('Community challenges not found.');
            }
            this.isLoadingSendChallenges = false;
          })
          .catch(error => {
            console.error('Error:', error.response);
            this.isLoadingSendChallenges = false;
          });
    },

    fetchUsers() {
      const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_users';
      axios.get(url).then(response => {
        if (response.status === 200) {
          this.users = response.data.filter(user => user.user_id !== this.userID);
        } else {
          console.error('Users not found.');
        }
      }).catch(error => {
        console.error('Error:', error.response);
      });
    },

    sendChallenge(challenge) {
      const recipientId = challenge.selectedUser;
      console.log('Sending challenge to recipient ID:', recipientId);
      if (!recipientId) {
        challenge.sendStatus = 'Please select a user';
        return;
      }

      const url = this.selectedSendChallengeType === 'personal'
          ? 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/send_personal_challenge'
          : 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/send_community_challenge';

      const data = {
        sender_id: this.userID,
        recipient_id: recipientId,
        [this.selectedSendChallengeType === 'personal' ? 'challenge_id' : 'community_challenge_id']: this.selectedSendChallengeType === 'personal' ? challenge.challenge_id : challenge.id,
      };

      axios
          .post(url, data)
          .then(response => {
            if (response.status === 200) {
              challenge.sendStatus = 'Sent successfully';
            } else {
              challenge.sendStatus = 'Failed to send';
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
            challenge.sendStatus = 'Failed to send';
          });
    },

    getChallengeName(challenge) {
      return challenge.community_challenge_name || challenge.challenge_name;
    },

    getUserChallengeStatus(challenge) {
      const userChallengeStatus = this.userChallengeStatuses.find(status =>
          (status.type === 'Personal' && status.challenge_id === challenge.challenge_id) ||
          (status.type === 'Community' && status.challenge_id === challenge.id)
      );
      return userChallengeStatus ? userChallengeStatus.status : 'Not Participating';
    },

    fetchUserChallengeStatuses() {
      this.selectedChallengeTypeInProgress = '';
      this.selectedStatusInProgressChallenges = '';
      this.searchQueryInProgress = '';
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/user_challenge_status/${this.userID}`;
      axios.get(url)
          .then(response => {
            if (response.status === 200) {
              this.userChallengeStatuses = response.data;
            } else {
              console.error('User challenge statuses not found.');
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    joinChallenge(challenge) {
      const url = challenge.challenge_type === 'Personal'
          ? 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/join_personal_challenge'
          : 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/join_community_challenge';
      const data = {
        user_id: this.userID,
        [challenge.challenge_type === 'Personal' ? 'challenge_id' : 'community_challenge_id']: challenge.id,
      };
      axios.post(url, data)
          .then(response => {
            if (response.status === 200) {
              // Update the user challenge status after joining
              this.fetchUserChallengeStatuses();
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    async createPersonalChallenge() {
      if (this.challengeTitle && this.challengeDescription && this.eco_points && this.startDate && this.endDate) {
        if (!this.userID) {
          console.error('User ID is empty');
          return;
        }

        try {
          const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/create_personal_challenge';
          const response = await axios.post(url, {
            user_id: this.userID,
            name: this.challengeTitle,
            description: this.challengeDescription,
            eco_points: this.eco_points,
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
          const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/create_community_challenge';
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
    },
  },
  watch: {
    showSendChallengesModal(newVal) {
      if (newVal) {
        this.fetchUsers();
        this.fetchPersonalChallengesForSending();
      }
    },
    showJoinChallengesModal(newVal) {
      if (newVal) {
        this.fetchUsers();
        this.fetchUserChallengeStatuses();
        this.fetchPersonalChallengesForSending();
      }
    },
  }
}
</script>

<style scoped>
/* Scoped styles for Gamification component */
.Gamification {
  font-family: 'Roboto', sans-serif;
  color: #333;
  background: #e4fcec;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 2rem auto;
}

/* Header styles */
header {
  background: linear-gradient(to right, #4CAF50, #8BC34A);
  color: white;
  padding: 1rem 0;
  border-radius: 8px 8px 0 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  font-size: 1.5rem;
  position: relative;
}

/* Logout button styles */
.logout-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 15px;
  background: #FF6347;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  border: none;
}

/* Main content styles */
main {
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Button container styles */
.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

/* Button group styles */
.button-group {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 10px;
  margin-bottom: 20px;
}

/* Square button styles */
.square-button {
  width: 150px;
  height: 150px;
  margin: 10px;
  border: none;
  background-color: #8BC34A;
  cursor: pointer;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s, transform 0.1s;
}

/* Square button hover styles */
.square-button:hover {
  background-color: #7CB342;
  transform: translateY(-2px);
}

/* Modal styles */
.modal {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Modal content styles */
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 700px;
}

/* Close button styles */
.close {
  float: right;
  font-size: 18px;
  cursor: pointer;
  border: 2px double #394936;
  border-radius: 5px;
  padding: 5px 10px;
  color: #b1060d;
}
.close:hover {
  color: #e30a0a;
  background-color: #d7f7d9;
}

/* Table styles */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

/* Header row styles */
th {
  background-color: #4CAF50;
  color: white;
}

/* Badges container styles */
.badges-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 0.1rem;
}

/* Badge image styles */
.badge-image {
  max-width: 250px;
  margin: 1rem;
  border: 3px solid #4CAF50;
  border-radius: 50%;
}

.toggle-btn {
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
  width: 100%;
}

.toggle-btn button {
  margin-right: 10px;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #eee;
  cursor: pointer;
  font-size: 18px;
}

.toggle-btn button.active {
  background-color: #4caf50;
  color: white;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  padding: 5px 10px;
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}

.dropdown-menu {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 120px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown:hover .dropdown-menu {
  display: block;
}

.dropdown-item {
  padding: 8px 16px;
  text-decoration: none;
  display: block;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f1f1f1;
}

.search-fields {
  margin-bottom: 10px;
}

.search-fields input {
  width: calc(50% - 12px);
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  outline: none;
  transition: all 0.3s ease;
}

.search-fields input:focus {
  border-color: #4CAF50;
  box-shadow: 0 0 8px rgba(76, 175, 80, 0.5);
}

.search-fields {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}


.send-challenges-button {
  padding: 8px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  background-color: #2196F3;
  color: white;
}

.send-challenges-button:hover {
  background-color: #950bda;
}

select {
  width: 100%;
  padding: 8px 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.status-button {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  color: #fff;
  font-weight: bold;
  margin: 4px;
}

.status-button:hover {
  opacity: 0.8;
}

.status-pending {
  background-color: #1056b5;
}

.status-accepted {
  background-color: #28a745;
}

.status-rejected {
  background-color: #dc3545;
}

.challenge-type-button {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  color: #fff;
  font-weight: bold;
  margin: 4px;
}

.challenge-type-personal {
  background-color: #007bff;
}

.challenge-type-community {
  background-color: #6c757d;
}

.table-container {
  max-height: 400px;
  overflow-y: auto;
}
.table-container th {
  position: sticky;
  top: 0;
}

.filter-search {
  margin-bottom: 10px;
  display: flex;
}

.filter-search select,
.filter-search input {
  margin-right: 10px;
}

.filter-search {
  margin-bottom: 10px;
}

.filter-buttons {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.filter-buttons label {
  margin-right: 5px;
}

.filter-buttons select {
  margin-right: 10px;
  width: 120px;
  height: 32px;
}

.search-input {
  display: flex;
  align-items: center;
  width: 80px;
}

.search-input label {
  margin-right: 5px;
}

.search-input input {
  width: 200px;
}

.impact-score {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 1.2rem;
  font-weight: bold;
  margin-top: 10px;
  color: white;
  background-color: #21809a;
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

@media (max-width: 768px) {
  .button-group {
    flex-direction: column;
  }
  .modal-content {
    width: 95%;
    padding: 10px;
  }
}

</style>
