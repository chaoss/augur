<!-- #SPDX-License-Identifier: MIT -->
<template>
  <div class="main-content-container container-fluid px-4">
    <!-- Page Header -->
    <div class="page-header row no-gutters py-4">
      <div class="col-12 col-sm-12 text-center text-sm-center mb-0">
        <span class="text-uppercase page-subtitle text-center">Viewing all</span>
        <h3 class="page-title text-center">Giants-Project</h3>
      </div>
    </div>



    <div class="row">
      <div class="col">
        <div class="card card-small mb-4">
          <div class="card-header border-bottom">
            <h6 class="m-0">Currently Stored Repos</h6>
          </div>

          <d-card-body v-if="!loadedRepos">
            <spinner></spinner>
          </d-card-body>

          <div v-if="loadedRepos" class="card-body p-0 pb-3 text-center">
            <table class="table mb-0">
              <thead class="bg-light">
                <tr>
                  <th width="50%" scope="col" class="border-0" v-on:click="sortTable('repo_id')">
                    <div class="row">
                      <div class="col">Repo ID</div>
                      <div class="arrow" v-bind:class="ascending ? 'arrow_up' : 'arrow_down'" v-if="'repo_id' == sortColumn"></div>
                    </div>
                  </th>
                  <th width="50%" scope="col" class="border-0" v-on:click="sortTable('repo_name')">
                    <div class="row">
                      <div class="col">Repo Name</div>
                      <div class="arrow" v-bind:class="ascending ? 'arrow_up' : 'arrow_down'" v-if="'repo_name' == sortColumn"></div>
                    </div>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="repo in sortedGiantsRepos(sortColumn,ascending)" v-bind:item="repo" :key="repo.repo_id">
                  <td width="50%">
                    <a href="#" @click="onGitRepo(repo.repo_id)">{{ repo.repo_id }}</a>
                  </td>
                  <td width="50%">{{ repo.repo_name }}</td>
                  <!-- <td>
                    <div class="row">
                      <button :id="'favorite'+index" class="nav-link col col-2" style="margin-left: 2rem; margin-right: 1rem; padding: 0;border: none; background: none;">
                        <i class="material-icons" style="color:#007bff;">star_rate</i>
                        <div class="item-icon-wrapper"></div>
                      </button>
                      <d-tooltip :target="'#favorite'+index"
                                 container=".shards-demo--example--tooltip-01">
                        Consider this repo group as a "favorite" and our workers will regulaly update its metrics' data before others
                      </d-tooltip>
                      <button :id="'add_compare'+index" class="nav-link col col-2" style="padding: 0;border: none; background: none;" @click="addComparedRepo(repo)">
                        <i class="material-icons" style="color:#007bff;">library_add</i>
                        <div class="item-icon-wrapper"></div>
                      </button>
                      <d-tooltip :target="'#add_compare'+index"
                                 :triggers="['hover']"
                                 container=".shards-demo--example--tooltip-01">
                        Add this repo group to your current compared repos
                      </d-tooltip>
                    </div>
                  </td> -->
                </tr>
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
      'loadGiantsRepos'
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

export default class Giants extends Vue{
  colors: string[] = ["#343A40", "#24a2b7", "#159dfb", "#FF3647", "#4736FF","#3cb44b","#ffe119","#f58231","#911eb4","#42d4f4","#f032e6"];
  testEndpoints: string[] = ['issuesClosed', 'codeChangesLines', 'issueNew'];
  testTimeframes: string[] = ['past 1 month', 'past 3 months', 'past 2 weeks'];
  // repos: any[] = [];
  repo_groups:any[] = [];
  repo_relations:any[] =  [];
  themes: string[] = ['dark', 'info', 'royal-blue', 'warning'];
  loadedGroups: boolean = false;
  loadedSparks: boolean = false;

  loadedRepos: boolean = false;

  ascending:boolean = true;
  sortColumn: string ='repo_id';
  getRepoRelations!: any
  sortedGiantsRepos!:any
  loadGiantsRepos!:any;

  setBaseRepo!:any;
  addComparedRepo!:any;


  created() {

    this.loadGiantsRepos().then(() => {
      this.loadedRepos = true
    })

  }

  sortTable(col: string) {
      if (this.sortColumn === col) {
        this.ascending = !this.ascending;
      } else {
        this.ascending = true;
        this.sortColumn = col;
      }
  }

  onGitRepo (repo_id: number) {
    this.$router.push(`giants/${repo_id}/status`, () => {
      console.log(`REPO_ID: ${repo_id}`);
    });
  }
}

</script>
