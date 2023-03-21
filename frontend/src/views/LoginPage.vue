<template>
  <div>
    <MenuBarLimited />

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Login</h1>
    <div class="field">
      <input type="text" placeholder="Enter Username" id="username" name="username" required />
      <input type="password" placeholder="Enter Password" id="password" name="password" required />
      <button type="submit">Log in</button>
      <p>
        <router-link to="/sign-up">Don't have an account? Sign up here.</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import MenuBarLimited from '../components/MenuBarLimited.vue';

export default {
  name: 'LoginPage',

  components: {
    MenuBarLimited
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
