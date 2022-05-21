<template>
  <nuxt-link :to ="'jobDetails/'+id">
    <v-layout
        row
        wrap
        align-content-space-around
        justify-start
        class="mx-2 my-2"
      >
  
        
        <!-- for the v-card, usage of <v-for> is considerable for repetitive display of cards -->

          <v-card
            class="ml-4 mb-4"
            width="48rem"
            hover
          >
          
          
            <v-list-item>
              <v-list-item-content>
                <div class="text-h6 ml-4 font-weight-bold">{{ rolename }}</div>
                <v-container bg>
                  <v-layout row justify-start class="py-2 px-4">
                    <v-layout column align-content-start justify-start>
                      <v-list-item-avatar class="text-p6" align="center" size="100px" color="light grey"
                        ><div class="text-body-6"> {{ rolename }}</div></v-list-item-avatar
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
                        <div class="ml-2">{{department}}</div>
                      </v-layout>
                      <v-layout row class="my-2">
                        <v-icon class="mr-2" color="black">mdi-map-marker</v-icon>
                        <!-- <div class="font-weight-bold">Location:</div> -->
                        <div class="ml-2">{{working_location}}</div> </v-layout
                      ><v-layout row class="my-2">
                        <v-icon class="mr-2" color="black">mdi-clock</v-icon>
                        <!-- <div class="font-weight-bold">Team:</div> -->
                        <div class="ml-2">{{working_time_details}}</div>
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
                        <div class="ml-2">{{application_deadline}}</div>
                      </v-layout>
                      <v-layout row class="my-2">
                        <div class="font-weight-black">Start Date:</div>
                        <div class="ml-2">{{start_date}}</div>
                      </v-layout>
                      <v-layout row class="my-2">
                        <div class="font-weight-black">Salary Range:</div>
                        <div class="ml-2">{{approx_salary}}</div>
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
  </nuxt-link>
</template>

<script>
export default {
  name: "Jobs",
  props:["rolename",
  "id",
  "department",
  "working_location",
  "working_time_details",
  "application_deadline",
  "start_date",
  "approx_salary"]
}
</script>

<style>

</style>