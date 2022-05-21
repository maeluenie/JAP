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
        <v-btn @click="printSelect" color="primary darken-3" justify-center>
          <v-icon> mdi-magnify </v-icon>
        </v-btn>
        
        <!-- v-btn above must include the feature to select the roles accordingly. -->
      </v-layout>

      <Jobsnocred 
        v-for="(job,i) in jobs" :key="i" 
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
  </div>
</template>


<script>
import axios from "axios";
import Jobs from '../../components/Jobs.vue'

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
    this.jobs = res.data;
    console.log(res.data)

    } catch(err) {
      console.log(err)
    }
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