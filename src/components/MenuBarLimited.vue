<template>
  <div>
    <div class="menu-container">
      <div class="menu-item"><router-link to="/">
          <div style="font-size: 30px; color: #fac62e; font-weight: bold;">NucScholar</div>
        </router-link></div>
      <footer style="bottom: 0; position: fixed;">NucScholar is a product of Lawrence Berkeley National Laboaratory
        &trade; and The Air Force Institute of Technology &trade;</footer>
    </div>
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
}</style>