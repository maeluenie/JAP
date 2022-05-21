<template>
  <v-form class="mx-8 mt-2 align-content-center">
       
    <v-card class="mx-4 my-2 py-2">
      <v-text-title>
        <h2 class="mx-8 my-4 text-left">
          Specific Questions
        </h2>
      </v-text-title>
    </v-card>

      
          <div v-for="(question, i) in all_q" :key="i"> 
            <v-card  class="mx-4 my-2 py-2">
              <v-row class="mt-2">
                <v-col cols="20" sm="20" md="12">
                  
                        Question {{i+1}}. {{ question.question}}
                    
                      <v-text-field
                        v-model="question.answer" 
                        required
                        outlined
                        dense
                        placeholder="Enter Answer"     
                      />
              
                
                </v-col>
              </v-row>
            </v-card>
          </div>
          <!-- {{all_q}} -->
          <v-row>
          <v-dialog
            v-model="dialog"
            width="500"
          >
            <template v-slot:activator="{ on, attrs }">
                <v-col>
                  <v-btn 
                  align="end" 
                  color="primary darken-3"
                  v-bind="attrs"
                  v-on="on" 
                  @click="submit();"
                  > 
                    Submit
                  </v-btn>
                  
                </v-col>
            </template>
          <v-card>
            <v-card-title icon ="mdi-check" class="text-h5 grey lighten-2">
              Submitted!
            </v-card-title>

            <v-card-text>
              Thank you for your interest, futhur information will be informed as soon as possible.
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                @click="dialog = false"
                nuxt to="/"
              >
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
          </v-dialog>
          </v-row>
  </v-form>
</template>

<script>
import axios from 'axios';
export default {
  computed: {
    all_q2(){
      return this.all_q.map(value=>{return {
        question_id: value.q_id,
        answer: value.answer
      }})
    }
  },
  data(){
    return{
      dialog:false,
      questions:[],
      answer: [],
      all_q: []
      // user:{
      //   id:[],
      //   questions:[]
      // }
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
    const res = await axios.get("https://api.job-application.duckdns.org/displaySelectedQuestions",config);
    this.questions = res.data.questions;
    this.qa()
    console.log(res.data.questions)

    } catch(err) {
      console.log(err)
    }
  },
  methods:{
     activate() {
      setTimeout(() => this.isHidden = false, 500);
    },
    async qa(){
      for(let i of this.questions)
      this.all_q.push({
        ...i,
        answer:""
      })
      console.log(this.all_q)
    },
    async submit(){
      const config = {
        headers:{
          Authorization : this.$auth.$storage._state["_token.local"],
        }
      }
      await axios.post('https://api.job-application.duckdns.org/postSpecificQuestions',{
        "list_of_answers":this.all_q.map(value=>{return {
        q_id: value.q_id,
        answer: value.answer
      }})},config)
    }
  }
}
</script>

<style>

</style>