<template>
  <div>
    <MenuBar />

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Login</h1>
    <div class="field">
      <form @submit.prevent="submitForm" autocomplete="on">
        <input type="text" placeholder="Enter Username"     v-model="username" autocomplete="username" required/>
        <input type="password" placeholder="Enter Password" v-model="password" autocomplete="current-password" required/>
        <button type="submit">Login</button>
      </form>
      <p>
        <router-link to="/sign-up">Don't have an account? Sign up here.</router-link>
      </p>
      <p>
        <router-link to="/sign-up">Forgot Password?</router-link>
      </p>
    </div>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>
import axios from 'axios';
import MenuBar from '../components/MenuBar.vue';

export default {
  name: 'LoginPage',

  components: {
    MenuBar
  },
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password
      }

      axios
        .post('/api/v1/token/login', formData)
        .then(response => {
          console.log(response)

          const token = response.data.auth_token
          this.$store.commit('setToken', token)
          axios.defaults.headers.common['Authorization'] = "Token " + token
          localStorage.setItem('token', token)

          this.$router.push('/')
          
        })
        .catch(error => {
          console.error(e)
          console.error(error)

        })
    }
  }
};
</script>

<style scoped>
.field input {
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #fac62e;
}

.field button {
  width: 320px;
  height: 40px;
  border: 1px solid #00313c;
  background: #00313c;
  color: #fff;
  cursor: pointer;
  margin-bottom: 10px;
}

p {
  text-align: center;
}
</style>
