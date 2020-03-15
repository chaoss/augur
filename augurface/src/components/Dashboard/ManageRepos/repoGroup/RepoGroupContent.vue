<template>
  <div id="RepoGroupContent">
    <div id="add-repos-input">
      <aug-text-area
        text="Add repos to group"
        placeholder="git urls (seperated by commas, newlines, and spaces)"
        inputName="urls"
        @valueUpdated="setUrlsInput"
      />
      <aug-button text="add" @click="addRepos()" />
      <aug-spinner v-if="isCurrentlyAddingRepos" size="2" />
    </div>
    <repo-list
      v-if="repoCountInGroup(repoGroup.repo_group_id) > 0"
      :repos="getReposInGroup(repoGroup.repo_group_id)"
      style="margin-top: 3rem"
    />
  </div>
</template>

<script>
import AugButton from "../../../BaseComponents/AugButton.vue";
import AugTextArea from "../../../BaseComponents/AugTextArea";
import AugSpinner from "../../../BaseComponents/AugSpinner";
import RepoList from "./RepoList.vue";
import { mapGetters } from "vuex";

export default {
  name: "RepoGroupContent",

  props: {
    isCollapsed: {
      type: Boolean,
      default: () => {
        return true;
      }
    },
    repoGroup: {
      type: Object,
      default: () => {
        return {
          rg_name: "sample group",
          repo_group_id: "sampleid"
        };
      }
    }
  },

  data() {
    return {
      urlsInput: "",
      isCurrentlyAddingRepos: false
    };
  },

  methods: {
    setUrlsInput(val) {
      this.urlsInput = val;
    },
    stopEventPropagation(e) {
      e.stopPropagation(); // keep events from propogating to parent components
    },
    addRepos() {
      if (this.isCurrentlyAddingRepos) {
        return;
      }

      this.isCurrentlyAddingRepos = true;

      // setup
      let urls = this.urlsInput.split(/[ ,\n]+/).map(url => url.trim()); // regex splits by spaces, newlines and commas
      let requestBody = {
        group: this.repoGroup.rg_name,
        repos: urls
      };

      // console.log(requestBody);

      // make request
      fetch(`${this.$store.state.utilModule.baseEndpointUrl}/add-repos`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(requestBody)
      })
        .then(res => {
          console.log(`STATUS: ${res.status}`);
          if (res.status === 200) {
            return res.json();
          } else {
            return null;
          }
        })
        .then(res => {
          if (res) {
            // update state
            this.$store.commit("reposModule/addRepos", res.repos_inserted);

            // check for failed adds
            if (res.repos_not_inserted.invalid_inputs.length > 0) {
              window.alert(
                `${res.repos_inserted.length} repos successfully added\n${res.repos_not_inserted.invalid_inputs.length} repos failed\ncheck console for detail`
              );
              console.log("following repos failed to be inserted: ");
              console.log(res.repos_not_inserted.invalid_inputs);
            }

            this.isCurrentlyAddingRepos = false;
          }
        });
    }
  },

  components: {
    AugButton,
    AugTextArea,
    AugSpinner,
    RepoList
  },

  computed: {
    ...mapGetters("reposModule", ["getReposInGroup", "repoCountInGroup"])
  }
};
</script>

<style scoped>
#RepoGroupContent {
  position: relative;
  top: 0.3rem;
  border-top: 1px solid var(--grey);
  padding-top: 1rem;
  padding-bottom: 0.5rem;
}

#RepoGroupContent > * {
  margin-top: 1rem;
}

p {
  height: 200px;
}

.open {
  background-color: var(--light-grey) !important;
}

#add-repos-input {
  max-width: 80%;
  justify-content: flex-start;
  display: flex;
  align-items: flex-end;
}

#add-repos-input > * {
  margin-left: 1rem;
}

#add-repos-input button {
  background-color: white;
  margin-left: 1rem !important;
}

.ease-enter-active,
.ease-leave-active {
  transition: max-height 0.3s, padding-top 0.3s, height 0.3s;
  height: auto;
  overflow: hidden;
}

.ease-enter,
.ease-leave-to {
  max-height: 0;
}

.ease-leave,
.ease-enter-to {
  max-height: 80vh;
}
</style>