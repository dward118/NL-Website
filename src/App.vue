<template>
  <HomePage />
  <LoginPage />
  <ContactUs />
  <SignUp />
</template>

<script>
//import HomePage from './components/Homepage.vue'
//import LoginPage from './components/LoginPage.vue'
import ContactUs from './components/ContactUs.vue'
//import SignUp from './components/SignUp.vue'

export default {
  name: 'App',
  components:{
    //HomePage,
    //LoginPage,
    ContactUs,
    //SignUp,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
