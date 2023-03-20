<template>
  <MenuBarLimited />
  <div class="semantic-search">
    <p>
      This app will let you query a small database of arXiv articles on fission.
      The database consists of 71708 individual sentences automatically
      extracted from 108 articles.
    </p>
    <p>
      The search engine will attempt to return sentences from the database that
      are semantically related to your query. For example, try: fission fragment
      detectors.
    </p>
    <input v-model="fullName" placeholder="Enter name" />
    <button @click="greet">Submit</button>
  </div>
</template>

<script>
import MenuBarLimited from "./MenuBarLimited.vue";

export default {
  name: "SemanticSearch",

  components: {
    MenuBarLimited,
  },
  data() {
    return {
      fullName: "",
    };
  },
  methods: {
    greet: function () {
      console.log("My name is: ", this.fullName);
    },
  },
};
</script>

<style>
.semantic-search {
  margin-top: 130px;
}
</style>
