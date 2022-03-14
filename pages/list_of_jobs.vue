<template>
  <!-- list_of_jobs page must have the consideration of roles to see -->

  <div>
    <v-container bg>
      <v-layout
        row
        wrap
        align-center
        align-content-center
        justify-center
        class="mx-4"
      >
        <v-flex>
          <!-- hide-selected is also a props to consider for UX -->
          <v-combobox
            v-model="selectedRole"
            :items="job_role"
            label="Select your dream jobs"
            elevation-4
            multiple
            solo
            persistent-hint
            small-chips
            class="mx-2 mt-6 font-weight-bold"
            clearable
          ></v-combobox>
        </v-flex>
        <v-btn @click="printSelect" color="primary darken-3" justify-center>
          <v-icon> mdi-magnify </v-icon>
        </v-btn>
        <!-- v-btn above must include the feature to select the roles accordingly. -->
      </v-layout>
      <v-layout
        row
        wrap
        align-content-space-around
        justify-start
        class="mx-2 my-2"
      >
        <!-- for the v-card, usage of <v-for> is considerable for repetitive display of cards -->
        <v-card class="ml-4 mb-4" width="48rem" nuxt to="/jobDetails" hover>
          <v-list-item>
             <v-list-item-content>
              <div class="text-h6 ml-4 font-weight-bold">OVERLINE</div>
              <v-container bg>
                <v-layout row justify-start class="py-2">
                  <v-layout
                    column
                    align-content-start
                    justify-start
                    class="mx-1"
                  >
                    <v-list-item-avatar
                      align="center"
                      class="ml-1 mr-1"
                      size="100px"
                      color="grey"
                      >UX/UI</v-list-item-avatar
                    ></v-layout
                  >
                  <v-layout
                    column
                    align-content-start
                    justify-start
                    class="mx-2"
                  >
                    <v-layout row class="my-2">
                      <div class="font-weight-black">Team:</div>
                      <div class="ml-2">User Experience Design</div>
                    </v-layout>
                    <v-layout row class="my-2">
                      <v-icon class="mr-2" color="black">mdi-map-marker</v-icon>
                      <!-- <div class="font-weight-bold">Location:</div> -->
                      <div class="ml-2">Ladkrabang HQ, Bangkok</div> </v-layout
                    ><v-layout row class="my-2">
                      <v-icon class="mr-2" color="black">mdi-clock</v-icon>
                      <!-- <div class="font-weight-bold">Team:</div> -->
                      <div class="ml-2">Full-Time, Weekdays</div>
                    </v-layout>
                  </v-layout>
                  <v-layout
                    column
                    align-content-start
                    justify-start
                    class="mx-2"
                  >
                    <v-layout row class="my-2">
                      <div class="font-weight-black">Deadline:</div>
                      <div class="ml-2">February 25, 2022</div>
                    </v-layout>
                    <v-layout row class="my-2">
                      <div class="font-weight-black">Start Date:</div>
                      <div class="ml-2">April 1, 2022</div>
                    </v-layout>
                    <v-layout row class="my-2">
                      <div class="font-weight-black">Salary Range:</div>
                      <div class="ml-2">Negotiable</div>
                    </v-layout>
                  </v-layout>
                </v-layout>
              </v-container>
            </v-list-item-content>
          </v-list-item>

          <hr class="my-1" />

          <v-col class="text-right">
            <v-btn
              align="end"
              outlined
              color="primary darken-3"
              nuxt
              to="/addJob1"
            >
              <!-- this section must take users to job details page with details of that job + v-if "admin" role -->
              Edit
            </v-btn>
            <v-btn
              align="end"
              color="primary darken-3"
              hover
              nuxt
              to="/applicationForm"
            >
              <!-- this application form url must include the job details -->
              Apply
            </v-btn>
          </v-col>
        </v-card>
        
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "List of Jobs Page",
  data() {
    return {
      selectedRole: [],
      job_role: [
        // must be retrieved from the database via the API
        "UX/UI Designer",
        "DevOps",
        "Cyber Security",
        "Back-End Golang Developer",
        "Front-End Developer",
      ],
    };
  },
  methods: {
    printSelect() {
      console.log(this.selectedRole);
    },
  },
};
</script>
