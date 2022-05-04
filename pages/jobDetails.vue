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

            <!-- for the accommodations, vehicles the data will provide something, so check the whether is it null or not might be better such as
            v-if="jobDetails.accommodations != null" might be better, copy those characters and place it below at "Accommodations at Ladkrabang"-->
            
            <!-- So, if it's null, display grey, but if it provides anything, -->

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
            <!-- specifically replacing the text here to be jobDetails.accommodations, so the text will be display as an overlay after hovering -->
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
        <!-- Dialog 1 -->
        <v-dialog
          v-if="role===true"
          v-model="dialog1"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
        >
         
          <!-- this is the container of the overview of the form dialog for job application form -->
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary darken-2"
              class="ml-1 mr-4 my-2"
              v-bind="attrs"
              v-on="on"
              v-if="role===true"
            >
              EDIT
            </v-btn>
            
          </template>
          
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog1 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog1 = false"> Done </v-btn>
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
              <v-btn icon dark @click="dialog2 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Edit form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog2 = false"> Done </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-6 my-4" outlined color="transparent">

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
              <v-btn icon dark @click="dialog3 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Edit form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog3 = false"> Done </v-btn>
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
                      <v-btn align="end" color="primary darken-3" @click="dialog7 = false"> 
                        Submit
                      </v-btn>
                    </v-col>
                  </v-col>
                </v-row>
              </v-form>
            </v-card>
          </v-card>

        </v-dialog>
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
    dialog2: false,
    dialog3: false,

    notifications: false,
    sound: true,
    widgets: false,

    Questions: [{ ques: "" }],

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

    statement:'',
    totalcharacter : 0,
    role: true,

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

    addField(value, fieldType) {
      fieldType.push({ value: "" });
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1);
    },

    charCount(){

         this.totalcharacter = this.message.length;

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
