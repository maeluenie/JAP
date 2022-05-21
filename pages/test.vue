<template>
  <div id="app">
    <form name="vue-upload" method="post" action="https://localhost/upload" @submit="sendForm">

  <input type="file" id="files" @change="onFileChanged" multiple>

   <button :disabled="!files">Upload!</button>
  
  </form>

</div>
  
</template>

<script>
import axios from 'axios'
export default {
  
  data() {
    return{
      message: 'Upload files here:',
      files: false,
      test:[]
    }
  },
   async created(){
    const config = {
      headers:{
        Accept: 'application/json'
      }
    }
    try{
      const res = await axios.get(
        "https://api.job-application.duckdns.org/getAllJobs", config
      );
      
      console.log(res.data);
    }catch(err){
      console.log(err);
    }
  },
  methods:{
    onFileChanged: function(e){
      var files = e.target.files;
      console.log(e);
      this.files = files;
    },
    sendForm: function(e){
      
      if (!this.files) {
        e.preventDefault();
        alert("Select file, yo!");
        return false;
      }
      
      // old school submit if ya want
      
      // or fetch if IE11 not a problem
      // or JQuery because we still have to include it
      // or old schoool XMLHttpRequest
      
    }
  }
}
// <script>
// import axios from 'axios';
// export default {
//   name: "List of Jobs Page",
//   data () {
    
//     return {
//       selectedRole: [],
//       fab: false,
//     },
//   },
//     async created(){
//     const config = {
//       headers:{
//         Accept: 'application/json'
//       }
//     }
//     try{
//       const res = await axios.get(
//         "https://api.job-application.duckdns.org/getAllJobs", config
//       );
//       console.log('hi');
//     }catch(err){
//       console.log(err);
//     }
//   },
//     // asyncData () {
//     //   await axios.get('http://143.198.77.144:8000/getAllJobs')
//     //   .then(res => {
//     //   consol.res.data })
//     //   }
//     // },


//     selectedRole:"",
//     job_role: [
//       // must be retrieved from the database via the API
//       "UX/UI Designer",
//       "DevOps",
//       "Cyber Security",
//       "Back-End Golang Developer",
//       "Front-End Developer",
//     ],
//     jobList: {
//       jobOverview1: {
//         // must link with the database through an API
//         jobID: 1111,
//         jobName: "UX/UI Designer",
//         teamName: "UX Researchers",
//         location: "Ladkrabang HQ",
//         workTime: "Full-Time, Weekdays",
//         deadline: "February 25, 2022",
//         startDate: "April 1, 2022",
//         salaryRange: "Negotiable",
//       },
//       jobOverview2: {
//         // must link with the database through an API
//         jobID: 1112,
//         jobName: "Back-End Developer ( Golang )",
//         teamName: "Back-End Team",
//         location: "Ramkhamhaeng Office",
//         workTime: "Part-Time, Weekdays",
//         deadline: "February 24, 2022",
//         startDate: "April 15, 2022",
//         salaryRange: "100,000 THB",
//       },
//     },
//   },
//   watch: {
//     menu(val) {
//       val && setTimeout(() => (this.activePicker = "YEAR"));
//     },
//   },
//   methods: {
//     printSelect() {
//       console.log(this.selectedRole);
//     },

//     // async created(){
//     //   const config ={
//     //     headers:{
//     //     Accept: "application/json"
//     //     }
//     //   };
//     //   try {
//     //     const res = await axios.get(
//     //       "http://143.198.77.144:8000/getAllJobs", config
//     //     );
//     //     console.log(res.data);
//     //     //this.currInv = res.data;
//     //   } catch (err) {
//     //     console.log(err);
//     //   }
//     // }
//   }      
// };
</script>

<style>

</style>