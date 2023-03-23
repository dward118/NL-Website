<template>
  <div>
    <MenuBar />

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Sign Up</h1>
    <div class="field">
      <form @submit.prevent="submitForm">
        <input type="email" placeholder="Enter Your Email" name="email" v-model="email" required>
        <input type="text" placeholder="Enter Username" name="username" v-model="username" required />
        <input type="password" placeholder="Enter Password" name="password" v-model="password" required />
        <input type="text" placeholder="Enter Your Institution" name="institution" v-model="institution" required />
        <select name="experience" v-model="experience" required>
          <option value="" disabled selected hidden>Select Your Experience</option>
          <option value="grad">Grad</option>
          <option value="undergrad">Undergrad</option>
          <option value="professor">Professor</option>
          <option value="adjunct">Adjunct</option>
        </select>
        <button type="submit">Submit</button>
      </form>
      <p>
        <router-link to="/login">Back to Login</router-link>
      </p>
    </div>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>
import axios from 'axios'
// import { response } from 'express';
import MenuBar from '../components/MenuBar.vue';

export default {
  name: 'SignUp',

  components: {
    MenuBar
  },
  data() {
    return {
      email: '',
      username: '',
      password: '',
      institution: '',
      experience: '',
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        // first_name: "testname",
        // last_name: "lastname",
        email: this.email,
        username: this.username,
        password: this.password,
        institution: this.institution,
        experience: this.experience
      }

      console.log(formData)

      axios
        .post('/api/v1/users/', formData)
        .then(response => {

          this.$router.push('/sign-in')
          console.log(response)
        })
        .catch(error => {
          console.log(error)
          console.log(e)
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

.field select {
  width: 325px;
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

p {
  text-align: center;
}
</style>
