<template>
  <v-app>
    <!-- this page will be how users can submit their purpose and required information for the job, full page overlay can be used -->
    
    <v-card class="mx-6 my-4" outlined color="transparent">

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to ="/addJob1">
    <v-text>1 Biographical</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" nuxt to="/addJob2">
    <v-text>2 Working Requirement</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/addJob3">
    <v-text>3 General Evaluation</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/addJob3">
    <v-text>3 Personalized Evaluation</v-text>
    </v-btn>

    </v-card>


    <v-card class="mx-4 my-2 py-2">
      <v-text-title class="font-weight-bold"

        ><h2 class="mx-8 my-4 text-left">
          Personal Information
        </h2></v-text-title>
     

      <v-row class="mx-4 justify-center align-center">
        <v-col cols="1" sm="1" md="12">
          <div class="text-left justify-left" >
            <input
              type="file"
              accept=".jpeg,.jpg,.png,image/jpeg,image/png"
              label="upload image button"
              @change="selectedFile"
              ref="fileInput"
              style="display: none"
            />

            <img
              icon
              @click="$refs.fileInput.click()"
              width="150"
              height="150"
              src="~assets/upload.png"
            />
            <p class="mb-1 text-left">Upload your profile image.</p>
          </div>
        </v-col>
      </v-row>

      <v-form class="mx-4 mt-2 align-content-center" elevation-1>
        <!-- on real use case situation, the upload method will be included in the main save button -->
        <v-container bg>
          <v-layout
            row
            wrap
            align-center
            align-content-center
            justify-center
            class="mx-1"
          >
            <v-flex class="mx-2">
              <v-text class="font"
                ><h5 class="mb-1 text-left">Full Name</h5>
              </v-text>
              <v-text-field
                v-model="fullName"
                :rules="nameRules"
                label="Full Name"
                required
                outlined
                dense
              ></v-text-field>
            </v-flex>
            <v-flex class="mx-2">
              <v-text class="font"
                ><h5 class="mx-1 mb-1 text-left">Approximate Salary</h5></v-text
              >
              <v-text-field
                v-model="approximateSalary"
                :rules="numRules"
                type="number"
                label="Approximate Salary"
                required
                dense
                outlined
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>

        <v-col class="text-right">
          <v-btn align="end" color="primary darken-3"> Next </v-btn>
        </v-col>
      </v-form>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: " Application Form Page",
  data: () => ({
    
    return: {
      selectedFile: null,
  
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
      competencies: [
        {
          skillName: "UX/UI Designer",
          skillDesc:
            "Discover how users can simply use the application as simple as possible",
        },
        {
          skillName: "DevOps",
          skillDesc:
            "Provide stable system for different components of a system",
        },
        {
          skillName: "Cyber Security",
          skillDesc:
            "Check the authenticity and security of a system to prevent hacking or data leaks",
        },
        {
          skillName: "Front-End Developer",
          skillDesc:
            "Web-application developer using React.js framework to create a system's interface",
        },
      ],
      accommodations: true, // must link with the database through an API
      vehicles: false, // must link with the database through an API
      laptop: false, // must link with the database through an API
      overtime: false, // must link with the database through an API
      // must link with the database through an API
      textExample:
        "User experience (UX) designers are among the most in-demand professionals in the creative industry right now. As businesses update their websites, mobile apps and more to interact with customers in new ways, people who can help conceive and build intuitive and engaging digital experiences are needed across the country. The UX designer creates satisfying and compelling experiences for users of a product, often drawing on results from user research and workflow analysis. Generally, UX designers need to possess strong creative, technical and problem-solving skills. Areas of focus may include content, controls, visual design and development, information architecture, user research, branding, and customer/technical support.",
    },
    valid: true,
    citizenID: "",
    citizenID_Rules: [
      (v) => !!v || "This field is required, receiving only integers",
      (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],
    fullName: "",
    nameRules: [
      (v) => !!v || "This field is required",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    select: null,
    religion: "",
    religionSelection: [
      "Buddhism",
      "Christianity",
      "Islam",
      "Hinduism",
      "Sikhism",
      "Atheist",
      "Others",
    ],
    activePicker: null,
    date: null,
    menu: false,
    checkbox: false,
  }),
  watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = "YEAR"));
    },
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
    selectedFile(event) {
      // this is the function used to upload images for the profile picture.
      console.log(event);
      console.log("Image uploaded successfully");
      this.selectedFile = event.target.files[0]; // this is use to access the actual image file in and store it in the "selectedFile" section.
    },
  },
};
</script>
<style></style>
