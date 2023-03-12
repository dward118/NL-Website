<template>
  <div>
    <MenuBarLimited />

    <div>
      <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Contact Us</h1>
      <div class="field">
        <input type="text" placeholder="Enter Your First Name" id="first-name" name="firstName" required>
        <input type="text" placeholder="Enter Your Last Name" id="last-name" name="lastName" required>
        <input type="email" placeholder="Enter Your Email" id="email" name="email" required>
        <input type="text" placeholder="Enter Subject Line" id="subject" name="subject" required>
        <textarea placeholder="Body" id="body" name="body" required></textarea>
        <button type="submit">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import MenuBarLimited from './MenuBarLimited.vue';

export default {
  name: 'ContactUs',

  components: {
    MenuBarLimited
  },

  data() {
    return {
      activeItem: 'NucScholar',
    }
  },
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
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #fac62e;
}
</style>