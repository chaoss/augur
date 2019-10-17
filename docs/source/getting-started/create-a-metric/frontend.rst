--------------------------------------
Build a Visualization
--------------------------------------

The rest of the process can be found in the frontend doc_.

.. _doc: frontend.html

.. 3.   example file 3: 'augurAPI.js' in the ``augur/frontend/app/`` directory needs to have the the metric from ``routes.py`` mapped to an API endpoint that the frontend will then access.


..    * Metrics from the facade.py that take a git url should go under the //GIT section in this file
..    * Most of your metrics are going to belong in the //GROWTH, MATURITY AND DECLINE section.

.. .. code-block:: javascript
..    :linenos:

..      // IN THIS SECTION of augurAPI.js DEVELOPER NOTE

..      if (repo.owner && repo.name) {
..       // DIVERSITY AND INCLUSION
..       // GROWTH, MATURITY, AND DECLINE

..       // FIND THE RIGHT SECTION, like "GROWTH, MATURITY AND DECLINE" and ADD YOUR code
..       Timeseries(repo, 'closedIssues', 'issues/closed')
..       Timeseries(repo, 'closedIssueResolutionDuration', 'issues/time_to_close')
..       Timeseries(repo, 'codeCommits', 'commits')
..       // Timeseries(repo, 'codeReviews', 'code_reviews')

..       // THIS IS THE NEW METRIC IN OUR EXAMPLE
..       Timeseries(repo, 'codeReviewIteration', 'code_review_iteration')
..      }


.. 4. Example file 4: `ExperimentalCard.vue` in the `augur/frontend/app/components/` directory. We will need to import and insert a chart component that we will be creating next or a chart component that already exists in the `augur/frontend/app/components/charts/ ` directory.

..       In the `<script>` section of `ExperimentalCard.vue`, we must import the chart file and add it to the `components` section under `module.exports` like this:

.. .. code-block::
..    :linenos:

..       import ExampleChart from `./charts/ExampleChart`

..       import DynamicLineChart from './charts/DynamicLineChart'
..       import BubbleChart from './charts/BubbleChart'
..       import StackedBarChart from './charts/StackedBarChart'
..       import DualAxisContributions from './charts/DualAxisContributions'

..       module.exports = {
..         data() {
..           return {
..             colors: ["#FF3647", "#4736FF","#3cb44b","#ffe119","#f58231","#911eb4","#42d4f4","#f032e6"]
..           }
..         },
..         components: {
..           ExampleChart,

..           DynamicLineChart,
..           BubbleChart,
..           StackedBarChart,
..           DualAxisContributions
..         }
..       }


.. **TODO** Can we keep the example from above in place?


.. 5. Example file 5: **TODO** <\ :raw-html-m2r:`<FILL IN FILE NAME and PATH>`\ > We insert the ``ExampleChart`` component with our endpoint name (\ ``closedIssues``\ ) defined as the ``source`` property (prop) of the component (Vue converts a string name like 'ExampleChart' to 'example-chart' to be used as an html tag):

.. .. code-block:: html
..    :linenos:


..       <example-chart source="closedIssues"
..                           title="Closed Issues / Week "
..                           cite-url=""
..                           cite-text="Closed Issues">
..       </example-chart>


.. 6. You will need to create a chart file. **TODO** << Where? What will it be called? What example are we using? >> Here is an example of a chart file that calls the endpoint that is passed as the ``source`` property. The template section holds the vega-lite tag that renders the chart. The Vega-lite ``spec`` is being bound to what is being returned by the ``spec()`` method inside the ``computed`` properties (\ ``:spec="spec"``\ ), and the ``data`` being used for the chart is bound to the ``values`` array being returned by the ``data()`` method (\ ``:data="values"``\ ):

.. **TODO** Where it goes in this file. Same file?

.. .. code-block:: html
..    :linenos:

..       <template>
..         <div ref="holder" style="position: relative; z-index: 5">
..           <div class="chart">
..             <h3 style="text-align: center">{{ title }}</h3>
..             <vega-lite :spec="spec" :data="values"></vega-lite>
..             <p> {{ chart }} </p>
..           </div>
..         </div>
..       </template>

.. **TODO** Where it goes in this file. Same file?

.. .. code-block:: javascript
..    :linenos:

..       import { mapState } from 'vuex'
..       import AugurStats from 'AugurStats'

..       export default {
..         props: ['source', 'citeUrl', 'citeText', 'title', 'disableRollingAverage', 'alwaysByDate', 'data'],
..         data() {
..           return {
..             values: [],
..           }
..         },
..         computed: {
..           repo() {
..             return this.$store.state.baseRepo
..           },
..           spec() {
..               // IF YOU WANT TO CALL YOUR ENDPOINT IN THE CHART FILE, THIS IS WHERE/HOW YOU SHOULD DO IT:
..             let repo = window.AugurAPI.Repo({ githubURL: this.repo })
..             repo[this.source]().then((data) => {
..                // you can print your data in a console.log() to make                   // sure the endpoint is returning what it needs to
..               // console.log("HERE", data)
..               this.values = data
..             })
..             //FINISH CALLING ENDPOINT

..             // THIS IS A SAMPLE 'spec', SPECS ARE WHAT CREATE THE VEGA-LITE FILE,
..             // YOU CAN PLAY WITH SAMPLE SPEC OF A LINE CHART AT:
..             // https://vega.github.io/editor/#/examples/vega-lite/line
..             // AND SEE THE DATA THAT THEY ARE USING AT:
..             // https://vega.github.io/vega-lite/data/stocks.csv
..             let config = {
..               "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
..               "width": 950,
..               "height": 300,
..               "mark": "line",
..               "encoding": {
..                 "x": {
..                   "field": "date", "type": "temporal",
..                 },
..                 "y": {
..                   "field": "value","type": "quantitative",
..                 },
..               }
..             }
..             return config
..           }
..         },
..         methods: {
..           //define any methods you may need here
..           //you can call them anywhere with: this.methodName()
..         }
..       }
