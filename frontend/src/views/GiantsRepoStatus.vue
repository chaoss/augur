<!-- #SPDX-License-Identifier: MIT -->
<template>
  <div class="main-content-container container-fluid px-4">
    <!-- Page Header -->
    <div class="page-header row no-gutters py-4">
      <div class="col-12 col-sm-12 text-center text-sm-center mb-0">
        <span class="text-uppercase page-subtitle text-center">Viewing</span>
        <h3 class="page-title text-center">Giants-Project</h3>
      </div>
    </div>



    <div class="row">
      <div class="col">
        <div class="card card-small mb-4">
          <div v-if="!loadedInfo" class="card-header border-bottom">
            <h6 class="m-0">Information on {{ $route.params.repo_id }}</h6>
          </div>

          <d-card-body v-if="!loadedInfo">
            <spinner></spinner>
          </d-card-body>

          
          <div v-if="loadedInfo" class="card-header border-bottom">
            <h6 class="m-0">Information on {{ status.repo_name }}</h6>
          </div>
          
          <div v-if="loadedInfo" class="card-body p-0 pb-3 text-center">
            <table class="table mb-0">
              <tbody>
                aaaaaaaaaaaaa
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Component from 'vue-class-component';
import Vue from 'vue';
import {mapActions, mapGetters, mapMutations} from "vuex";
import Spinner from '../components/Spinner.vue'
@Component({
  components: {
    Spinner,
  },
  methods: {
    ...mapActions('common',[
      'endpoint', // map `this.endpoint({...})` to `this.$store.dispatch('endpoint', {...})`
                  // uses: this.endpoint({endpoints: [], repos (optional): [], repoGroups (optional): []})
      'getRepoRelations',
      'loadGiantsStatus'
    ]),

    ...mapActions('compare',[
      'addComparedRepo',
      'setBaseRepo'
    ])
  },
  computed: {
    ...mapGetters('common', [
      'sortedGiantsRepos'
    ]),
  },
})

export default class GiantsRepoStatus extends Vue{
  colors: string[] = ["#343A40", "#24a2b7", "#159dfb", "#FF3647", "#4736FF","#3cb44b","#ffe119","#f58231","#911eb4","#42d4f4","#f032e6"];
  testEndpoints: string[] = ['issuesClosed', 'codeChangesLines', 'issueNew'];
  testTimeframes: string[] = ['past 1 month', 'past 3 months', 'past 2 weeks'];
  // repos: any[] = [];
  repo_groups:any[] = [];
  repo_relations:any[] =  [];
  themes: string[] = ['dark', 'info', 'royal-blue', 'warning'];
  loadedGroups: boolean = false;
  loadedSparks: boolean = false;

  loadedInfo: boolean = false;

  loadGiantsStatus!:any;
  status:any = null;

  created() {

    this.loadGiantsStatus(this.$route.params.repo_id).then((status) => {
      this.status = status[0]
      this.loadedInfo = true
    })

  }
}

</script>
