<template>
  <div>
      {{ $route.params.id }}
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data(){
    return{
      job:{}
    }
  },
  async created(){
    const config = {
      headers:{
        Accept:"application/json"
      }
    };
    try{
      const res = await axios.get("https://api.job-application.duckdns.org/getSingleJobs",config);
      this.jokes = res.data.results;
    } catch(err){
      console.log(err);
    }
  }
};
</script>

<style>

</style>