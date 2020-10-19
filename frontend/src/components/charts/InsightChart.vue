<!-- #SPDX-License-Identifier: MIT -->
<template>
  <div ref='holder' class='insightChartSpinnerHolder'>
    <spinner v-if='loading' class='insightChartSpinner'></spinner>
    <vega-lite v-if='!loading' :spec='spec(vegaSpec)' :data='values' center='true' id='vegaChart'></vega-lite>
  </div>
</template>

<script>
import Spinner from '../Spinner.vue';
import vegaEmbed from 'vega-embed';
import axios from 'axios';

export default {
  props: ['url', 'metric', 'repo_id', 'title', 'color', 'repo_group_id'],
  components: {
    Spinner
  },
  data() {
    return {
      values: [],
      user: null,
      loading: true,
      errored: false,
      vegaSpec: null
    };
  },
  mounted() {
    let today = new Date()
    axios.get(`http://localhost:5000/api/unstable/repo-groups/${this.repo_group_id}/repos/${this.repo_id}/${this.metric}?begin_date=${today.getFullYear() - 1}-${today.getMonth()}-${today.getDate()}`).then(response => {
    // axios.get(this.baseURL + "/repo-group/${repo-group-id}/repo-id/${repo-id}/${metric}").then(response => {
      this.values = this.convertKey(response['data'])
      this.calculateVegaSpec();
      this.loading = false
    }).catch(error => {
      console.log("InsightChart error: ", error)
      this.errored = true
      this.loading = false
    }).finally(() => this.loading = false)
    
    
    this.$nextTick(() => {
      window.onresize = this.calculateVegaSpec;
    });
  },
  computed: {
    earliest() {
      if (!this.values[0]) return null;
      let date = new Date(this.values[0].date);
      date.setYear(2020);
      return date
    },
    latest() {
      return this.values[0] ? new Date(this.values[this.values.length - 1].date) : null;
    }
  },
  methods: {
    spec(vegaSpec) {
      vegaEmbed('#vegaChart', vegaSpec, {
        mode: 'vega-lite',
        tooltip: false
      });
      return vegaSpec;
    },
    calculateVegaSpec() {
      let specWidth = this.$refs.holder.clientWidth * 0.75;
      let specHeight = this.$refs.holder.clientHeight * 0.75;

      this.includeNullDates();
      this.vegaSpec = {
        $schema: "https://vega.github.io/schema/vega-lite/v2.json",
        center: true,
        width: specWidth, //263.7,
        height: specHeight, //166,
        padding: {left: 0, top: specHeight * .1, right: 0, bottom: 0},
        data: {values: this.values},
        layer: [
          {
            mark: {
              type: 'line',
              interpolate: 'basis'
            },
            encoding: {
              x: {
                field: 'date',
                type: 'temporal',
                axis: {grid: false, title: false, format: '%b %d'}
              },
              y: {
                field: 'value',
                type: 'quantitative',
                axis: {grid: false, title: false, ticks: false}
              },
              color: {value: this.color}
            }
          },
        ]
      };
      vegaEmbed('#vegaChart', this.vegaSpec, {
        mode: 'vega-lite'
      });
      this.loading = false;
    },
    convertKey(ary) {
      ary.forEach(el => {
        let keys = Object.keys(el);
        let field = null;
        keys.forEach(key => {
          if (el[key] != null && key != 'date' && key != 'repo_name') {
            field = key;
          }
        });
        el['value'] = el[field];
        el['field'] = field;
      });
      return ary;
    },
    includeNullDates() {
      for (let date = new Date(this.values[0].date); date > (new Date(this.values[this.values.length - 1].date).setYear(2018)); date.setDate(date.getDate() - 1)) {
        this.values.unshift({'date': date, 'test': 1})
      }
    }
  }
};
</script>

<style scoped>
  .insightChartSpinnerHolder {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    position: absolute;
    top: 30px;
  }

  .insightChartSpinner {
    top: 30%; 
    position: relative; 
    transform: translateY(-40%); 
    margin: 3.5rem 5.9rem 0px auto;
  }
</style>
