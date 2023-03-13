<template>
  <MenuBar />
</template>
  
<script>
import MenuBar from './MenuBar.vue';

export default {
  name: 'HomePage',

  components: {
    MenuBar
  },

  data() {
    return {
      activeItem: 'NucScholar',
    }
  },
}
</script>
  
<style></style>
  