<template>
  <div class="menu-item">
    <a><router-link to="/" style="font-size: 30px; color: #fac62e; font-weight: bold;"
        onmouseover="this.style.color='aliceblue'" onmouseout="this.style.color='#fac62e'">NucScholar</router-link></a>
  </div>
  <footer>
    <div class="footer-content">
      <p class="footerStyle">
        NucScholar is a product of Lawrence Berkeley National Laboaratory &trade;
        and The Air Force Institute of Technology &trade;
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'MenuBarLimited',
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
}

.menu-item a {
  float: left;
  color: aliceblue;
  text-align: center;
  padding: 14px 16px;
  font-size: 18px;
  text-decoration: none;
  margin-right: 5px;
}

.menu-item a:hover {
  color: #fac62e;
}

footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #00313c;
  height: fit-content;
  width: 100vw;
  padding-top: 10px;
  color: aliceblue;
  font-size: large;
}

footer-content {
  text-align: center;
  align-items: center;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.footerStyle {
  text-align: center;
}
</style>