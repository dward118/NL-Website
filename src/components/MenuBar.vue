<template>
    <div>
  
      <div class="menu-container">
        <div class="title">NucScholar</div>
          <div class="menu-item" :class="{'active': activeItem === 'Home'}" @click="activeItem = 'Home'">Home</div>
        <div class="divider"></div>
        <div class="menu-item" :class="{'active': activeItem === 'Ask a Question'}" @click="activeItem = 'Ask a Question'">Ask a Question</div>
        <div class="divider"></div>
        <div class="menu-item" :class="{'active': activeItem === 'Search'}" @click="activeItem = 'Search'">Search</div>
        <div class="divider"></div>
          <div class="menu-item" :class="{'active': activeItem === 'Contact Us'}" @click="activeItem = 'Contact Us'">Contact Us</div>
        <div class="divider"></div>
          <div class="menu-item" :class="{'active': activeItem === 'My Account'}" @click="activeItem = 'My Account'">My Account</div>
      </div>
  
      </div>
    </template>

    <script>
    export default {
      name: 'MenuBar',
  
      data() {
        return {
          activeItem: 'Home'
        }
      },
    }
    </script>
    
    <style scoped>
    /* Styles for the horizontal menu */
  .menu-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
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
  
  /* Style for the divider */
  .divider {
    height: 1px;
    width: 10px;
    background-color: #ccc;
    margin-left: 10px;
    margin-right: 10px;
  }
  
  /* Style for the title */
  .title {
    font-size: 24px;
    font-weight: bold;
    margin-right: 20px;
  }
    </style>