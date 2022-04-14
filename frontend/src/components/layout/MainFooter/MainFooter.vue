<!-- #SPDX-License-Identifier: MIT -->
<template>
  <footer
    class="main-footer d-flex p-2 px-3 border-top body-bg-color"
    style="
      position: fixed;
      left: 0;
      bottom: 0;
      width: 100%;
      text-align: center;
      z-index: 1001;
    "
  >
    <div :class="[contained ? 'container' : 'container-fluid']">
      <div class="row" style="margin-top: 4px">
        <ul class="nav" style="margin: 0px auto 0px auto">
          <li v-for="(item, idx) in menuItems" :key="idx" class="nav-item">
            <d-link class="nav-link" :href="item.to">{{ item.title }}</d-link>
          </li>
          <li class="nav-item d-flex ">
            <div class="d-flex align-items-center gap-2">
              <input
                @change="toggleTheme"
                id="checkbox"
                type="checkbox"
                class="switch-checkbox mr-2"
              />
              <label for="checkbox" class="switch-label m-0">
                <span v-if="userTheme == 'light-theme'">🌙</span>
                <span v-else>☀️</span>
                <div
                  class="switch-toggle"
                  :class="{
                    'switch-toggle-checked': userTheme === 'dark-theme',
                  }"
                ></div>
              </label>
            </div>
          </li>
        </ul>
        <!-- <span class="copyright ml-auto my-auto mr-2">{{ copyright }}</span> -->
      </div>
    </div>
  </footer>
</template>

<script>
const defaultMenuItems = [
  {
    title: "Augur",
    to: "http://augurlabs.io",
  },
  {
    title: "CHAOSS",
    to: "https://chaoss.community",
  },
  {
    title: "Augur Documentation",
    to: "https://oss-augur.readthedocs.io",
  },
  {
    title: "Submit an Issue",
    to: "https://github.com/chaoss/augur/issues/new/choose",
  },
];
export default {
  name: "main-footer",
  props: {
    /**
     * The footer menu items.
     */
    menuItems: {
      type: Array,
      default() {
        return defaultMenuItems;
      },
    },
    /**
     * The copyright information.
     */
    copyright: {
      type: String,
      default: "Copyright © 2018 DesignRevision",
    },
    /**
     * Whether the footer should be wrapped in a container, or not.
     */
    contained: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      userTheme: "light-theme",
    };
  },

  mounted() {
    const initUserTheme = this.getTheme() || this.getMediaPreference();
    this.setTheme(initUserTheme);
  },

  methods: {
    setTheme(theme) {
      localStorage.setItem("user-theme", theme);
      this.userTheme = theme;
      document.documentElement.className = theme;
    },

    toggleTheme() {
      const activeTheme = localStorage.getItem("user-theme");
      if (activeTheme === "light-theme") {
        this.setTheme("dark-theme");
      } else {
        this.setTheme("light-theme");
      }
    },

    getMediaPreference() {
      const hasDarkPreference = window.matchMedia(
        "(prefers-color-scheme: dark)"
      ).matches;
      if (hasDarkPreference) {
        return "dark-theme";
      } else {
        return "light-theme";
      }
    },
    getTheme() {
      return localStorage.getItem("user-theme");
    },
  },
};
</script>