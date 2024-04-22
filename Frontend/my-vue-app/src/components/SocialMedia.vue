<template>
  <!-- Social media component template -->
  <div class="social-media-component">
    <!-- Main section for buttons -->
    <main>
      <div class="button-class">
        <div class="button-group-top">
          <!-- Buttons for adding friends, creating a post, and sending a message -->
          <button class="square-button" @click="addfriends">Add Friends</button>
          <button class="square-button" @click="openPostModal()">Create Post</button>
          <button class="square-button" @click="openSendMessage()">Send Message</button>
        </div>
        <div class="button-group-bottom">
          <!-- Buttons for viewing friend list and all posts -->
          <button class="square-button" @click="Friends">Friend List</button>
          <button class="square-button" @click="getAllPosts()">View Posts</button>
        </div>
      </div>
    </main>
  </div>

  <!-- Modal for creating a post -->
  <div v-if="showPostModal" class="modal">
    <div class="modal-content">
      <span class="close" @click="showPostModal = false">&times;</span>
      <h2>Create Post</h2>
      <!-- Text area for writing the post content -->
      <textarea v-model="postContent" placeholder="Write your post here" class="post-textarea"></textarea>
      <!-- Button to submit the post -->
      <button @click="createPost()" class="submit-button">Submit</button>
    </div>
  </div>

  <!-- Add Friends -->
  <div v-if="showAddFriendModal" class="modal">
    <div class="modal-content">
      <span class="close" @click="showAddFriendModal = false">&times;</span>
      <h2>Add Friends </h2>
      <div class="filter-container">
        <label for="filterBy">Filter By:</label>
        <select id="filterBy" v-model="selectedFilter">
          <option value="People">People</option>
          <option value="Action">Action</option>
          <option value="Status">Status</option>
        </select>
        <input type="text" v-model="searchQuery" placeholder="Search people...">
      </div>
      <div class="add-friends-table-container">
        <table class="add-friends-table">
          <thead>
            <tr>
              <th>People</th>
              <th>Action</th>
              <th>Friendship Status</th>
              <th>Requested Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in filteredUsers" :key="user.user_id">
              <td>{{ user.username }}</td>
              <td>
                <button class="friendship-button" :class="{
                    'requested': getFriendshipStatus(user.user_id) === 'requested',
                    'not-requested': getFriendshipStatus(user.user_id) === 'None',
                    'accepted': getFriendshipStatus(user.user_id) === 'Accepted'
                  }" :disabled="getFriendshipStatus(user.user_id) === 'Accepted'"
                  @click="toggleFriendRequest(user.user_id)">
                  {{
                  getFriendshipStatus(user.user_id) === 'requested' ? 'Cancel Request' :
                      getFriendshipStatus(user.user_id) === 'Accepted' ? 'Friends' : 'Send Request'
                }}
                </button>
              </td>
              <td>{{ getFriendshipStatus(user.user_id) }}</td>
              <td>{{ getFriendshipRequestedDate(user.user_id) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Send Message 
    <div v-if="showSendMessageModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showSendMessageModal = false">&times;</span>
        <h2>Send Message</h2>
        <textarea v-model="messageContent" placeholder="Write your message here"></textarea>
        <button @click="sendMessage()">Send</button>
      </div>
    </div>
    -->

    <div v-if="showViewPostsModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showViewPostsModal = false">&times;</span>
        <h2>View All Posts</h2>
        <div class="posts-container">
          <table>
            <tr>
              <th>ID</th>
              <th>User</th>
              <th>Time</th>
              <th>Content</th>
            </tr>
            <tr v-for="post in posts" :key="post.post_id">
              <td>{{ post.post_id }}</td>
              <td>{{ post.username }}</td>
              <td>{{ post.created_at }}</td>
              <td>{{ post.content }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Send Message -->
  <div v-if="showSendMessageModal" class="modal">
    <div class="modal-content">
      <span class="close" @click="showSendMessageModal = false">&times;</span>
      <h2>Send Message</h2>
      <textarea v-model="messageContent" placeholder="Write your message here"></textarea>
      <button @click="sendMessage()">Send</button>
    </div>
  </div>



  <div v-if="showViewPostsModal" class="modal">
    <div class="modal-content">
      <span class="close" @click="showViewPostsModal = false">&times;</span>
      <h2>View All Posts</h2>
      <div class="posts-container">
        <table>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Time</th>
            <th>Content</th>
          </tr>
          <tr v-for="post in posts" :key="post.post_id">
            <td>{{ post.post_id }}</td>
            <td>{{ post.username }}</td>
            <td>{{ post.created_at }}</td>
            <td>{{ post.content }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>

  <!-- Friend List -->
  <div v-if="showFriendListModal" class="modal">
    <div class="modal-content">
      <span class="close" @click="showFriendListModal = false">&times;</span>
      <h2>Friend List</h2>
      <div class="filter-container">
        <label for="filterBy">Filter By:</label>
        <select id="filterBy" v-model="selectedFriendFilter">
          <option value="All">All</option>
          <option value="Friends">Friends</option>
          <option value="Incoming">Incoming Requests</option>
          <option value="Outgoing">Outgoing Requests</option>
        </select>
        <input type="text" v-model="friendSearchQuery" placeholder="Search friends...">
      </div>
      <div class="add-friends-table-container">
        <table class="add-friends-table">
          <thead>
            <tr>
              <th>Friends</th>
              <th>Friendship Status</th>
              <th>Action</th>
              <th>Request Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="friendship in filteredFriends" :key="friendship.id">
              <td>{{ friendship.friend_name }}</td>
              <td>
                <span class="friendship-status" :class="{
                  'accepted': friendship.status === 'accepted',
                  'incoming-request': friendship.request_type === 'incoming' && friendship.status !== 'accepted',
                  'outgoing-request': friendship.request_type === 'outgoing' && friendship.status !== 'accepted'
                }">
                  {{
                friendship.status === 'accepted' ? 'Friends' :
                    friendship.request_type === 'incoming' ? 'Incoming Request' :
                        friendship.request_type === 'outgoing' ? 'Outgoing Request' : ''
              }}
                </span>
              </td>
              <td>
                <button v-if="friendship.status === 'accepted'" class="friendship-button requested"
                  @click="cancelFriendRequest(friendship.friend_id)">
                  Remove
                </button>
                <div v-else-if="friendship.request_type === 'incoming'" class="dropdown">
                  <button class="friendship-button requested dropdown-toggle" type="button" data-toggle="dropdown">
                    Action
                  </button>
                  <div class="dropdown-menu">
                    <a class="dropdown-item" @click="respondToFriendRequest(friendship.friend_id, 'accept')">Accept</a>
                    <a class="dropdown-item"
                      @click="respondToFriendRequest(friendship.friend_id, 'decline')">Decline</a>
                  </div>
                </div>
                <button v-else-if="friendship.request_type === 'outgoing'"
                  class="friendship-button requested-friendslist" @click="cancelFriendRequest(friendship.friend_id)">
                  Cancel Request
                </button>
              </td>
              <td>{{ friendship.created_at }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <!-- Toast component for displaying messages -->
  <toast-component ref="toast" :message="toastMessage" />
</template>

<script>

import axios from 'axios';
import {mapGetters} from 'vuex';
import ToastComponent from './ToastComponent.vue';


export default {
  components: {
    ToastComponent, // Register the ToastComponent
  },
  // Importing computed properties from Vuex store
  computed: {
    ...mapGetters(['currentUser']),
    // Compute the user ID from currentUser
    userID() {
      return this.currentUser ? this.currentUser.userId : null;
    },
    filteredUsers() {
      let filtered = this.users;

      if (this.searchQuery) {
        filtered = filtered.filter(user =>
            user.username.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      if (this.selectedFilter === 'Action') {
        filtered = filtered.filter(user =>
            this.getFriendshipStatus(user.user_id) !== 'None' &&
            this.getFriendshipRequestType(user.user_id) !== 'incoming'
        );
      } else if (this.selectedFilter === 'Status') {
        filtered = filtered.filter(user =>
            this.getFriendshipStatus(user.user_id) !== 'None' &&
            this.getFriendshipRequestType(user.user_id) !== 'incoming'
        );
      }

      // Exclude users who have sent an incoming friend request
      filtered = filtered.filter(user =>
          this.getFriendshipRequestType(user.user_id) !== 'incoming'
      );

      return filtered;
    },
    filteredFriends() {
      let filtered = this.friendships;

      if (this.friendSearchQuery) {
        filtered = filtered.filter(friendship =>
            friendship.friend_name.toLowerCase().includes(this.friendSearchQuery.toLowerCase())
        );
      }

      if (this.selectedFriendFilter === 'Friends') {
        filtered = filtered.filter(friendship => friendship.status === 'accepted');
      } else if (this.selectedFriendFilter === 'Incoming') {
        filtered = filtered.filter(friendship => friendship.request_type === 'incoming');
      } else if (this.selectedFriendFilter === 'Outgoing') {
        filtered = filtered.filter(friendship => friendship.request_type === 'outgoing');
      }

      return filtered;
    },
  },

  name: 'SocialMedia',
  data() {
    // Data properties for managing state
    return {
      showPostModal: false,
      postContent: '',
      showAddFriendModal: false,
      showSendMessageModal: false,

      showViewPostsModal: false,
      posts: [],  // Array to store all posts
      users: [],
      friendships: [],
      selectedFilter: 'People',
      searchQuery: '',
      showFriendListModal: false,
      friendList: [],
      selectedFriendFilter: 'People',
      friendSearchQuery: '',
      toastMessage: '',

    };
  },

  methods: {
    addfriends() {
      if (!this.userID) {
        console.error('Id is empty');
        return;
      }
      this.getAllUsers();
      this.getUserFriendships();
      this.showAddFriendModal = true;
    },

    getAllUsers() {
      const url = 'https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_users';
      axios.get(url)
          .then(response => {
            if (response.status === 200) {
              // Filter out the logged-in user from the list of users
              this.users = response.data.filter(user => user.user_id !== this.userID);
            } else {
              console.error('Users not found.');
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    getUserFriendships() {
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/get_friendships/${this.userID}`;
      axios.get(url)
          .then(response => {
            if (response.status === 200) {
              this.friendships = response.data;
            } else {
              console.error('Friendships not found.');
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    getFriendshipStatus(userId) {
      const friendship = this.friendships.find(
          friendship => (friendship.user_id === this.userID && friendship.friend_id === userId) ||
              (friendship.user_id === userId && friendship.friend_id === this.userID)
      );
      return friendship ? (friendship.status === 'accepted' ? 'Accepted' : friendship.status) : 'None';
    },

    getFriendshipRequestedDate(userId) {
      const friendship = this.friendships.find(
          friendship => (friendship.user_id === this.userID && friendship.friend_id === userId) ||
              (friendship.user_id === userId && friendship.friend_id === this.userID)
      );
      return friendship ? friendship.created_at : 'None';
    },

    toggleFriendRequest(userId) {
      const friendship = this.friendships.find(
          friendship => (friendship.user_id === this.userID && friendship.friend_id === userId) ||
              (friendship.user_id === userId && friendship.friend_id === this.userID)
      );

      if (friendship) {
        if (friendship.status === 'requested') {
          this.cancelFriendRequest(userId);
        }
      } else {
        this.sendFriendRequest(userId);
      }
    },

    sendFriendRequest(userId) {
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/add_friend/${this.userID}/${userId}`;
      axios.post(url)
          .then(response => {
            if (response.status === 201) {
              this.getUserFriendships();
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    cancelFriendRequest(userId) {
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/remove_friend/${this.userID}/${userId}`;
      axios.delete(url)
          .then(response => {
            if (response.status === 200) {
              this.getUserFriendships();
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    showMessage() {
      // Add logic to show the add friends modal
      if (!this.userID) {
        console.error('Id is empty');
        return;
      }
      this.showSendMessageModal = true;

    },

    // Method to create a post
    createPost() {
      // Add logic to show the create post modal
      if (!this.userID) {
        console.error('Id is empty');
        return;
      }
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/create_post`;

      axios.post(url, {
        user_id: this.userID,
        content: this.postContent
      }).then(response => {
        if (response.status === 201) {
          console.log(response.data);
          this.content = response.data;
          console.log(this.content);
          this.toastMessage = "Successfuly Created Post.";
          this.$refs.toast.showToast(3000, 'success', this.toastMessage);
        } else {
          console.error('Post could not be created.');
          this.toastMessage = "Post could not be created.";
          this.$refs.toast.showToast(3000, 'error', this.toastMessage);
        }
      })
          .catch(error => {
            console.error("Error:", error.response);
          });
    },

    // Method to open the create post modal
    openPostModal() {
      this.showPostModal = true;
    },


    // Method to get all posts
    getAllPosts() {
      if (!this.userID) {
        console.error('Id is empty');
        return;
      }

      console.log("Getting all posts")

      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/view_my_posts/${this.userID}`;

      axios.get(url, {
        user_id: this.userID,
      }).then(response => {
        if (response.status === 200) {
          console.log(response.data);
          this.posts = response.data;
          this.showViewPostsModal = true;
          console.log(this.posts);
        } else {
          console.error('Posts not found.');
        }
      })
          .catch(error => {
            console.error("Error:", error.response);
          });
    },


    // Method to open the send message modal
    sendMessage() {
      // Add logic to show the send message modal
    },

    openSendMessage() {
      this.showSendMessageModal = true;
    },

    // Method to view friend list
    Friends() {
      this.getUserFriendships();
      this.showFriendListModal = true;
    },
    viewPosts() {
      // Add logic to show the view posts modal
    },

    respondToFriendRequest(userId, action) {
      console.log('Responding to friend request');
      const url = `https://heroku-project-backend-staging-ffb8722f57d5.herokuapp.com/respond_friend_request/${this.userID}/${userId}`;
      axios.post(url, {action})
          .then(response => {
            if (response.status === 200) {
              this.getUserFriendships();
            }
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
    },

    getFriendshipRequestType(userId) {
      const friendship = this.friendships.find(
          friendship => (friendship.user_id === this.userID && friendship.friend_id === userId) ||
              (friendship.user_id === userId && friendship.friend_id === this.userID)
      );
      return friendship ? friendship.request_type : 'None';
    },

  }
}

</script>

<style scoped>
/* Scoped styles for the social media component */

.social-media-component {
  /* Styles that apply to the whole component */
}

.image-action {
  /* Styles that apply to the first photo */
  /* make image smaller */

  /* add padding */
  /* add border */
  /* add border radius */
  /* add margin */
  /* add box shadow */
  /* add hover effect */
  /* add cursor pointer */
  /* add transition */
}

main {
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.button-group {
  display: flex;
  justify-content: center;
  padding: 10px;
  margin-bottom: 20px;
}

/* Styles for buttons */
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

.square-button:hover {
  background-color: #7CB342;
  transform: translateY(-2px);
}

/* Styles for modal */
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

/* Styles for modal content */
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
}

.posts-container {
  overflow-y: auto;
  /* Only vertical scrolling */
  max-height: 300px;
  /* Adjust based on your needs */
  margin-top: 20px;
  /* Space between header and table */
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #4CAF50;
}

.close {
  float: right;
  font-size: 28px;
  cursor: pointer;
}

.add-friends-table-container {
  max-height: 400px;
  overflow-y: auto;
  margin-top: 20px;
}

.add-friends-table {
  width: 100%;
  border-collapse: collapse;
}

.add-friends-table th,
.add-friends-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.add-friends-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.add-friends-table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.add-friends-table tbody tr:hover {
  background-color: #e9e9e9;
}

.friendship-button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.friendship-button.requested {
  background-color: #b52f7c;
  color: white;
}

.friendship-button.requested:hover {
  background-color: #FF0000;
}

.friendship-button.not-requested {
  background-color: #2196F3;
  color: white;
}

.friendship-button.not-requested:hover {
  background-color: #1976D2;
}

.filter-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.filter-container label {
  margin-right: 10px;
}

.filter-container select,
.filter-container input {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.filter-container input {
  margin-left: 10px;
}

.friendship-button.accepted {
  background-color: #4CAF50;
  color: white;
  cursor: default;
}

.friendship-status {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 4px;
}

.friendship-status.accepted {
  background-color: #4CAF50;
  color: white;
}

.friendship-status.incoming-request {
  background-color: #18b4ec;
  color: white;
}

.friendship-status.outgoing-request {
  background-color: #4555a8;
  color: white;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  background-color: #b52f7c;
  color: white;
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

.requested-friendslist {
  background-color: #FF0000;
  color: white;
}

/* Text area style */
.post-textarea {
  width: 90%;
  height: 150px;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: none;
}

/* Placeholder text style */
.post-textarea::placeholder {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px; /* Adjust font size as needed */
  color: #999; /* Adjust placeholder text color as needed */
}

/* Submit button style */
.submit-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.submit-button:hover {
  background-color: #45a049;
}
</style>
