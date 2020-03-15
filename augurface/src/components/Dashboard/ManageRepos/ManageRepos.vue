<template>
  <div id="ManageRepos">
    <manage-buttons @collapseAll="collapseAll()"/>
    <div class="loading" v-if="!isLoaded">
      <aug-spinner size="4" />
      <p>loading repositories</p>
    </div>
    <div class="groups" v-if="isLoaded">
      <repo-group
        v-for="rg in getRepoGroups"
        :key="rg.repo_group_id"
        :repoGroup="rg"
        ref="repoGroups"
        @dropdownclick="dropdownClick()"
      />
    </div>
  </div>
</template>

<script>
import RepoGroup from "./repoGroup/RepoGroup.vue";
import ManageButtons from "./ManageButtons.vue";
import AugSpinner from "../../BaseComponents/AugSpinner.vue";

import { mapGetters } from "vuex";

export default {
  name: "ManageRepos",
  components: {
    RepoGroup,
    ManageButtons, 
    AugSpinner
  },
  methods: {
    collapseAll() {
      this.$refs.repoGroups.forEach(rg => rg.collapse());
    }, 
    dropdownClick() {
      this.$refs.repoGroups.forEach(rg => {
        rg.$refs.header.$refs.dropdown.collapse()
      });
    }
  }, 
  computed: {
    ...mapGetters("reposModule", ["isLoaded", "isGroupsLoaded", "getRepoGroups"])
  }
};
</script>

<style scoped>
#ManageRepos {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 3rem;
  height: 2000px;
}

.groups {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.loading {
  margin-top: 4rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.loading > p {
  color: var(--dark-grey);
}
</style>