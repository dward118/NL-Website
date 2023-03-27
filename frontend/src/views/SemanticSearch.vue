<template>
  <MenuBar />
  <h1 style="font-size:40px; color: #00313c; margin-top: 150px; margin-bottom: 80px;">Semantic Search</h1>
  <div class="field">
    <p>
      This app will let you query a small database of arXiv articles on fission.
      The database consists of 71708 individual sentences automatically <br>
      extracted from 108 articles. The search engine will attempt to return sentences from the database that
      are semantically related to your query.
    </p>

    <input v-model="SearchBar" style="margin-top: 50px;" placeholder="Ex: Fission fragment detectors" />

    <button @click="Search">Search</button>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>
import MenuBar from "../components/MenuBar.vue";

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

p {
  text-align: center;
  line-height: 1.3;
}
</style>
