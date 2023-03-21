<template>
  <div>
    <MenuBarLimited />

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Sign Up</h1>
    <div class="field">
      <form @submit.prevent="submitForm">
        <input type="email" placeholder="Enter Your Email" id="email" name="email" required>
        <input type="text" placeholder="Enter Username" id="username" name="username" required />
        <input type="password" placeholder="Enter Password" id="password" name="password" required />
        <button type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { response } from 'express';
import MenuBarLimited from '../components/MenuBarLimited.vue';

export default {
  name: 'SignUp',

  components: {
    MenuBarLimited
  },
  data() {
    return {
      email: '',
      username: '',
      password: '',
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        email: this.email,
        username: this.username,
        password: this.password
      }

      axios
        .post('/api/v1/users/', formData)
        .then(response => {

          this.$router.push('/sign-in')
          console.log(response)
        })
        .catch(error => {
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
}
</style>