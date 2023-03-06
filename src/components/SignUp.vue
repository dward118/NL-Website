<template>
    <div>
      <MenuBarLimited />
  
      <h1>Sign Up</h1>
      <div class="field">
        <input type="email" placeholder="Enter Your Email" id="email" name="email" required>
        <input type="text" placeholder="Enter Username" id="username" name="username" required />
        <input type="password" placeholder="Enter Password" id="password" name="password" required />
        <button type="submit">Submit</button>
      </div>
    </div>
  </template>

  <script>
  import MenuBarLimited from './MenuBarLimited.vue';

  export default {
    name: 'SignUp',

    components: {
      MenuBarLimited
    },

    data() {
      return {
        activeItem: 'Home',
      };
    },
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