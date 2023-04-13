<template>
  <MenuBar />

  <div>
    <h3 style="font-size:40px; color: #00313c; margin-top: 150px; margin-bottom: 80px;">NucScholar Search Engine</h3>
    <p>
      Created by Walid Younes and Bethany Goldblum at the <a href="https://www.lbl.gov/">Lawrence Berkeley National Laboratory</a> and Juan Manfredi at the
      <a href="https://www.afit.edu/">Air Force Institute of Technology.</a> Please report any problems to Walid Younes.
    </p>
    <p>
      The NucScholar project uses Natural Language Processing (NLP) to automatically retrieve, categorize, and recommend
      nuclear science papers. The goal of this effort is to provide the groundwork for a shift to a fully automated
      workflow for nuclear science literature searches, enabling increased efficiency in the nuclear data pipeline and
      accelerating data throughput for a wide range of applications.
    </p>
    <p>
      Additional information about the project can be found <a href="https://nucscholar.berkeley.edu/">here</a>, along with a listing of all <a href="https://nucscholar.berkeley.edu/our-team/">project team members.</a>
    </p>
    <p>
      The NucScholar project is supported by the <a href="https://www.energy.gov/science/office-science">U.S. Department of Energy/Office of Science</a>
    </p>
  </div>

  <h1 style="color: #fac62e; margin-top: 75px; margin-bottom: 30px; font-size: 35px;">News</h1>
  <div class="news-container">
    No scheduled maintenance. <br>
  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>
  
<script>
import MenuBar from '../components/MenuBar.vue';

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
  line-height: 1.3;
}

.news-container {
  margin-top: 150px;
  margin: 25px;
  width: 1000px;
  height: 300px;
  margin: 0 auto;
  border: 1px solid #fac62e;
  padding: 10px;
}
</style>
