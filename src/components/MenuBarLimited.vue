<template>
    <div>
  
      <div class="menu-container">
        <div class="title">NucScholar</div>
          <div class="menu-item" :class="{'active': activeItem === 'Home'}" @click="activeItem = 'Home'">Home</div>
      </div>
    </div>
  </template>

  <script>
export default {
  name: 'MenuBarLimited',
  data() {
    return {
      activeItem: 'Home',
    };
  },
};
</script>

<style scoped>

/* Styles for the horizontal menu */
.menu-container {
  position: fixed;
  top: 0;
  left: 0;
  background-color: #0000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}
.menu-item {
  margin-left: 10px;
  font-size: 18px;
  cursor: pointer;
}

/* Style for the active menu item */
.active {
  color: #4CAF50;
  font-weight: bold;
}

/* Style for the title */
.title {
  font-size: 24px;
  font-weight: bold;
  margin-right: 20px;
}
</style>