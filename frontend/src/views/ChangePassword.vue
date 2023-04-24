<template>
  <div>
    <MenuBar />

    <div class="container" style="background-color: #c9d0d1;" id="container">
      <h2 style="color: #00313c; font-size: 30px;">Change your password</h2>
      <hr style="margin-bottom: 20px; border: 1px solid #00313c;">
      <input type="password" placeholder="Enter Your Old Password" v-model="password" autocomplete="current-password"
        required />
      <input type="password" placeholder="Enter Your New Password" v-model="password" autocomplete="current-password"
        required />
      <input type="password" placeholder="Confirm New Password" v-model="password" autocomplete="current-password"
        required />
      <button type="submit">Change</button>
    </div>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>
  
<script>
import MenuBar from '../components/MenuBar.vue';

export default {
  name: 'ChangePassword',

  components: {
    MenuBar
  },
}
</script>
  
<style scoped>
.container {
  margin: 250px auto 0px auto;
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
</style>