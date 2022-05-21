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
          <!-- :items="job_role" -->
          <v-combobox
            v-model="selectedRole"
            
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
        <!-- <v-btn @click="printSelect" color="primary darken-3" justify-center>
          <v-icon> mdi-magnify </v-icon>
        </v-btn> -->
        
        <!-- v-btn above must include the feature to select the roles accordingly. -->
      </v-layout>
    
      <Jobs 
        v-for="(job,i) in filteredjobs" :key="i" 
        :id="job.job_id.toString()" 
        :rolename="job.rolename"
        :department="job.department"
        :working_time_details="job.working_time_details"
        :working_location="job.working_location"
        :application_deadline="job.application_deadline"
        :start_date="job.start_date"
        :approx_salary="job.approx_salary"
      />

    </v-container>


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
  
  



  </div>
</template>

<script>
import axios from "axios";
import Jobs from '../../components/Jobs.vue'
export default {
  middleware: ['is-admin'],
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
    this.jobs = res.data;
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
  },
  computed:{
    filteredjobs(){
      return this.jobs.filter(job => job.rolename && job.rolename.includes(this.selectedRole))

    
    }
  }      
};

</script>