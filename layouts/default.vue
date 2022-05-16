<template>
  <v-app>
    <!-- this marks the left side bar -->

    <v-navigation-drawer 
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >

    <v-list>
      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :to="item.to"
        router
        exact
        dense
        color="primary darken-3"
      >
  
          <!-- Looping through the imported list of item declared from line 138-158 -->

          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- this marks the end of left side bar -->

    <!-- this marks the top navigation bar -->

    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon >mdi-{{ `chevron-${miniVariant ? "right" : "left"}` }}</v-icon>
      </v-btn>
      <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>mdi-application</v-icon>
      </v-btn>
      <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>mdi-minus</v-icon>
      </v-btn>
      <v-toolbar-title class="font-weight-bold primary--text text--darken-3" v-text="title"/>
      <v-spacer />
      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
        <div v-if="$auth.loggedIn">
          {{$auth.user.username}}
          <v-btn text>Logout</v-btn>
        </div>
        <div v-else>
          <v-btn text to="/login">Login</v-btn>
        </div>
    </v-app-bar>

    <!-- this marks the end of the top navigation bar -->

    <!-- this marks the content section -->

    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>

    <!-- this marks the end of the content section -->

    <!-- this marks the right drawer section -->

    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light> mdi-repeat </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- this marks the right drawer section -->

    <!-- this marks the footer on the bottom-most of the page -->

    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>

    <!-- this marks the end of the footer on the bottom-most of the page -->
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: "mdi-lock",
          title: "Login",
          to: "/login",
        },
        {
          icon: "mdi-chart-bubble",
          title: "About us",
          to: "/company_information",
        },
        {
          icon: "mdi-chart-bubble",
          title: "Job Display",
          to: "/list_of_jobs",
        },
    

      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Job Application Portal",
    };
  },
};
</script>
