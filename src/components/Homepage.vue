<template>
  <MenuBar />

  <div>
    <h3 style="font-size:40px; color: #00313c; margin-top: 150px;">NucScholar Search Engine</h3>
    <p>
      Created by Walid Younes and Bethany Goldblum at the Lawrence Berkeley National Laboratory and Juan Manfredi at the
      Air Force Institute of Technology. Please report any problems to Walid Younes.
    </p>
    <p>
      The NucScholar project uses Natural Language Processing (NLP) to automatically retrieve, categorize, and recommend
      nuclear science papers. The goal of this effort is to provide the groundwork for a shift to a fully automated
      workflow for nuclear science literature searches, enabling increased efficiency in the nuclear data pipeline and
      accelerating data throughput for a wide range of applications.
    </p>
    <p>
      Additional information about the project can be found here, along with a listing of all project team members.
    </p>
    <p>
      The NucScholar project is supported by the U.S. Department of Energy/Office of Science.
    </p>
  </div>

  <h1 style="color: #fac62e; margin-top: 75px; margin-bottom: 100px;">News</h1>
  <div class="news-container">
    No news to display. Check back later!
  </div>
</template>
  
<script>
import MenuBar from './MenuBar.vue';

export default {
  name: 'HomePage',

  components: {
    MenuBar
  },
}
</script>
  
<style>
p {
  text-align: left;
  margin-left: 20px;
}

.news-container {
  margin-top: 150px;
  margin: 25px;
  width: 1000px;
  height: 500px;
  margin: 0 auto;
  border: 1px solid;
  border-color: #fac62e;
}
</style>
  