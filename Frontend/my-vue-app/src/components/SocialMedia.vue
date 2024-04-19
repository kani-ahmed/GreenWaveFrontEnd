<template>
    <div class="social-media-component">


        <main>
            <div class="button-class">
                <div class="button-group-top">
                    <button class="square-button" @click="addfriends">Add Friends</button>
                    <button class="square-button" @click="openPostModal()">Create Post</button>
                    <button class="square-button" @click="openSendMessage()">Send Message</button>
                </div>
                <div class="button-group-bottom">
                    <button class="square-button" @click="Friends">Friend List</button>
                    <button class="square-button" @click="viewPosts">view posts</button>
                </div>
            </div>
        </main>
    </div>

    <div v-if="showPostModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="showPostModal = false">&times;</span>
            <h2>Post</h2>
            <textarea v-model="postContent" placeholder="Write your post here"></textarea>
            <button @click="createPost()">Submit</button>
        </div>
    </div>

            <!-- Add Friends -->
    <div v-if="showAddFriendModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="showAddFriendModal = false">&times;</span>
            <h2>Add Friends</h2>
            <input type="text" v-model="searchQuery" placeholder="Search users..." @keyup.enter="searchUsers">
            <button @click="searchUsers">Search</button>
            <ul class="friend-search-results">
                <li v-for="user in searchResults" :key="user.id">
                    {{ user.username }}
                    <button @click="sendFriendRequest(user.id)">Add</button>
                </li>
            </ul>
        </div>
    </div>


</template>

<script>

import axios from 'axios';
import { mapGetters } from 'vuex';


export default {
    computed: {
        ...mapGetters(['currentUser']),
        // Use a computed property to react to changes in currentUser
        userID() {
            return this.currentUser ? this.currentUser.userId : null;
        }
    },

    name: 'SocialMedia',
    data() {
        return {

            showPostModal: false,
            postContent: '',
            

        };
    },

    methods: {
        addfriends() {
            // Add logic to show the add friends modal
            if (!this.userID) {
                console.error('Id is empty');
                return;
            }

        },

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
                }
                else {
                    console.error('Post not found.');
                }
            })
                .catch(error => {
                    console.error("Error:", error.response);
                });
        },

        openPostModal() {
            this.showPostModal = true;
        },

        sendMessage() {
            // Add logic to show the send message modal
        },

        openSendMessage() {
            this.showSendMessageModal = true;
        },

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

.modal-content {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 80%;
    max-width: 600px;
}


/* Add other CSS styles to match the design of the second photo */
</style>
