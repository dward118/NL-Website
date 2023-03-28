<template>
  <router-view />
</template>

<script>
import axios from 'axios'
// import store from './store'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if ( token ) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
  
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
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
body{
  padding: 0;
  margin: 0;
}
</style>
