<template>
  <!-- jobDetails page will contain the details upon that specific role, 
  the page should be changed to something with the roleID at the end of the URL -->
  <v-app>
    <v-card class="mx-4 my-4">
      <v-card-title class="mx-4"> UX/UI Designer </v-card-title>
      <v-divider></v-divider>
      <v-container bg>
        <v-layout row justify-start class="mx-2 px-4 py-2">
          <v-list-item-avatar
            align="center"
            class="ml-4 mr-16"
            size="100px"
            color="grey"
            >UX/UI</v-list-item-avatar
          >
          <v-layout column align-content-start justify-start class="mx-2">
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
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Manager's Name:</div>
              <div class="ml-2">John Doe</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Recruiter:</div>
              <div class="ml-2">George Doe</div> </v-layout
            ><v-layout row class="my-2">
              <div class="font-weight-black">Recruiter Contact:</div>
              <div class="ml-2">+66 82-111-1111</div>
            </v-layout>
          </v-layout>
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Application Deadline:</div>
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
      <v-divider></v-divider>
      <v-container bg>
        <v-layout row justify-start class="mx-1">
          <v-card-subtitle class="font-weight-bold text-subtitle-1">
            Job Description
          </v-card-subtitle>
          <v-card-text class="text-body-2 text-justify">
            {{ this.textExample }}
          </v-card-text>
        </v-layout>
      </v-container>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "Job Details",
  data() {
    return {
      textExample:
        "User experience (UX) designers are among the most in-demand professionals in the creative industry right now. As businesses update their websites, mobile apps and more to interact with customers in new ways, people who can help conceive and build intuitive and engaging digital experiences are needed across the country. The UX designer creates satisfying and compelling experiences for users of a product, often drawing on results from user research and workflow analysis. Generally, UX designers need to possess strong creative, technical and problem-solving skills. Areas of focus may include content, controls, visual design and development, information architecture, user research, branding, and customer/technical support.",
    };
  },
  methods: {},
};
</script>
