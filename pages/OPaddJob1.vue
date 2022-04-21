<template>
  <v-app>

    <!-- addJob1 must be the user's personal details , it must also be an editable form with original content for modification too --> 
    <v-card class="mx-6 my-4" outlined color="transparent">

    <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
    <v-text>1 Job Details</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/OPaddJob2">
    <v-text>2 General Question</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/OPaddJob3">
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
              <v-btn align="end" color="primary darken-3" nuxt to="/OPaddJob2">
                Next
              </v-btn>
            </v-col>
          </v-col>
        </v-row>
      </v-form>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "Add Job Benefits and Wellfare",
  data: () => ({
    return: {
      selectedFile: null,
    },

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
    belongedTeam: "",
    managerName: "",
    educationalDegree: "",
    requiredExperience: "",
    jobDescription: "",
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
  }),

  //calendar 1
  watch: {
    menu1(val) {
      val && setTimeout(() => (this.activePicker1 = "YEAR"));
    },
  },

  //calender 2
  watch: {
    menu2(val) {
      val && setTimeout(() => (this.activePicker2 = "YEAR"));
    },
  },

  //calender 1
  methods: {
    save(date) {
      this.$refs.menu1.save(date);
    },
  },

  //calender 2
  methods: {
    save(date) {
      this.$refs.menu2.save(date);
    },
  },

  //chips
  methods: {
    remove(item) {
      this.requiredSkills.splice(this.requiredSkills.indexOf(item), 1);
      this.requiredSkills = [...this.requiredSkills];
    },
  },
};
</script>
<style></style>