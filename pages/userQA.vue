<template>
  <v-app>
    <!-- addJob2 page will be the second page of job details with navigation after addJob1 -->

    <v-card class="mx-4 my-2 py-2">
      <v-text-title class="font-weight-bold"

        ><h2 class="mx-8 my-4 text-left">
          Personalized Questions
        </h2></v-text-title>
     


      <v-form class="mx-8 mt-2 align-content-center">

        <v-row>
          <v-col cols="1" sm="1" md="12">

            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">1. What is the first step emphathize users.</h5></v-text
            >

            <v-textarea

            v-model="jobDescription"
            :rules="nameRules"
            label="Job Description"
            required
            outlined
            dense

            ></v-textarea>
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">Job Description</h5></v-text
            >

            <v-textarea

            v-model="jobDescription"
            :rules="nameRules"
            label="Job Description"
            required
            outlined
            dense

            ></v-textarea>
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">Job Description</h5></v-text
            >

            <v-textarea

            v-model="jobDescription"
            :rules="nameRules"
            label="Job Description"
            required
            outlined
            dense

            ></v-textarea>
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">Job Description</h5></v-text
            >

            <v-textarea

            v-model="jobDescription"
            :rules="nameRules"
            label="Job Description"
            required
            outlined
            dense

            ></v-textarea>
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">Job Description</h5></v-text
            >

            <v-textarea

            v-model="jobDescription"
            :rules="nameRules"
            label="Job Description"
            required
            outlined
            dense

            ></v-textarea>
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">Job Description</h5></v-text
            >

            <v-textarea

            v-model="jobDescription"
            :rules="nameRules"
            label="Job Description"
            required
            outlined
            dense

            ></v-textarea>
          </v-col>


          <v-col class="text-right">
            <v-btn align="end" color="primary darken-3" nuxt to="/APform4">  
              Submit
            </v-btn>
          </v-col>
          
        </v-row>
      </v-form>
    </v-card>
  </v-app>
</template>

<script>
export default {
  // name: "AddRemove",
  // data() {
  //   return {
  //     Questions: [{ ques: "" }],
  //   };
  // },
  // methods: {
  //   addField(value, fieldType) {
  //     fieldType.push({ value: "" });
  //   },
  //   removeField(index, fieldType) {
  //     fieldType.splice(index, 1);
  //   },
  // },
};
</script>
<style></style>
