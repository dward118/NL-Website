<template>
  <MenuBar />
  
  <a v-if="this.$store.state.isAuthenticated">

    <div class="dropdown" style="margin-left: 5px; float:left; top: 100px;">
      <button class="dropbtn">=</button>
      <div class="dropdown-content" style="left:0;">
        <a href="#">Settings</a>
        <a href="#">Admin</a>
        <a><router-link to="/change">Change Password</router-link></a>
        <a>
          <div class="logout" id="logout">
            <form @submit.prevent="logout">
              <button type="submit">Logout</button>
            </form>
          </div>
        </a>
      </div>
    </div>

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Welcome {{ this.$store.state.username }}!</h1>

    <p class="greeting">
      Thank you for using the NucScholar website. <br><br>
      From this page, you can manage different aspects of your account such as: <br>
      -Changing your password.<br>
      -Logging out.<br>
      -Toggle settings.<br>
      -View admin controls.<br><br>

      We appreciate your continued support!
    </p>

  </a>
  <a v-else>
    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Welcome Guest!</h1>

    <p class="greeting">
      You shouldn't be here...
    </p>
  </a>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>
import axios from 'axios';
import MenuBar from '../components/MenuBar.vue';

export default {
  name: 'HomePage',

  components: {
    MenuBar
  },
  methods: {
    logout(e) {
      const formData = {
        refresh: this.$store.state.refresh
      }

      console.log(formData)
      axios
        .post('/api/token/logout/', formData)
        .then(response => {
          console.log(response)

          this.$store.commit('removeToken')

          this.$router.push('/')

        })
        .catch(error => {
          console.error(error)
          console.error(e)
        })
    }
  }
}

</script>

<style>
.dropbtn {
  background-color: #c9d0d1;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

.dropdown {
  position: fixed;
}

.dropdown-content {
  display: none;
  position: fixed;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #00313c;
}

.greeting {
  margin-top: 10rem;
  text-align: left;
  margin-left: 200px;
  line-height: 1.3;
  font-size: larger;
}

.logout button {
  color: black;
  width: 200px;
  height: 40px;
  background-color: #f1f1f1;
  cursor: pointer;
}
</style>
