<template>
  <v-app>
    <!-- addJob2 page will be the second page of job details with navigation after addJob1 -->
    <v-card class="mx-6 my-4" outlined color="transparent">

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to ="/OPaddJob1">
    <v-text>1 Job Details</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" nuxt to="/OPaddJob2">
    <v-text>2 General Question</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/OPaddJob3">
    <v-text>3 Benefits and Welfare</v-text>
    </v-btn>

    </v-card>


    <v-card class="mx-4 my-2 py-2">
      <v-text-title class="font-weight-bold"

        ><h2 class="mx-8 my-4 text-left">
          General Questions
        </h2></v-text-title>
     


      <v-form class="mx-8 mt-2 align-content-center">

        <v-row>
          <v-col cols="1" sm="1" md="12">

            <div class="form-group">
              <div
                v-for="(input, index) in Questions"
                :key="`ques-${index}`"
                class="input wrapper flex items-center"
              >
                  <v-textarea 
                  v-model="input.ques"
                  type="text" 
                  required
                  outlined
                  dense
                  placeholder=" Enter Question"     
                />
              <!--          Add Svg Icon-->
              <svg

                @click="addField(input, Questions)"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                width="24"
                height="24"
                class="ml-2 cursor-pointer"
              >
                <path fill="none" d="M0 0h24v24H0z" />
                <path
                  fill="green"
                  d="M11 11V7h2v4h4v2h-4v4h-2v-4H7v-2h4zm1 11C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"
                />
              </svg>

              <!--          Remove Svg Icon-->
              <svg
                v-show="Questions.length > 1"
                @click="removeField(index, Questions)"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                width="24"
                height="24"
                class="ml-2 cursor-pointer"
              >
                <path fill="none" d="M0 0h24v24H0z" />
                <path
                  fill="red"
                  d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16zm0-9.414l2.828-2.829 1.415 1.415L13.414 12l2.829 2.828-1.415 1.415L12 13.414l-2.828 2.829-1.415-1.415L10.586 12 7.757 9.172l1.415-1.415L12 10.586z"
                />
              </svg>
              </div>
            </div>
          </v-col>


          <v-col class="text-right">
            <v-btn align="end" color="natural dark-grey" nuxt to="/OPaddJob1">  
                  Back
                </v-btn>
            <v-btn align="end" color="primary darken-3" nuxt to="/OPaddJob3">  
              Next
            </v-btn>
          </v-col>
          
        </v-row>
      </v-form>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "AddRemove",
  data() {
    return {
      Questions: [{ ques: "" }],
    };
  },
  methods: {
    addField(value, fieldType) {
      fieldType.push({ value: "" });
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1);
    },
  },
};
</script>
<style></style>
