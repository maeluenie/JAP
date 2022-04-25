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
        <!-- Dialog 1 -->
        <v-dialog
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
            >
              APPLY
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
                <v-btn dark text @click="dialog1 = false"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-8 my-8 py-2">
                <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
                  <v-text>1 Biographical</v-text>
                  </v-btn>

                  <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page2();">
                  <v-text>2 Working Requirement</v-text>
                  </v-btn>

                  <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page3();">
                  <v-text>3 General Evaluation</v-text>
                  </v-btn>

                  <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page4();">
                  <v-text>4 Personalized Evaluation</v-text>
                  </v-btn>

              </v-card>

                <v-card class="mx-4 my-2 py-2">

                  <v-text-title class="font-weight-bold"
                    ><h2 class="mx-8 my-4 text-left">
                      Personal Information
                    </h2>
                  </v-text-title>
                
                  <v-form class="mx-8 mt-5 align-content-center"> 
                  
                      <v-row>


                        <v-col cols="20" sm="20" md="3">
                          <div class="text-center justify-center" >
                            
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
                              width="200"
                              height="200"
                              src="~assets/upload.png"
                            />
                            <p class="mb-1 text-center">Upload your profile image.</p>

                          </div>
                        </v-col>
                          
                        <v-col>
                          <v-row>
                            <v-col cols="20" sm="20" md="12">
                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Full Name</h5></v-text
                              >

                              <v-text-field
                                v-model="roleName"
                                :rules="nameRules"
                                label="Full Name"
                                required
                                outlined
                                dense
                              ></v-text-field>
                    
                            </v-col>
                          </v-row>

                          <v-row>
                            <v-col>
                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Contact Number</h5></v-text
                              >

                              <v-text-field
                                v-model="contactNum"
                                :rules="numRules"
                                label="Number"
                                required
                                outlined
                                dense
                              ></v-text-field>

                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Nationality</h5></v-text
                              >

                              <v-select
                                v-model="nationality"
                                :items="nationalitySelection"
                                :rules="nameRules"
                                label="Nationality"
                                required
                                outlined
                                dense
                              >
                              </v-select>
                            </v-col>
                            <v-col>
                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Email Address</h5></v-text
                              >

                              <v-text-field
                                v-model="emailAdress"
                                :rules="nameRules"
                                label="Email Address"
                                required
                                outlined
                                dense
                              ></v-text-field>

                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Religious</h5></v-text
                              >

                              <v-select
                                v-model="religious"
                                :items="religiousSelection"
                                :rules="nameRules"
                                label="Religious"
                                required
                                outlined
                                dense
                              ></v-select>
                            </v-col>
                          </v-row>
                        </v-col>



                        <v-col>
                          <v-row>
                            <v-col cols="20" sm="20" md="12">
                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Citizen ID/ Passport ID</h5></v-text
                              >

                              <v-text-field
                                v-model="idCard"
                                :rules="numRules"
                                label="Citizen ID/ Passport ID"
                                required
                                outlined
                                dense
                              ></v-text-field>
                    
                            </v-col>
                          </v-row>
                          
                          <v-row>
                            <v-col>
                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Age</h5></v-text
                              >

                              <v-text-field
                                v-model="age"
                                :rules="numRules"
                                label="Age"
                                required
                                outlined
                                dense
                              ></v-text-field>

                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Degree</h5></v-text
                              >

                              <v-select
                                v-model="Degree"
                                :items="degreeSelection"
                                :rules="nameRules"
                                label="Degree"
                                required
                                outlined
                                dense
                              ></v-select>
                            </v-col>
                            
                            <v-col>
                              <v-text class="font"
                                ><h5 class="mx-1 mb-2 text-left">Date of Birth</h5></v-text
                              >
                            <v-menu
                              ref="menu"
                              v-model="menu"
                              :close-on-content-click="false"
                              transition="scale-transition"
                              offset-y
                              min-width="auto"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="date"
                                  label="Date of Birth"
                                  append-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                  outlined
                                  dense
                                ></v-text-field>
                              </template>
                              <v-date-picker
                                v-model="date"
                                :active-picker.sync="activePicker"
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
                                ><h5 class="mx-1 mb-2 text-left">GPA</h5></v-text
                              >

                              <v-text-field
                                v-model="GPA"
                                :rules="numRules"
                                label="GPA"
                                required
                                outlined
                                dense
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-col>

                      </v-row>
                      <v-row>
                        <v-col>
                          <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">
                          Statement of Purpose
                        </h5></v-text>

                        <v-textarea
                        v-model="statement"
                        :rules="statement"
                        label="Statement of Purpose"
                        required
                        outlined
                        dense
                        ></v-textarea>
                        </v-col>
                      </v-row>
                        
                      <v-row>
                        <v-col>  
                          <v-text class="font"
                            ><h5 class="mb-2 text-left">Gender</h5></v-text
                          >
                          <label for="Male">
                            <input
                              type="radio"
                              name="radio"
                              value="Male"
                              id="Male"
                              @change="$emit('input', 'Male')"
                            />
                            Male
                          </label>
                          <label for="Female">
                            <input class="mx-2"
                              type="radio"
                              name="radio"
                              value="Female"
                              id="Female"
                              @change="$emit('input', 'Female')"
                            />
                            Female</label
                          >

                          <label for="Non-Binary">
                            <input class="mx-2"
                              type="radio"
                              name="radio"
                              value="Yes"
                              id="Yes"
                              @change="$emit('input', 'Yes')"
                            />
                            Non-Binary
                          </label>
                        </v-col>
                        <v-col>
                          <v-text class="font"
                            ><h5 class="mx-1 mb-2 text-left">Marital Status</h5></v-text
                          >

                          <v-select
                            v-model="maritalStatus"
                            :items="maritalSelection"
                            :rules="nameRules"
                            label="Marital Status"
                            required
                            outlined
                            dense
                          ></v-select>
                        </v-col>  
                        <v-col>
                          <v-text class="font"
                            ><h5 class="mx-1 mb-2 text-left">Military Status</h5></v-text
                          >

                          <v-select
                            v-model="militaryStatus"
                            :items="militarySelection"
                            :rules="nameRules"
                            label="Military Status"
                            required
                            outlined
                            dense
                          ></v-select>
                        </v-col>
                      </v-row>
                      
                  
                        
                    <v-divider class="my-2"></v-divider>
                  </v-form>

                  <v-text-title class="font-weight-bold">
                    <h2 class="mx-8 my-4 text-left">
                      Partner's Information
                    </h2>
                  </v-text-title>

                  <v-form class="mx-8 mt-2 align-content-center">
                    <v-row>
                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">First Name</h5></v-text
                        >

                        <v-text-field
                          v-model="firstName"
                          :rules="nameRules"
                          label="FirstName"
                          required
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Middle Name</h5></v-text
                        >

                        <v-text-field
                          v-model="middleName"
                          :rules="nameRules"
                          label="Middle Name"
                          required
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Last Name</h5></v-text
                        >

                        <v-text-field
                          v-model="lastName"
                          :rules="nameRules"
                          label="Last Name"
                          required
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                            ><h5 class="mx-1 mb-2 text-left">Occupation</h5></v-text
                          >
                        <v-select 
                          v-model= "occupation"
                          :items="occupationSelection"
                          :rules="[(v) => !!v || 'This field is required']"
                          label="Occupation"
                          required
                          outlined
                          dense
                        ></v-select>
                      </v-col>
                      <v-col cols="16" sm="8" md="8">
                        <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Working Company</h5></v-text
                        >

                        <v-text-field
                          v-model="workingCompany"
                          :rules="nameRules"
                          label="Working Company"
                          required
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                            ><h5 class="mx-1 mb-2 text-left">Number of Children</h5></v-text
                          >
                        <v-select 
                          v-model= "numChild"
                          :items="childSelection"
                          :rules="[(v) => !!v || 'This field is required']"
                          label="Number of Children"
                          required
                          outlined
                          dense
                        ></v-select>
                      </v-col>

                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Contact Number</h5></v-text
                        >

                        <v-text-field
                          v-model="partnerNum"
                          :rules="numRules"
                          label="Contact Number"
                          required
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                      <v-col cols="16" sm="8" md="4">
                        <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Email Address</h5></v-text
                        >

                        <v-text-field
                          v-model="partnerEmail"
                          :rules="nameRules"
                          label="Email Address"
                          required
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                      
                      <v-col>
                          <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">
                          Address
                        </h5></v-text>

                        <v-textarea
                        v-model="statement"
                        :rules="statement"
                        label="Partner's Address"
                        required
                        outlined
                        dense
                        ></v-textarea>
                        </v-col>
                      
                      
                    </v-row>
                  
                  </v-form>
                <v-col class="text-right">
                <v-btn align="right" color="primary darken-3" @click="page2();">  
                  Next
                </v-btn>          
                </v-col>
                </v-card>
          
          </v-card>

        </v-dialog>

        <!-- Dialog2 -->
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
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog2 = false"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-8 my-8 py-2">
                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page1();">
                <v-text>1 Biographical</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
                <v-text>2 Working Requirement</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page3();">
                <v-text>3 General Evaluation</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page4();">
                <v-text>4 Personalized Evaluation</v-text>
                </v-btn>

              </v-card>

              <v-card class="mx-4 my-2 py-2">
                <v-text-title class="font-weight-bold"

                  ><h2 class="mx-8 my-4 text-left">
                    Experience and Achievements
                  </h2></v-text-title>
              


                <v-form class="mx-8 mt-2 align-content-center">

                  <v-row>
                    <v-col cols="1" sm="1" md="12">
                      <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Resume/CV</h5></v-text
                      >
                    
                        <v-file-input
                          accept=".pdf"
                          :rules="[(v) => !!v || 'This field is required']"
                          label="No file chosen"
                          outlined
                          dense
                        ></v-file-input>
                        
                      <v-text class="font"
                      ><h5 class="mx-1 mb-2 text-left">
                        Statement of Purpose
                      </h5></v-text>

                      <v-textarea
                      v-model="statement"
                      :rules="statement"
                      label="Statement of Purpose"
                      required
                      outlined
                      dense
                      ></v-textarea>

                      <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Additional Achievements and Certificates</h5></v-text
                      >

                      <v-file-input
                          accept=".pdf"
                          :rules="[(v) => !!v || 'This field is required']"
                          label="No file chosen"
                          outlined
                          dense
                      ></v-file-input>
                      
                      <v-row>
                        
                        <v-text class="font"
                          ><h5 class="mx-5 mb-2 text-left">Do you have a driving license?</h5></v-text
                        >
                        <label for="Yes1">
                          <input
                            type="radio"
                            name="radio1"
                            value="Yes1"
                            id="Yes1"
                            @change="$emit('input', 'Yes1')"
                          />
                          Yes
                        </label>
                        <label for="No1">
                          <input class="mx-2"
                            type="radio"
                            name="radio1"
                            value="No1"
                            id="No1"
                            @change="$emit('input', 'No1')"
                          />
                          No</label
                        >

                        <v-text class="font"
                          ><h5 class="mx-5 mb-2 text-left">Do you have a car?</h5></v-text
                        >
                        <label for="Yes2">
                          <input class="mx-2"
                            type="radio"
                            name="radio2"
                            value="Yes2"
                            id="Yes2"
                            @change="$emit('input', 'Yes2')"
                          />
                          Yes
                        </label>
                        <label for="No2">
                          <input class="mx-2"
                            type="radio"
                            name="radio2"
                            value="No2"
                            id="No2"
                            @change="$emit('input', 'No2')"
                          />
                          No</label
                        >
                        <v-text class="font"
                          ><h5 class="mx-5 mb-2 text-left">Do you have a PC?</h5></v-text
                        >
                        <label for="Yes3">
                          <input 
                            type="radio"
                            name="radio3"
                            value="Yes3"
                            id="Yes3"
                            @change="$emit('input', 'Yes3')"
                          />
                          Yes
                        </label>
                        <label for="No3">
                          <input class="mx-2"
                            type="radio"
                            name="radio3"
                            value="No3"
                            id="No3"
                            @change="$emit('input', 'No3')"
                          />
                          No</label
                        >
                        
                      </v-row>
                      
                    </v-col>
                  </v-row>
                  <v-divider class="my-2"></v-divider>
                </v-form>

                <v-text-title class="font-weight-bold"><h2 class="mx-8 my-4 text-left">
                  Abilities and Language Proficiencies
                </h2></v-text-title>

                <v-form class="mx-8 mt-2 align-content-center">
                  <v-row>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Foreign Language</h5></v-text
                        >
                      <v-select 
                        v-model= "foreignLanguage"
                        :items="languageSelection"
                        :rules="[(v) => !!v || 'This field is required']"
                        label="Foreign Language"
                        required
                        outlined
                        dense
                      ></v-select>
                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Proficiency level</h5></v-text
                      >
                      <v-select 
                          v-model= "proficiencyLevel"
                          :items="levelSelection"
                          :rules="[(v) => !!v || 'This field is required']"
                          label="Proficiency level"
                          required
                          outlined
                          dense
                        ></v-select>
                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Special Abilities</h5></v-text
                      >
                      <v-text-field
                        v-model="specialAbilities"
                        :rules="specialAbilities"
                        type="number"
                        label="Special Abilities"
                        required
                        dense
                        outlined
                      >
                      </v-text-field>
                      
                    </v-col>
                    <v-divider class="my-2"></v-divider>
                  </v-row>
                  <v-divider class="my-2"></v-divider>
                </v-form>
                <v-text-title class="font-weight-bold"

                ><h2 class="mx-8 my-4 text-left">
                  Emergency Contact
                </h2></v-text-title>
              
                <v-form class="mx-8 mt-2 align-content-center">
                  <v-row>
                  
                    <v-col cols="16" sm="8" md="4">
                    <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Contact Full Name</h5></v-text
                    >
                    <v-text-field
                      v-model="contactName"
                      :rules="contactName"
                      type="number"
                      label="Contact Full Name"
                      required
                      dense
                      outlined
                    >
                    </v-text-field>
                    <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Additional Contact Name</h5></v-text
                    >
                    <v-text-field
                      v-model="additionalName"
                      :rules="additionalName"
                      type="number"
                      label="Additional Contact Name"
                      required
                      dense
                      outlined
                    >
                    </v-text-field>
                    <v-text-field
                      v-model="additionalName"
                      :rules="additionalName"
                      type="number"
                      label="Additional Contact Name"
                      required
                      dense
                      outlined
                    >
                    </v-text-field>

                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Contact Number</h5></v-text
                      >
                      <v-text-field
                        v-model="contactNumber"
                        :rules="contactNumber"
                        type="number"
                        label="Contact Number"
                        required
                        dense
                        outlined
                      >
                      </v-text-field>
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Contact Number</h5></v-text
                      >
                      <v-text-field
                        v-model="contactNumber"
                        :rules="contactNumber"
                        type="number"
                        label="Contact Number"
                        required
                        dense
                        outlined
                      >
                      </v-text-field><v-text-field
                        v-model="contactNumber"
                        :rules="contactNumber"
                        type="number"
                        label="Contact Number"
                        required
                        dense
                        outlined
                      >
                      </v-text-field>
                      </v-col>
                  
                    <v-col cols="16" sm="8" md="4">
                    <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Family Status</h5></v-text
                      >
                    <v-select 
                      v-model= "familyStatus"
                      :items="statusSelection"
                      :rules="[(v) => !!v || 'This field is required']"
                      label="Family Status"
                      required
                      outlined
                      dense
                    ></v-select>
                    <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Family Status</h5></v-text
                        >
                      <v-select 
                        v-model= "familyStatus"
                        :items="statusSelection"
                        :rules="[(v) => !!v || 'This field is required']"
                        label="Family Status"
                        required
                        outlined
                        dense
                      ></v-select>
                      <v-select 
                        v-model= "familyStatus"
                        :items="statusSelection"
                        :rules="[(v) => !!v || 'This field is required']"
                        label="Family Status"
                        required
                        outlined
                        dense
                      ></v-select>
                    </v-col>
              
                  </v-row>
              </v-form>
              
              <v-col class="text-right">
                <v-btn align="end" color="natural dark-grey" @click="page1();">  
                  Back
                </v-btn>
                <v-btn align="end" color="primary darken-3" @click="page3();"> 
                  Next
                </v-btn>
              </v-col>
            </v-card>
          </v-card>

        </v-dialog>

        <!-- Dialog3 -->
        <v-dialog
          v-model="dialog3"
          fullscreen
          hide-overlay
          transition="dialog-top-transition"
        >
          <!-- this is the container of the overview of the form dialog for job application form -->
          
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog4 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog4 = false"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
                <v-card class="mx-6 my-4" outlined color="transparent">

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page1();">
                <v-text>1 Biographical</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page2();">
                <v-text>2 Working Requirement</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" >
                <v-text>3 General Evaluation</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page4();">
                <v-text>4 Personalized Evaluation</v-text>
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
                <v-btn align="end" color="natural dark-grey" @click="page2();">  
                  Back
                </v-btn>
                <v-btn align="end" color="primary darken-3" @click="page4();"> 
                  Next
                </v-btn>
              </v-col>
              </v-row>
            </v-form>
          </v-card>
          </v-card>

        </v-dialog>

        <!-- Dialog4 -->
        <v-dialog
          v-model="dialog4"
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
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog2 = false"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>

              <v-card class="mx-6 my-4" outlined color="transparent">

              <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page1();">
              <v-text>1 Biographical</v-text>
              </v-btn>

              <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page2();">
              <v-text>2 Working Requirement</v-text>
              </v-btn>

              <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="page3();">
              <v-text>3 General Evaluation</v-text>
              </v-btn>

              <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
              <v-text>4 Personalized Evaluation</v-text>
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
                <v-btn align="end" color="natural dark-grey" @click="page3();">  
                  Back
                </v-btn>
                <v-btn align="end" color="primary darken-3" @click="dialog4 = false"> 
                  Submit
                </v-btn>
              </v-col>
              </v-row>
            </v-form>
          </v-card>
          </v-card>

        </v-dialog>

        <!-- <v-btn
          color="primary darken-2"
          class="ml-1 mr-4 my-2"
          nuxt
          to="/APform1"
        >
          APPLY2
        </v-btn> -->
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
    dialog4: false,
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
    page1(){
      this.dialog1= true;
      this.dialog2= false;
      this.dialog3= false;
      this.dialog4= false;
    },
    page2(){
      this.dialog1= false;
      this.dialog2= true;
      this.dialog3= false;
      this.dialog4= false;
    },
    page3(){
      this.dialog1= false;
      this.dialog2= false;
      this.dialog3= true;
      this.dialog4= false;
    },
    page4(){
      this.dialog1= false;
      this.dialog2= false;
      this.dialog3= false;
      this.dialog4= true;
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
