<template>
  <div>
    <MenuBar />
    <u>
      <h1 style="font-size:40px; color: #00313c; margin-top: 150px; margin-bottom: 100px;">Contact Us</h1>
    </u>
    <form ref="form" @submit.prevent="sendEmail" class="field">
      <input type="text" placeholder="Enter Your First Name" name="firstName" required autocomplete="given-name">
      <input type="text" placeholder="Enter Your Last Name" name="lastName" required autocomplete="family-name">
      <input type="email" placeholder="Enter Your Email" name="email" required autocomplete="email">
      <input type="text" placeholder="Enter Subject Line" name="subject" required>
      <textarea placeholder="Body" id="body" name="body" required></textarea>
      <button type="submit">Send</button>
    </form>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>

import emailjs from '@emailjs/browser';
import MenuBar from '../components/MenuBar.vue';

export default {
  name: 'ContactUs',

  components: {
    MenuBar
  },

  methods: {
    sendEmail() {
      /*
        this needs to be completely reworked, yes you can keep using emailjs.
        However the problem with this is that its a paid service and you have a backend.
        There's a better way to hook this up or you could keep using emailjs and hook up the parametters again.
      */
      emailjs.sendForm('service', 'template', this.$refs.form, '')
        .then((result) => {
          console.log('SUCCESS!', result.text);
          this.$router.push('/')
        }, (error) => {
          console.log('FAILED...', error.text);
        });
    }
  }
}
</script>

<style>
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

.field textarea {
  width: 300px;
  height: 100px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #fac62e;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
