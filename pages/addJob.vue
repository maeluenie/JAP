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
              <v-btn dark text nuxt to="/list_of_jobs"> Done </v-btn>
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
                      :max="
                        new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
                          .toISOString()
                          .substr(0, 10)
                      "
                      min="1950-01-01"
                      @change="save"
                    ></v-date-picker>
                  </v-menu>

                  <v-text class="font"
                    ><h5 class="mx-1 mb-2 text-left">Manager Name</h5></v-text
                  >
                  <v-text-field
                    v-model="managerName"
                    :rules="nameRules"
                    label="Manager Name"
                    required
                    dense
                    outlined
                  ></v-text-field>

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

                  <v-text-field
                    v-model="workingTime"
                    :rules="numRules"
                    type="number"
                    label="Working Time Details"
                    required
                    dense
                    outlined
                  >
                  </v-text-field>
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
                      :max="
                        new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
                          .toISOString()
                          .substr(0, 10)
                      "
                      min="1950-01-01"
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
                      @change="$emit('input', 'Open')"
                    />
                    Open for Application
                  </label>
                  <label for="Close">
                    <input
                      type="radio"
                      name="radio"
                      value="Close"
                      id="Close"
                      @change="$emit('input', 'Close')"
                    />
                    Close Temporarily</label
                  >
                  <label for="Urgent">
                    <input
                      type="radio"
                      name="radio"
                      value="Urgent"
                      id="Urgent"
                      @change="$emit('input', 'Urgent')"
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
                  <v-btn dark text nuxt to="/list_of_jobs"> Done </v-btn>
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
              <v-btn dark text nuxt to="/list_of_jobs"> Done </v-btn>
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
                    label="Annual Bonus Minimum Allowance"
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
                  :rules="additional"
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
                    <v-btn align="end" color="primary darken-3" nuxt to = "/list_of_jobs"> 
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
export default {
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
    Questions: [{ ques: "" }],

    valid: true,
    citizenID: "",
    citizenID_Rules: [
      (v) => !!v || "This field is required, receiving only integers",
      (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],

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
    lastName: "",
    managerName: "",
    requiredExperience: "",
    jobDescription: "",
    additional: "",//dialog3
    nameRules: [
      (v) => !!v || "This field is required",
      // (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    
    select: null,
    workingLocation: "",
    locationSelection: ["Latkrabung", "Sathorn", "Bangsue", "Thonglor"],

    select: null,
    educationalDegree: "",
    degreeSelection: ["Associate Degree", "Bachelor’s Degree", "Master’s Degree", "Doctoral Degree"],

    select: null,
    belongedTeam: "",
    teamSelection: ["Team A", "Team B", "Team C", "Team D"],

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
      "5%",
      "10%",
      "15%",
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
      "Latkrabung",
      "Sathorn",
      "Bangsue",
      "Thonglor",
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
    addField(value, fieldType) {
      fieldType.push({ value: "" });
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1);
    },

    testPrint(){
      console.log(this.fullName)
    }
  },
};
</script>
