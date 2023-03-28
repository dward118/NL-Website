<template>
  <MenuBar />

  <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Welcome 'USER'!</h1>

  <p class="greeting">
    Thank you for using the NucScholar website. <br><br>
    From this page, you can manage different aspects of your account such as: <br>
    -<a href="#container">Changing your password.</a><br>
    -Logging out.<br>
    -Toggle settings.<br>
    -View admin controls.<br><br>

    We appreciate your continued support!
  </p>

  <div class="logout" id="logout">
    <form @submit.prevent="logout">
      <button type="submit">Logout</button>
    </form>
    
  </div>

  <div class="container" style="background-color: #aaa;" id="container">
    <h2 style="color: #00313c; font-size: 30px;">Change your password</h2>
    <hr style="margin-bottom: 50px; border: 1px solid #00313c;">
    <input type="password" placeholder="Enter Password" v-model="password" autocomplete="current-password" required/>
    <input type="password" placeholder="Confirm Password" v-model="password" autocomplete="current-password" required/>
    <button type="submit">Change</button>
  </div>

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
      console.log("logout")
      axios
        .post('/api/v1/token/logout')
        .then(response => {

          this.$router.push('/login')
          console.log(response)

          this.$store.commit('removeToken')
          axios.defaults.headers.common['Authorization'] = ""
          localStorage.setItem('token', "")

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

.greeting {
  margin-top: 10rem;
  text-align: left;
  margin-left: 200px;
  line-height: 1.3;
  font-size: larger;
}

.container {
  margin: 300px auto 0px auto;
  width: 400px;
  height: 20rem;
  border: 1px solid #00313c;
  padding: 10px;
}

.container button {
  width: 250px;
  height: 30px;
  border: 1px solid #00313c;
  background: #00313c;
  color: #fff;
  cursor: pointer;
  margin-bottom: 10px;
}

.container input {
  display: block;
  margin: 10px auto 20px auto;
  border: 1px solid #00313c;
  width: 300px;
  height: 30px;
}

.logout button {
margin: 100px auto 10px auto;
width: 320px;
height: 40px;
border: 1px solid #00313c;
background: #00313c;
color: #fff;
cursor: pointer;
}
</style>
