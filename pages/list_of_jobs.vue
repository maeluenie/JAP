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
        <v-btn @click="printSelect" color="primary darken-3" justify-center> <v-icon> mdi-magnify </v-icon> </v-btn>
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
            <v-card class="ml-4 mb-4" width="48rem">
              <v-list-item>
                <v-list-item-avatar
                  align="center"
                  tile
                  color="grey"
                ></v-list-item-avatar>

                <v-list-item-content>
                  <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

                  <v-container bg fill-height align-left>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Ladkrabang HQ </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                    </v-layout>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Start Date : April 2022 </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          Deadline : March 3 , 2022
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          Approx. Salary ≈ 100,000 THB
                        </v-flex>
                      </v-layout>
                    </v-layout>
                  </v-container>
                </v-list-item-content>
              </v-list-item>

              <hr class="my-1" />

              <v-col class="text-right">
                <v-btn align="end" outlined color="primary darken-3" nuxt to="/addJob1"> <!-- this section must take users to job details page with details of that job + v-if "admin" role -->
                  Edit
                </v-btn>
                <v-btn align="end" color="primary darken-3" nuxt to="/applicationForm">  <!-- this application form url must include the job details -->
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
        "UX/UI Designer",
        "DevOps",
        "Cyber Security",
        "Back-End Golang Developer",
        "Front-End Developer",
      ],
    };
  },
  methods:{
    printSelect() {
      console.log(this.selectedRole)
    }
  }
};
</script>
