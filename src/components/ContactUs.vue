<template>
<div>
  <MenuBarLimited />

  <div>
    <h1>Contact Us</h1>
    <form ref="form" @submit.prevent="sendEmail" class="field">
      <input type="text" placeholder="Enter Your First Name" name="firstName" required autocomplete="given-name">
      <input type="text" placeholder="Enter Your Last Name" name="lastName" required autocomplete="family-name">
      <input type="email" placeholder="Enter Your Email" name="email" required autocomplete="email">
      <input type="text" placeholder="Enter Subject Line" name="subject" required>
      <textarea placeholder="Body" id="body" name="body" required></textarea>
      <button type="submit">Send</button>
    </form>  
  </div>
</div>
</template>

<script>
import emailjs from '@emailjs/browser';
import MenuBarLimited from './MenuBarLimited.vue';

export default {
  name: 'ContactUs',

  components: {
    MenuBarLimited
  },

  data() {
    return {
      activeItem: 'Home',
    }
  },

  methods: {
    sendEmail() {
      emailjs.sendForm('service_v4pdofo', 'template_dvtn57k', this.$refs.form, 'VFoCuA7pmsGIFz8Ml')
        .then((result) => {
            console.log('SUCCESS!', result.text);
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
  border: 1px solid skyblue;
}

.field textarea {
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid skyblue;
}

.field button {
  width: 320px;
  height: 40px;
  border: 1px solid skyblue;
  background: skyblue;
  color: #fff;
  cursor: pointer;
}
</style>
