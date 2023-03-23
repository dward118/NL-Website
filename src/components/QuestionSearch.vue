<template>
    <MenuBar />

<!-- This is to create whitespace at the bottom until we have other containers. -->
<div style="height: 200px;"></div>
</template>
    
<script>
import MenuBar from './MenuBar.vue';

export default {
    name: 'QuestionSearch',

    components: {
        MenuBar
    },
}
</script>
    
<style></style>