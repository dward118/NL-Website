<template>
  <MenuBar />
  <h1 style="font-size:40px; color: #00313c; margin-top: 150px; margin-bottom: 80px;">Question Search</h1>
  <div class="field">
    <p>
      This app will let you query a small database of arXiv articles on fission.
      The database consists of 71708 individual sentences automatically <br>
      extracted from 108 articles. The search engine will attempt to return short phrases from the database
      that most closely answer your question.
    </p>

    <input
      v-model="SearchBar" style="margin-top: 50px;" placeholder="Ex: What model is used to calculate tunneling?"
    />

    <button @click="Search">Search</button>
  </div>

  <h1 style="color: #00313c; margin-top: 100px; margin-bottom: 30px; font-size: 35px;">Results</h1>
  <div class="qsearch-container">
    Search for results! <br>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
  <div class="leftLogo">
    <img src="frontend\src\assets\berkeley.png" alt="BerkelyLab"/>
  </div>
  <div class="rightLogo">
    <img src="frontend\src\assets\afit.png" alt="AFIT"/>
  </div>
</template>

<script>
import MenuBar from "../components/MenuBar.vue";

export default {
  name: "QuestionSearch",

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

.qsearch-container {
  margin-top: 150px;
  margin: 25px;
  width: 1000px;
  height: 500px;
  margin: 0 auto;
  border: 1px solid #00313c;
  padding: 10px;
}

.leftLogo {
  display: inline-block;
}

.rightLogo {
  display: inline-block;
}
</style>
