<template>
  <MenuBarLimited />
  <div style="margin-top: 130px">
    <p>
      This app will let you query a small database of arXiv articles on fission.
      The database consists of 71708 individual sentences automatically
      extracted from 108 articles.
    </p>
    <p>
      The search engine will attempt to return short phrases from the database
      that most closely answer your question. For example, try: what model is
      used to calculate tunneling?
    </p>
    <input v-model="fullName" placeholder="Enter name" />
    <button @click="greet">Submit</button>
  </div>
</template>

<script>
import MenuBarLimited from "./MenuBarLimited.vue";

export default {
  name: "QuestionSearch",

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

<style></style>
