<template>
  <!-- jobDetails page will contain the details upon that specific role, 
  the page should be changed to something with the roleID at the end of the URL -->
  <v-app>
    <v-card class="mx-4 my-4">
      <v-card-title class="mx-4"> {{ this.jobDetails.jobName }} </v-card-title>

      <v-divider></v-divider>

      <!-- this is the container of the overview of the job details -->
      <v-container bg>
        <v-layout row justify-start class="mx-2 px-4 py-2">
          <v-layout column align-content-start justify-start class="mx-2">
            <v-list-item-avatar
              align="center"
              class="ml-4 mr-16"
              size="100px"
              color="grey"
              >UX/UI</v-list-item-avatar
            ></v-layout
          >
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Team:</div>
              <div class="ml-2">{{ this.jobDetails.teamName }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <v-icon class="mr-2" color="black">mdi-map-marker</v-icon>
              <!-- <div class="font-weight-bold">Location:</div> -->
              <div class="ml-2">{{ this.jobDetails.location }}</div> </v-layout
            ><v-layout row class="my-2">
              <v-icon class="mr-2" color="black">mdi-clock</v-icon>
              <!-- <div class="font-weight-bold">Team:</div> -->
              <div class="ml-2">{{ this.jobDetails.workTime }}</div>
            </v-layout>
          </v-layout>
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Manager's Name:</div>
              <div class="ml-2">{{ this.jobDetails.managerName }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Recruiter:</div>
              <div class="ml-2">{{ this.jobDetails.recruiterName }}</div> </v-layout
            ><v-layout row class="my-2">
              <div class="font-weight-black">Recruiter Contact:</div>
              <div class="ml-2">{{ this.jobDetails.recruiterContact }}</div>
            </v-layout>
          </v-layout>
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Application Deadline:</div>
              <div class="ml-2">{{ this.jobDetails.deadline }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Start Date:</div>
              <div class="ml-2">{{ this.jobDetails.startDate }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Salary Range:</div>
              <div class="ml-2">{{ this.jobDetails.salaryRange }}</div>
            </v-layout>
          </v-layout>
        </v-layout>
      </v-container>

      <v-divider></v-divider>

      <!-- this is the container of the overview of the job description -->
      <v-container bg>
        <v-layout row justify-start class="mx-1">
          <v-card-subtitle class="font-weight-bold text-subtitle-1">
            Job Description
          </v-card-subtitle>
          <v-card-text class="text-body-2 text-justify">
            {{ this.jobDetails.jobDescription }}
          </v-card-text>
        </v-layout>
      </v-container>

      <v-divider></v-divider>

      <!-- this is the container of the overview of the benefits and welfare -->
      <v-container bg>
        <v-layout row justify-start class="mx-1">
          <v-card-subtitle class="font-weight-bold text-subtitle-1">
            Benefits and Welfare
          </v-card-subtitle>
        </v-layout>

        <!-- maybe in this <v-item-group> section we can further use v-for for icon-iterations -->
        <v-item-group class="mx-4 my-2">
          <v-tooltip bottom color="primary" v-if="jobDetails.benefits.accommodations == true">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                color="primary"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark> mdi-home </v-icon>
              </v-btn>
            </template>
            <span>Accommodations at Ladkrabang</span>
          </v-tooltip>
          <v-tooltip bottom color="grey" v-else>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                color="grey"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark> mdi-home </v-icon>
              </v-btn>
            </template>
            <span>No Accommodations Provided</span>
          </v-tooltip>

          <v-tooltip bottom color="primary" v-if="jobDetails.benefits.vehicles == true">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                color="primary"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark> mdi-car </v-icon>
              </v-btn>
            </template>
            <span> Vehicle Provisioning </span>
          </v-tooltip>
          <v-tooltip bottom color="grey" v-else>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                color="grey"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark> mdi-car </v-icon>
              </v-btn>
            </template>
            <span> No Vehicle Provided </span>
          </v-tooltip>

          <v-tooltip bottom color="primary" v-if="jobDetails.benefits.laptop == true">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                color="primary"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark> mdi-laptop </v-icon>
              </v-btn>
            </template>
            <span> Laptop is provided </span>
          </v-tooltip>
          <v-tooltip bottom color="grey" v-else>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                v-bind="attrs"
                v-on="on"
                fab
                dark
                color="grey"
              >
                <v-icon dark> mdi-laptop </v-icon>
              </v-btn>
            </template>
            <span> No Laptop Provided </span>
          </v-tooltip>

          <v-tooltip bottom color="primary" v-if="jobDetails.benefits.overtime == true">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                color="primary"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark> mdi-av-timer </v-icon>
              </v-btn>
            </template>
            <span> Overtime Bonus is provided </span>
          </v-tooltip>
          <v-tooltip bottom color="grey" v-else>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-1"
                small
                fab
                dark
                v-bind="attrs"
                v-on="on"
                color="grey"
              >
                <v-icon dark> mdi-av-timer </v-icon>
              </v-btn>
            </template>
            <span> No Overtime Bonus Provided </span>
          </v-tooltip>
        </v-item-group>
      </v-container>

      <v-divider></v-divider>

      <!-- this is the container of the required skills for this role -->
      <v-container bg>
        <v-layout row justify-start class="mx-1">
          <v-card-subtitle class="font-weight-bold text-subtitle-1">
            Required Skills
          </v-card-subtitle>
        </v-layout>
        <v-item-group class="mx-4 my-2">
          <v-tooltip
            bottom
            color="primary darken-2"
            class="mx-1"
            v-for="item in jobDetails.competencies"
            :key="item.skillName"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-chip
                color="primary darken-2"
                v-bind="attrs"
                v-on="on"
                class="mx-1"
              >
                {{ item.skillName }}
              </v-chip>
            </template>
            <span> {{ item.skillDesc }} </span>
          </v-tooltip>
        </v-item-group>
      </v-container>

      <v-divider></v-divider>

      <!-- this is the container of the overview of the buttons at the bottom of the card -->
      <v-card-actions>
        <v-spacer />
        <v-btn
          color="primary darken-2"
          class="mx-1 my-2"
          outlined
          nuxt
          to="/list_of_jobs"
        >
          BACK
        </v-btn>
        <v-dialog
          v-model="dialog1"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
        >
          <!-- this is the container of the overview of the form dialog for job application form -->
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog1 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog1 = false"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-8 my-8 py-2">
              <v-text-title class="font-weight-bold"
                ><h2 class="mx-8 mb-4 text-center">
                  Job Application Form
                </h2></v-text-title
              >
              <v-row class="mx-4 justify-center align-center">
                <v-col>
                  <div class="text-center justify-center" centered>
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
                      centered
                      width="150"
                      height="150"
                      src="~assets/upload.png"
                    />
                    <p class="mb-1 text-center">Upload your profile image.</p>
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
                        ><h5 class="mx-1 mb-1 text-left">
                          Email Address
                        </h5></v-text
                      >
                      <v-text-field
                        v-model="email"
                        :rules="emailRules"
                        type="number"
                        label="Email Address"
                        required
                        dense
                        outlined
                      ></v-text-field>
                    </v-flex>
                  </v-layout>
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
                        ><h5 class="mx-1 mb-1 text-left">
                          Approximate Salary
                        </h5></v-text
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
                        ><h5 class="mx-1 mb-1 text-left">
                          Approximate Salary
                        </h5></v-text
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
                  <v-btn align="end" color="primary darken-3" @click="testPrint"> Next </v-btn>
                </v-col>
              </v-form>
            </v-card>
          </v-card>
        </v-dialog>
        <v-btn
          color="primary darken-2"
          class="ml-1 mr-4 my-2"
          nuxt
          to="/APform1"
        >
          APPLY2
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "Job Details",
  data: () => ({
    return: { selectedFile: null }, // must return the data gathered from different entries and wrap up into json file.
    dialog1: false,
    notifications: false,
    sound: true,
    widgets: false,
    jobDetails: {        // must link with the database through an API
      jobName: "UX/UI Designer",
      teamName: "UX Researchers",
      location: "Ladkrabang HQ",
      workTime: "Full-Time, Weekdays",
      managerName: "John Doe",
      recruiterName: "George Doe",
      recruiterContact: "+66 82-111-1111",
      deadline: "February 25, 2022",
      startDate: "April 1, 2022",
      salaryRange: "Negotiable",
      competencies: [
        // must be taken from the database through an API which was linked from the front-end
        {
          skillName: "User Experience Architect",
          skillDesc:
            "Discover how users can simply use the application as simple as possible",
        },
        {
          skillName: "DevOps Planning",
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
      benefits: {
        accommodations: true, // must link with the database through an API
        vehicles: true, // must link with the database through an API
        laptop: true, // must link with the database through an API
        overtime: true, // must link with the database through an API
      },
      jobDescription:
        "User experience (UX) designers are among the most in-demand professionals in the creative industry right now. As businesses update their websites, mobile apps and more to interact with customers in new ways, people who can help conceive and build intuitive and engaging digital experiences are needed across the country. The UX designer creates satisfying and compelling experiences for users of a product, often drawing on results from user research and workflow analysis. Generally, UX designers need to possess strong creative, technical and problem-solving skills. Areas of focus may include content, controls, visual design and development, information architecture, user research, branding, and customer/technical support.",
    },
    valid: true,
    citizenID: "",
    citizenID_Rules: [
      (v) => !!v || "This field is required, receiving only integers",
      (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],
    fullName: "",
    nameRules: [(v) => !!v || "Full name is required"],
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
    testPrint(){
      console.log(this.fullName)
    }
  },
};
</script>
