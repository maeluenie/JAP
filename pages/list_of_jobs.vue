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
          <Jobs v-for="job in jobs"
            :key="job.id"
            :id="job.id" :job="job.position"/>

          <v-card
            class="ml-4 mb-4"
            width="48rem"
            hover
            Jobs
            v-for="job in jobs"
            :key="job.id"
            :id="job.id" :job="job.position">
          
          
            <v-list-item>
              <v-list-item-content>
                <div class="text-h6 ml-4 font-weight-bold">{{ job.position }}</div>
                <v-container bg>
                  <v-layout row justify-start class="py-2 px-4">
                    <v-layout column align-content-start justify-start>
                      <v-list-item-avatar class="text-p6" align="center" size="100px" color="light grey"
                        ><div class="text-body-6"> {{ job.position }}</div></v-list-item-avatar
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
                        <div class="ml-2">{{job.department}}</div>
                      </v-layout>
                      <v-layout row class="my-2">
                        <v-icon class="mr-2" color="black">mdi-map-marker</v-icon>
                        <!-- <div class="font-weight-bold">Location:</div> -->
                        <div class="ml-2">{{job.working_location}}</div> </v-layout
                      ><v-layout row class="my-2">
                        <v-icon class="mr-2" color="black">mdi-clock</v-icon>
                        <!-- <div class="font-weight-bold">Team:</div> -->
                        <div class="ml-2">{{job.working_time_details}}</div>
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
                        <div class="ml-2">{{job.application_deadline}}</div>
                      </v-layout>
                      <v-layout row class="my-2">
                        <div class="font-weight-black">Start Date:</div>
                        <div class="ml-2">{{job.start_date}}</div>
                      </v-layout>
                      <v-layout row class="my-2">
                        <div class="font-weight-black">Salary Range:</div>
                        <div class="ml-2">{{job.approx_salary}}</div>
                      </v-layout>
                    </v-layout>
                  </v-layout>
                </v-container>
              </v-list-item-content>
            </v-list-item>

            <v-divider class="my-2"></v-divider>

            <v-col class="text-right">
              <!-- <v-btn
                align="end"
                outlined
                color="primary darken-3"
                class="mr-2"
                nuxt to="/OPaddJob1"
              >
                this section must take users to job details page with details of that job + v-if "admin" role 
                APPLY
              </v-btn>  -->
              <v-btn
                align="end"
                color="primary darken-3"
                hover
                class="mr-2"
              >
                <!-- this application form url must include the job details -->
                Details
              </v-btn>
            </v-col>

          </v-card>
 
      </v-layout>
    </v-container>

  <v-container>

    <v-row class="text-right">
      <v-col col="12">
        
          <v-speed-dial
            v-model="fab"
            bottom
            direction="right"
            :open-on-hover="false"
            transition="slide-y-reverse-transition"
          >
            <template v-slot:activator>
              <v-btn v-model="fab" color="blue darken-2" dark fab>
                <v-icon v-if="fab">mdi-close</v-icon>
                <v-icon v-else>mdi-format-list-bulleted</v-icon>
              </v-btn>
            </template>
            <v-col>
              <v-tooltip top color="grey">
                <template v-slot:activator="{ on, attrs }">
                <v-btn fab dark small color="green"
                  class="mx-1"
                  v-bind="attrs"
                  v-on="on"
                  nuxt to="/addJob"
                >
                  <v-icon dark> mdi-plus </v-icon>
                </v-btn>
              </template>
              <span>Add Job</span>
              </v-tooltip>

              <v-tooltip top color="grey">
                <template v-slot:activator="{ on, attrs }">
                <v-btn fab dark small color="primary-darken"
                  class="mx-1"
                  v-bind="attrs"
                  v-on="on"
                  nuxt to="/applicants"
                >
                  <v-icon dark> mdi-account </v-icon>
                </v-btn>
              </template>
              <span>Suitable Applicant</span>
              </v-tooltip>
            </v-col>
          </v-speed-dial>  
      
      </v-col>
    </v-row>
  
  </v-container>



  </div>
</template>

<script>
import axios from "axios";
import Jobs from "../components/Jobs";
export default {
  components:{
    Jobs
  },
  data(){
    return { 
    jobs: [] ,
    selectedRole:"",
    fab: ""
  }
  },
  async created() {
    const config = {
      headers:{
        'Accept':'application/json'
      }
    }
    try{
    const res = await axios.get("https://api.job-application.duckdns.org/getAllJobs",config);
    this.jobs = res.data.Jobs;
    console.log(res.data)

    } catch(err) {
      console.log(err)
    }
  },
    return: {
      selectedRole: [],
      fab: false,
    },
    watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = "YEAR"));
    },
  },
  methods: {
    printSelect() {
      console.log(this.selectedRole);
    },
  }      
};

</script>