<!-- #SPDX-License-Identifier: MIT -->
<template>
  <d-container fluid>
    <div id="overview">
        <h3>What is <span>Augur</span>?</h3>
        <p>
        Augur is a software suite for collecting and measuring structured data about free and open-source software (FOSS) communities.
        We gather trace data for a group of repositories, normalize it into our data model, and provide a variety of metrics about said data. 
        The structure of our data model enables us to synthesize data across various platforms to provide meaningful context for meaningful questions about 
        the way these communities evolve.
        We are a CHAOSS project, and many of our metrics are implementations of the metrics defined by our awesome community. You can find more information 
        about how to get involved on the CHAOSS website.
        </p>
    </div>

    <div id="bySection">
        <h3 id="tabLabel">What does each tab do?</h3>
        <div class ="row">
          <div class="col">
            <h5>Insights</h5>
            <p>
              This tab shows you a list of the most anomalous of insights about different repos in the group. It displays a chart showing the anomalous data.
              You can click on the repo name to see an overview of all of that repo's metrics. You can also click on Evolution or Risk to see those specific
              metrics for the repo associated.
            </p>
          </div>
          <div class="col">
            <h5>Repos</h5>
            <p>
              This tabs displays a list of the repos within the group that is stored. It displays the repo's URL, group name, total commit count, and total issue
              count. You can click on the repo's URL to be directed to the repo.
            </p>
          </div>
          <div class="col">
            <h5>Groups</h5>
            <p>
              This tab shows you a list of the repo groups you have stored. The table shows the name, description, website, last modified, and type. You can
              click on the group name to be directed to the repos page which will list all of the repos in that group.
            </p>
          </div>
        </div>
    </div>
  </d-container>
</template>

<script>
export default {
  name: 'about',
  components: {
  },
  data() {
    return {
    };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@500&family=Ubuntu:wght@700&display=swap');

body {
  font-family: 'Rubik', sans-serif;
}

span{
    color: #1E90FF;
    font-family: 'Rubik', sans-serif;
}

#overview {
  text-align: center;
}

#bySection {
  text-align: center;
  margin-top: 2em;
}

h3 {
  margin: 2em;
  margin-bottom: 1em;
  font-family: 'Rubik', sans-serif;
}

h3#tabLabel {
  margin-top: 5em;
}

h5 {
  font-family: 'Rubik', sans-serif;
}

p {
  margin: 2em;
  font-family: 'Rubik', sans-serif;
}

</style>