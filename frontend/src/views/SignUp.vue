<template>
  <div>
    <MenuBar />

    <u>
      <h1 style="font-size:40px; color: #00313c; margin-top: 150px; margin-bottom: 100px;">Sign Up</h1>
    </u>
    <div class="field">
      <form @submit.prevent="submitForm" autocomplete="on">
        <div class="leftBound">
          <input type="text" placeholder="First Name" v-model="first_name" autocomplete="given-name" required />
          <input type="text" placeholder="Username" v-model="username" autocomplete="username" required />
          <input type="password" placeholder="Password" v-model="password" autocomplete="new-password" required />
        </div>
        <div class="rightBound">
          <input type="text" placeholder="Last Name" v-model="last_name" autocomplete="family-name" required />
          <input type="email" placeholder="Email" v-model="email" autocomplete="email" required />
          <input type="text" placeholder="Institution" v-model="institution" autocomplete="organization" required />
        </div>
        <select name="experience" v-model="experience" required>
          <option value="" disabled selected hidden>Select Your Experience</option>
          <option value="1">Undergraduate</option>
          <option value="2">Graduate</option>
          <option value="3">Postdoctoral</option>
          <option value="4">Junior Staff/Faculty</option>
          <option value="5">Staff/Faculty</option>
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

import MenuBar from '../components/MenuBar.vue';

export default {
  name: 'SignUp',

  components: {
    MenuBar
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      username: "",
      email: "",
      password: "",
      institution: "",
      experience: ""
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        email: this.email,
        password: this.password,
        institution: this.institution,
        experience: this.experience,
      }

      axios
        .post('/api/register', formData)
        .then(response => {
          console.log(response)
          this.$router.push('/login')
        })
        .catch(error => {
          console.error(error)
          console.error(e)
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

.leftBound {
  display: inline-block;
  margin-right: 5px;
}

.rightBound {
  display: inline-block;
  margin-left: 5px;
}

p {
  text-align: center;
}</style>
