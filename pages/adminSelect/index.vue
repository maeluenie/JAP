<template>
  <v-app>
    <!-- addJob2 page will be the second page of job details with navigation after addJob1 -->

    <v-card class="mx-4 my-2 py-2">
      <v-text-title class="font-weight-bold"

        ><h2 class="mx-8 my-4 text-left">
          Technical Questions for an Applicant
        </h2></v-text-title>
    </v-card>

    
      <v-form class="mx-2 mt-2 align-content-center">
      
        
        <div v-for="question in questions" :key="question.id"> 
          <v-card  class="mx-2 my-2 py-2">
            <v-row class="mt-2">
              
              <v-col>
                <v-checkbox class="mx-4 my-2 py-2" v-model="admin.selectedques" :value="question.q_id" />
              </v-col>
              <v-col>
              
                <label class="my-2 py-2 mt-2" align-content-center>{{ question.question }}</label>
              </v-col>
              <v-col>

              </v-col>
              <v-col>

              </v-col>
            </v-row>
            
          </v-card>
          
        </div>
        <v-col class="text-right">
            <v-btn align="end" color="primary darken-3" @click="send();" nuxt to = "/list_of_jobs"> 
              SEND
            </v-btn>
          </v-col>
        
       

      </v-form>
    
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  middleware: ['is-admin'],
  name:"adminSelect",
  props:["id"],
  data() {
    return {
      questions:[],
      admin:{
        selectedques: []
        // selectedques: [{q_id:"",questions:""}]
      },
      id:""
      
    }
  },

  async created() {
    const config = {
      headers:{
        Authorization : this.$auth.$storage._state["_token.local"],
        'Accept':'application/json'
      }
    }
    try{
    const res = await axios.get(`https://api.job-application.duckdns.org/displayAllSpecificQuestions/${this.$route.params.id}`,config);
    this.questions = res.data;
    console.log(res.data)

    } catch(err) {
      console.log(err)
    }
  },
  methods: {
    async send(){
      const config = {
        headers:{
          Authorization : this.$auth.$storage._state["_token.local"],

        }
      }
      await axios.post(`https://api.job-application.duckdns.org/selectSpecificQuestions/${this.$route.params.id}`,{
        "selected_q_id":this.admin.selectedques,
      },config)
    }
  }
};
</script>
<style></style>
