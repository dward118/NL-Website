<template>
  <div class="menu-item">
    <a><router-link to="/" style="font-size: 30px; color: #fac62e; font-weight: bold;"
        onmouseover="this.style.color='aliceblue'" onmouseout="this.style.color='#fac62e'">NucScholar</router-link></a>
    <a><router-link to="/question">Ask a Question</router-link></a>
    <a><router-link to="/semantic">Search by Meaning</router-link></a>
    <a><router-link to="/contact-us">Contact Us</router-link></a>
    <a v-if="this.$store.state.isAuthenticated">
      <router-link to="/login">My Account</router-link>
    </a>
    <a v-else>
      <router-link to="/login">Login</router-link>
    </a>
  </div>
  <footer>
    <p class="footerStyle">
      NucScholar is a product of Lawrence Berkeley National Laboratory &trade;
      and The Air Force Institute of Technology &trade;
    </p>
  </footer>
</template>

<script>
export default {
  name: 'MenuBar',
}
</script>

<style scoped>
/* Styles for the horizontal menu */
.menu-item {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #00313c;
  overflow: hidden;
  border: 2px solid#fac62e;
}

.menu-item a {
  float: left;
  color: aliceblue;
  text-align: center;
  padding: 14px 16px;
  font-size: 18px;
  text-decoration: none;
  margin-right: 10px;
}

.menu-item a:hover {
  color: #fac62e;
}

footer {
  position: fixed;
  bottom: 0;
  left: 0;
  background: #00313c;
  height: fit-content;
  width: 100vw;
  border: 2px solid#fac62e;
}

.footerStyle {
  color: aliceblue;
  text-align: center;
  font-size: small;
}
</style>
