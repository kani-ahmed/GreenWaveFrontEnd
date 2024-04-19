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
                    <button class="square-button" @click="getAllPosts()">view posts</button>
                </div>
            </div>
        </main>
    </div>

    <!-- Modal for creating a post -->
    <div v-if="showPostModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="showPostModal = false">&times;</span>
            <h2>Post</h2>
            <!-- Text area for writing the post content -->
            <textarea v-model="postContent" placeholder="Write your post here"></textarea>
            <!-- Button to submit the post -->
            <button @click="createPost()">Submit</button>
        </div>
    </div>

    <!-- Modal for viewing all posts -->
    <div v-if="showViewPostsModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="showViewPostsModal = false">&times;</span>
            <h2>View All Posts</h2>
            <!-- Add logic to display all posts -->
        <!-- make a table to display the posts -->
        <table>
          <tr>
            <th>Post</th>
            <th>Content</th>
          </tr>
          <!-- Loop through posts and display details -->
          <tr v-for="post in posts" :key="post.post_id">
            <td>{{ post.post_id }}</td>
            <td>{{ post.username}}</td>
            <!-- add time -->
            <td>{{ post.created_at }}</td>
            <td>{{ post.content }}</td>
          </tr>
        </table>
        </div>
    </div>

</template>

<script>

import axios from 'axios';
import { mapGetters } from 'vuex';


export default {
    // Importing computed properties from Vuex store
    computed: {
        ...mapGetters(['currentUser']),
        // Compute the user ID from currentUser
        userID() {
            return this.currentUser ? this.currentUser.userId : null;
        }
    },

    name: 'SocialMedia',
    data() {
        // Data properties for managing state
        return {
            
            showPostModal: false,
            postContent: '',
            showViewPostsModal: false,
            posts: [],  // Array to store all posts
        };
    },

    methods: {
        // Method to add friends
        addfriends() {
            // Add logic to show the add friends modal
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
                if (response.status === 200) {
                    console.log(response.data);
                    this.content = response.data;
                    console.log(this.content);
                }
                else {
                    console.error('Post not found.');
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
        getAllPosts(){
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
                }
                else {
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
            // Add logic to show the friend list modal
        },
        viewPosts() {
            // Add logic to show the view posts modal
        },
    },


}

// You can add your JavaScript logic here
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


table {
    width: 100%;
    border-collapse: collapse;
}

.posts-container {
    overflow-y: auto;
    /* Only vertical scrolling */
    max-height: 300px;
    /* Adjust based on your needs */
    margin-top: 20px;
    /* Space between header and table */
}

th,td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

/* Styles for close button */
.close {
  float: right;
  font-size: 28px;
  cursor: pointer;
}


/* Add other CSS styles to match the design of the second photo */
</style>
