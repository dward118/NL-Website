<template>
  <div>
    <div class="menu-container">
      <div class="menu-item">
        <router-link to="/">
          <div style="font-size: 30px; color: #fac62e; font-weight: bold">
            NucScholar
          </div>
        </router-link>
      </div>
      <div class="menu-item">
        <router-link to="/question">Ask a Question</router-link>
      </div>
      <div class="menu-item">
        <router-link to="/semantic">Search</router-link>
      </div>
      <div class="menu-item">
        <router-link to="/contact-us">Contact Us</router-link>
      </div>
      <div class="menu-item">
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <footer style="bottom: 0; position: fixed">
      NucScholar is a product of Lawrence Berkeley National Laboratory &trade;
      and The Air Force Institute of Technology &trade;
    </footer>
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
  name: "MenuBar",
};
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
