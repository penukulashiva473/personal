<template>
  <v-app dark>
    <v-app-bar
      :clipped-left="clipped"
      color="black"
      fixed
      app
    >
      <v-toolbar-title class="white--text" v-text="title" />
      <v-spacer />
      <v-btn
        id="no-background-hover"
        class="white--text"
        icon
        @click="homePage"
      >
        Home
      </v-btn>
    </v-app-bar>
    <v-main style="background-color: aliceblue;">
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      title: 'Shopping Project'
    }
  },
  methods: {
    homePage () {
      this.$router.push('/')
    }
  }
}
</script>
<style scoped>

#no-background-hover::before {
  background-color: transparent !important;
}
/* *:hover {
  color: white !important;
} */
</style>
