<template>
  <MenuBar />
  <div class="field" style="margin-top: 130px">
    <p>
      This app will let you query a small database of arXiv articles on fission.
      The database consists of 71708 individual sentences automatically
      extracted from 108 articles.
    </p>
    <p>
      The search engine will attempt to return sentences from the database that
      are semantically related to your query.
    </p>

    <input v-model="SearchBar" placeholder="Ex: fission fragment detectors" />

    <button @click="Search">Submit</button>
  </div>
</template>

<script>
import MenuBar from "./MenuBar.vue";

export default {
  name: "SemanticSearch",

  components: {
    MenuBar,
  },
  data() {
    return {
      SearchBar: "",
    };
  },
  methods: {
    Search: function () {
      console.log(this.SearchBar);
    },
  },
};
</script>

<style scoped>
.field input {
  width: 500px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #fac62e;
}

.field button {
  width: 120px;
  height: 40px;
  border: 1px solid #00313c;
  background: #00313c;
  color: #fff;
  cursor: pointer;
}
</style>
