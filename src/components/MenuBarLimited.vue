<template>
  <div>
    <div class="menu-container">
      <div class="menu-item"><router-link to="/">
          <div style="font-size: 30px; color: #fac62e; font-weight: bold;" onmouseover="this.style.color='aliceblue'"
            onmouseout="this.style.color='#fac62e'">NucScholar</div>
        </router-link></div>
    </div>
    <footer>
      <div class="footer-content">
        <p class="footerStyle">
          NucScholar is a product of Lawrence Berkeley National Laboaratory &trade;
          and The Air Force Institute of Technology &trade;
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'MenuBarLimited',
};
</script>

<style scoped>
/* Styles for the horizontal menu */
.menu-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #00313c;
  /*justify-content: space-between;*/
  display: flex;
  padding: 10px;
  overflow: hidden;
}

.menu-item {
  font-size: 18px;
  padding: 14px 40px;
  cursor: pointer;
  color: aliceblue;
}

.menu-item a {
  float: left;
  color: aliceblue;
  padding: 0px 30px;
  font-size: 18px;
  text-decoration: none;
}

.menu-item a:hover {
  color: #fac62e;
  text-decoration: none;
}

footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: #00313c;
  height: auto;
  width: 100vw;
  padding-top: 20px;
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