
<template>
  <v-app>
    <v-card>

      <v-dialog
        v-model="dialog1"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
      >
        
        <v-card>
          <v-toolbar dark color="primary">
            <v-btn icon dark nuxt to="/list_of_jobs">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Add new job form</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="submit();" nuxt to = "/list_of_jobs"> Submit </v-btn>
              <!-- this line must link a function to submit the data to the database -->
            </v-toolbar-items>
          </v-toolbar>
        
          <v-card class="mx-6 my-4" outlined color="transparent">

            <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
            <v-text>1 Job Details</v-text>
            </v-btn>

            <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="OP2();">
            <v-text>2 General Question</v-text>
            </v-btn>

            <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="OP3();">
            <v-text>3 Benefits and Welfare</v-text>
            </v-btn>

          </v-card>

          <v-card class="mx-4 my-2 py-2">
            <v-text-title class="font-weight-bold"
              ><h2 class="mx-8 my-4 text-left">Job Details</h2></v-text-title
            >

            <v-form class="mx-8 mt-2 align-content-center">
              <!-- on real use case situation, the upload method will be included in the main save button -->
              <v-row>
                <v-col cols="12" sm="8" md="6">
                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Role Name</h5></v-text
                  >

                  <v-text-field
                    v-model="roleName"
                    :rules="nameRules"
                    label="Role Name"
                    required
                    outlined
                    dense
                  ></v-text-field>
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
                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Start Date</h5></v-text
                  >
                  <v-menu
                    ref="menu1"
                    v-model="menu1"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="date1"
                        label="Start Date"
                        append-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                        outlined
                        dense
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="date1"
                      :active-picker.sync="activePicker1"
                      :min="
                        new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
                          .toISOString()
                          .substr(0, 10)
                      "
                      @change="save"
                    ></v-date-picker>
                  </v-menu>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Manager Name</h5></v-text
                  >
                  <v-select
                    v-model="managerName"
                    :rules="nameRules"
                    :items="managerSelection"
                    label="Manager Name"
                    required
                    dense
                    outlined
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Educational Degree</h5></v-text
                  >

                  <v-select
                    v-model="educationalDegree"
                    :items="degreeSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Educational Degree"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-1 text-left">Working Time Details</h5>
                  </v-text>

                  <v-select
                    v-model="workingTime"
                    :items ="timeSelection"
                    label="Working Time Details"
                    required
                    dense
                    outlined
                  >
                  </v-select>
                </v-col>

                <v-col cols="12" sm="8" md="6">
                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Belonged Teams</h5></v-text
                  >

                  <v-select
                    v-model="belongedTeam"
                    :items="teamSelection"
                    :rules="nameRules"
                    label="Belonged Team"
                    required
                    dense
                    outlined
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Number of Accepting Applicants
                    </h5></v-text
                  >
                  <v-text-field
                    v-model="numAccepting"
                    :rules="numRules"
                    type="number"
                    label="Number of Accepting Applicants"
                    required
                    outlined
                    dense
                  ></v-text-field>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">End Date</h5></v-text
                  >

                  <v-menu
                    ref="menu2"
                    v-model="menu2"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="date2"
                        label="Application Deadline"
                        append-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                        outlined
                        dense
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="date2"
                      :active-picker.sync="activePicker2"
                      :min="
                        new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
                          .toISOString()
                          .substr(0, 10)
                      "
                      @change="save"
                    ></v-date-picker>
                  </v-menu>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Working Location</h5></v-text
                  >

                  <v-select
                    v-model="workingLocation"
                    :items="locationSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Working Location"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Required Experience</h5></v-text
                  >

                  <v-select
                    v-model="requiredExperience"
                    :items="experienceSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Required Experience"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Status</h5></v-text
                  >

                  <label for="Open">
                    <input
                      type="radio"
                      name="radio"
                      value="Open"
                      id="Open"
                      v-model="status"
                    />
                    Open for Application
                  </label>
                  <label for="Close">
                    <input
                      type="radio"
                      name="radio"
                      value="Close"
                      id="Close"
                      v-model="status"
                    />
                    Close Temporarily</label
                  >
                  <label for="Urgent">
                    <input
                      type="radio"
                      name="radio"
                      value="Urgent"
                      id="Urgent"
                      v-model="status"
                    />Urgent
                  </label>
                </v-col>

                <v-col cols="1" sm="1" md="12">
                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Required Skills</h5></v-text
                  >

                  <v-combobox
                    v-model="requiredSkills"
                    :items="items"
                    :rules="nameRules"
                    chips
                    clearable
                    label="Required Skills"
                    required
                    outlined
                    dense
                    multiple
                  >
                    <template v-slot:selection="{ attrs, item, select, selected }">
                      <v-chip
                        v-bind="attrs"
                        :input-value="selected"
                        close
                        @click="select"
                        @click:close="remove(item)"
                      >
                        <strong>{{ item }}</strong
                        >&nbsp;
                        <span>(interest)</span>
                      </v-chip>
                    </template>
                  </v-combobox>
                  <v-divider class="my-2"></v-divider>

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

                  <v-col class="text-right">
                    <v-btn align="end" color="primary darken-3" @click="OP2();"> 
                      Next
                    </v-btn>
                  </v-col>
                </v-col>
              </v-row>
            </v-form>
          </v-card>
        
        </v-card>

      </v-dialog>

      <v-dialog
        v-model="dialog2"
        fullscreen
        hide-overlay
        transition="dialog-top-transition"
      >
            <!-- this is the container of the overview of the form dialog for job application form -->
        <v-card>
            <v-toolbar dark color="primary">
                <v-btn icon dark nuxt to="/list_of_jobs">
                  <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>Add new job form</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-toolbar-items>
                  <v-btn dark text @click="submit();" nuxt to = "/list_of_jobs"> Submit </v-btn>
                  <!-- this line must link a function to submit the data to the database -->
                </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-6 my-4">

              <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="OP1();">
              <v-text>1 Job Details</v-text>
              </v-btn>

              <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
              <v-text>2 General Question</v-text>
              </v-btn>

              <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="OP3();">
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

                    <div align="left">
                        <div class="my-2" v-for="(q, i) in questions" :key="i">
                          Question {{i+1}}
                          
                          <v-text-field
                            v-model="questions[i]" 
                            outlined
                            dense
                            placeholder="Enter Question"     
                          />
                    
                          
                          <v-btn
                          color="error"
                          @click="rmq(i)"
                          class=" white--text"
                          >
                          <v-icon
                          >
                            mdi-delete
                          </v-icon>Remove
                          </v-btn>

                          </div>

                          <v-btn
                            @click="addQ()"
                            color="primary darken"
                            class="my-2 white--text"
                          >
                          <v-icon
                          >
                            mdi-plus
                          </v-icon>
                          Add Question
                          </v-btn>
                      </div>
                      

                  </v-col>


                  <v-col class="text-right">
                    <v-btn align="end" color="natural dark-grey" @click="OP1();">  
                      Back
                    </v-btn>
                    <v-btn align="end" color="primary darken-3" @click="OP3();"> 
                      Next
                    </v-btn>
                  </v-col>
                  
                </v-row>
              </v-form>
          </v-card>
        </v-card>
      </v-dialog>

      <v-dialog
        v-model="dialog3"
        fullscreen
        hide-overlay
        transition="dialog-top-transition"
      >
        <!-- this is the container of the overview of the form dialog for job application form -->
        
        <v-card>
          <v-toolbar dark color="primary">
            <v-btn icon dark nuxt to="/list_of_jobs">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Add new job form</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="submit();" nuxt to = "/list_of_jobs"> Submit </v-btn>
              <!-- this line must link a function to submit the data to the database -->
            </v-toolbar-items>
          </v-toolbar>
          <v-card class="mx-6 my-4" outlined color="transparent">
            <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="OP1();">
            <v-text>1 Job Details</v-text>
            </v-btn>
            <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="OP2();">
            <v-text>2 General Question</v-text>
            </v-btn>
            <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
            <v-text>3 Benefits and Welfare</v-text>
            </v-btn>
          </v-card>

          <v-card class="mx-4 my-4 py-2">
            <v-text-title class="font-weight-bold"
              ><h2 class="mx-8 my-4 text-left">
                Benefits and Welfare        
              </h2>
            </v-text-title>

            <v-form class="mx-8 mt-2 align-content-center">
              <!-- on real use case situation, the upload method will be included in the main save button -->
              <v-row>
                <v-col cols="12" sm="8" md="6">
                  <v-text class="font"

                    ><h5 class="mx-1 mb-2 text-left">
                      Accomodation
                    </h5></v-text
                  >

                  <v-select
                    v-model= "accomodation"
                    :items="accomodationSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Accomodation"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Transportation
                    </h5></v-text
                  >

                  <v-select
                    v-model= "transportation"
                    :items="transportationSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Transportation"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Hourly Overtime Allowance
                    </h5></v-text
                  >

                  <v-select
                    v-model= "overTime"
                    :items="overtimeSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Hourly OverTime Allowance"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Laptop Provision
                    </h5></v-text
                  >

                  <v-select
                    v-model= "laptopProvision"
                    :items="laptopSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Laptop Provision"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Insurance Provision
                    </h5></v-text
                  >

                  <v-select
                    v-model= "insuranceProvision"
                    :items="insuranceSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Insurance Provision"
                    required
                    outlined
                    dense
                  ></v-select>

                  
                </v-col>

                <v-col cols="12" sm="8" md="6">
                  
                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Annual Bonus Minimum Allowance
                    </h5></v-text
                  >

                  <v-select
                    v-model= "bonusAllowance"
                    :items="bonusSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Annual Bonus Minimum Allowance (%)"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Monthly Transportation Allowance
                    </h5></v-text
                  >

                  <v-select
                    v-model= "transportationAllowance"
                    :items="transportationASelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Monthly Transportation Allowance"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Request Leave Quota
                    </h5></v-text
                  >

                  <v-select
                    v-model= "leaveQuota"
                    :items="leaveSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Request Leave Quota"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Additional Provision 
                    </h5></v-text
                  >
                  <v-select
                    v-model= "additionalProvision"
                    :items="additionalSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Additional Provision"
                    required
                    outlined
                    dense
                  ></v-select>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">
                      Insurance Level
                    </h5></v-text
                  >

                  <v-select
                    v-model= "insuranceLevel"
                    :items="insuranceLSelection"
                    :rules="[(v) => !!v || 'This field is required']"
                    label="Insurance Level"
                    required
                    outlined
                    dense
                  ></v-select>

                  
                </v-col>
              
                <v-col cols="1" sm="1" md="12">

                  <v-text class="font"
                  ><h5 class="mx-1 mb-2 text-left">
                    Additional Benefits and Welfare
                  </h5></v-text>

                  <v-textarea
                  v-model="additional"
                  :rules="nameRules"
                  label="Additional Benefits and Welfare"
                  required
                  outlined
                  dense
                  ></v-textarea>

                  <v-col class="text-right">
                    <v-btn align="end" color="natural dark-grey" @click="OP2();">  
                      Back
                    </v-btn>
                    <!-- pack into json send through API -->
                    <v-btn align="end" color="primary darken-3" @click="submit();" > 
                      Submit
                    </v-btn>
                  </v-col>
                </v-col>
              </v-row>
            </v-form>
          </v-card>
        </v-card>

      </v-dialog>
    </v-card>
  </v-app>
</template>

<script>
import axios from 'axios';
export default {
  middleware:['is-admin'],
  name: "Job Details",
  data: () => ({
    
    return: { selectedFile: null }, // must return the data gathered from different entries and wrap up into json file.
    dialog1: true,
    dialog2: false,
    dialog3: false,

    notifications: false,
    sound: true,
    widgets: false,
    //addjob dialog 2
    questions: [],

    //number
    valid: true,
    approximateSalary: "",
    numAccepting: "",
    workingTime: "",
    numRules: [
      (v) => !!v || "This field is required, receiving only integers",
      // (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],
    
    //alphabet
    roleName: "",
    managerName: "",
    requiredExperience: "",
    jobDescription: "",
    additional: "",//dialog3
    nameRules: [
      (v) => !!v || "This field is required",
      // (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    status:"",

    select: null,
    workingLocation: "",
    locationSelection: ["Latkrabung", "Sathorn", "Bangsue", "Thonglor"],

    select: null,
    educationalDegree: "",
    degreeSelection: ["Associate Degree", "Bachelor’s Degree", "Master’s Degree", "Doctoral Degree"],

    managerSelection: ["Jonathan Doe", "Josh Doe", "Jane Doe", "Jonny Foo Doe","Joshua Doe", "Jennifer Doe", "George Doe", " Giprgoe Doe"],
    
    timeSelection: ['8:00 AM - 4:00 PM','9:00 AM - 7:00 PM'],

    select: null,
    belongedTeam: "",
    teamSelection: ["product manager",
                    "ux/ui",
                    "service design",
                    "data strategy",
                    "data governance and risk",
                    "data science and analytics",
                    "data reporting and visualization",
                    "enterprise architecture",
                    "application architecture",
                    "infrastructure architecture",
                    "data architecture",
                    "integration architecture",
                    "security architecture",
                    "devops",
                    "project management",
                    "SDLC delivery",
                    "Agile deliver",
                    "app development",
                    "release management",
                    "service transition",
                    "app management",
                    "test management",
                    "testing methodology",
                    "testing tools",
                    "testing automation",
                    "middleware management",
                    "application integration",
                    "data integration",
                    "cloud",
                    "data centre",
                    "server",
                    "database",
                    "network",
                    "storage",
                    "tools and monitoring",
                    "service helpdesk and EUC",
                    "disaster recovery",
                    "identity and access management",
                    "governance, risk and compliance",
                    "cyber security",
                    "supplier assurance",
                    "security operations",
                    "data engineer"],

    select: null,
    requiredExperience: "",
    experienceSelection: ["no experience", "<= 2 years", "5 years", "10 years"],
    //chips
    select: null,
    requiredSkills: [],
    items: ["Communication", "Time management"],

    //calendar 1
    activePicker1: null,
    date1: null,
    menu1: false,
    checkbox1: false,

    //calender 2
    activePicker2: null,
    date2: null,
    menu2: false,
    checkbox2: false,

    //addjob dialog 3 
    select: null,
    accomodation: "",
    accomodationSelection: [
      "lunch",
      "Sathorn",
      "Bangsue",
      "Thonglor",
    ],

    select: null,
    transportation: "",
    transportationSelection: [
      "Latkrabung",
      "Sathorn",
      "Bangsue",
      "Thonglor",
    ],
    select: null,
    overTime: "",
    overtimeSelection: [
      "200",
      "500",
      "1000",
      "1500",
      "None",
    ],
    select: null,
    laptopProvision: "",
    laptopSelection: [
      "Mac", "ASUS", "Vivo", "MSI", "None"
    ],
    select: null,
    insuranceProvisiongS: "",
    insuranceSelection: [
      "Yes",
      "No",
    ],
    select: null,
    bonusAllowance: "",
    bonusSelection: [
      "5",
      "10",
      "15",
      "None",
    ],
    select: null,
    transportationAllowance: "",
    transportationASelection: [
      "200","500","1000", "None"
    ],
    select: null,
    overTime: "",
    overtimeSelection: [
      "500","1000","1500","2000", "None"
    ],
    select: null,
    leaveQuota: "",
    leaveSelection: [
      "10",
      "15",
      "20",
      "None",
    ],
    select: null,
    insuranceLevel: "",
    insuranceLSelection: [
      "1",
      "2",
      "3",
      "4",
    ],
    select: null,
    additionalProvision: "",
    additionalSelection: [
      "Latkrabung",
      "Sathorn",
      "Bangsue",
      "Thonglor",
    ],
  }),

  watch: {
    //calendar1
    menu1(val) {
      val && setTimeout(() => (this.activePicker1 = "YEAR"));
    },

  //calender 2
    menu2(val) {
      val && setTimeout(() => (this.activePicker2 = "YEAR"));
    },
  },
  methods: {

    save(date) {
      this.$refs.menu1.save(date);
      this.$refs.menu2.save(date);
    },

    OP1(){
      this.dialog1= true;
      this.dialog2= false;
      this.dialog3= false;

    },
    OP2(){
      this.dialog1= false;
      this.dialog2= true;
      this.dialog3= false;

    },
    OP3(){
      this.dialog1= false;
      this.dialog2= false;
      this.dialog3= true;

    },
    //addjob dialog 1
    remove(item) {
      this.requiredSkills.splice(this.requiredSkills.indexOf(item), 1);
      this.requiredSkills = [...this.requiredSkills];
    },
    //addjob dialog 2 left select used question and send/recieve
    addQ() {
      this.questions.push('')
      console.log(this.questions)
    },
    rmq(i) {
      this.questions.splice(i, 1)
    },
    async submit(){
      const config = {
        headers:{
          Authorization : this.$auth.$storage._state["_token.local"],

        }
      }
      await axios.post('https://api.job-application.duckdns.org/addNewJob',{
        
        "role_name" : this.roleName,
        "position" : this.belongedTeam,
        "approx_salary" : this.approximateSalary,
        "number_of_applicants" : this.numAccepting,
        "start_date" : this.date1,
        "application_deadline" : this.date2,
        "manager_name" : this.managerName,
        "working_location" : this.workingLocation,
        "educational_degree_required": this.educationalDegree,
        "required_experiences": this.requiredExperience,
        "required_skills": this.requiredSkills,
        "status": this.status,
        "working_time_details" : this.workingTime,
        "job_description": this.jobDescription,
        "accommodations" : this.accomodation, 
        "bonus": this.bonusAllowance,
        "transportation" : this.transportation,
        "transportation_allowances" : this.transportationAllowance,
        "ot_per_hour" : this.overTime,
        "leave_quota" : this.leaveQuota,
        "laptop_provision" : this.laptopProvision,
        "other_provision" : this.additionalProvision,
        "insurance_provision" : this.insuranceProvision,
        "insurance_level" : this.insuranceLevel,
        "additional_benefits_welfare": this.additionalProvision,
        "question_array" : this.questions},config)
        this.$router.push({name:'list_of_jobs'})
        
      .then(response => {
        console.log('success')
      })
      .catch(err => {
        console.log(err)
      })
    },
  

    testPrint(){
      console.log(this.fullName)
    }
  },
};
</script>
