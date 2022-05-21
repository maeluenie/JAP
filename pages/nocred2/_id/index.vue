<template>
  <!-- jobDetails page will contain the details upon that specific role, 
  the page should be changed to something with the roleID at the end of the URL -->
<v-app>
    <v-card class="mx-4 my-4">
      <v-card-title class="mx-4"> {{ this.jobs.rolename }} </v-card-title>

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
              <div class="ml-2">{{ this.jobs.position }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <!-- <v-icon class="mr-2" color="black">mdi-map-marker</v-icon> -->
              <div class="font-weight-bold">Location:</div>
              <div class="ml-2">{{ this.jobs.working_location }}</div> </v-layout
            ><v-layout row class="my-2">
              <!-- <v-icon class="mr-2" color="black">mdi-clock</v-icon> -->
              <div class="font-weight-bold">Team:</div>
              <div class="ml-2">{{ this.jobs.working_time_details }}</div>
            </v-layout>
          </v-layout>
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Manager's Name:</div>
              <div class="ml-2">{{ this.jobs.manager_fullname }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Manager's Role:</div>
              <div class="ml-2">{{ this.jobs.manager_role }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Required Experience:</div>
              <div class="ml-2">{{ this.jobs.required_experiences }}</div>
            </v-layout>
          </v-layout>
          <v-layout column align-content-start justify-start class="mx-2">
            <v-layout row class="my-2">
              <div class="font-weight-black">Application Deadline:</div>
              <div class="ml-2">{{ this.jobs.application_deadline }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Start Date:</div>
              <div class="ml-2">{{ this.jobs.start_date }}</div>
            </v-layout>
            <v-layout row class="my-2">
              <div class="font-weight-black">Salary Range:</div>
              <div class="ml-2">{{ this.jobs.approx_salary }}</div>
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
            {{ this.jobs.job_description }}
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
          <v-tooltip bottom color="primary" v-if="this.jobs.accommodations != 'None'">      

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
            <span>Accommodations at {{ this.jobs.accommodations }}</span> 
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

          <v-tooltip bottom color="primary" v-if="this.jobs.transportation != 'None'">
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
            <span> {{this.jobs.transportation}} Type of Provisioning with {{ this.jobs.transportation_allowances }} </span>
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

          <v-tooltip bottom color="primary" v-if="this.jobs.laptop_provision != 'None'">
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
            <span> {{this.jobs.laptop_provision}} </span>
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

          <v-tooltip bottom color="primary" v-if="this.jobs.bonus != 'None'">
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
            <span> {{ this.jobs.bonus }}% for overtime bonus </span>
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
            v-for="item in this.jobs.required_skills"
            :key="item"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-chip
                color="primary darken-2"
                v-bind="attrs"
                v-on="on"
                class="mx-1"
              >
                {{ item }}
              </v-chip>
            </template>
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
              @click="getQues()"
            >
              APPLY
            </v-btn>
            
          </template>
          
          <!-- if role is applicants -->
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog1 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog1 = false; submit()"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-8 my-8 py-2">
                <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
                  <v-text>1 Biographical</v-text>
                  </v-btn>

                  <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="AP2();">
                  <v-text>2 Working Requirement</v-text>
                  </v-btn>

                  <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="AP3();">
                  <v-text>3 General Evaluation</v-text>
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
                      <v-col>
                        <v-row>
                          <v-col cols="20" sm="20" md="12">
                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">Full Name</h5></v-text
                            >

                            <v-text-field
                              v-model="fullName"
                              :rules="nameRules"
                              label="Full Name"
                              required
                              outlined
                              dense
                            ></v-text-field>
                  
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
                              v-model="citizenID"
                              :rules="citizenID_Rules"
                              label="Citizen ID/ Passport ID"
                              required
                              outlined
                              dense
                            ></v-text-field>
                  
                          </v-col>
                        </v-row>
                      </v-col>
                      <v-col>
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
                  
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>

                        <v-row>
                          <v-col>
                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">Email Address</h5></v-text
                            >

                            <v-text-field
                              v-model="email"
                              :rules="emailRules"
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
                          <v-col>
                            
                            
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
                            
                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">University</h5></v-text
                            >

                            <v-text-field
                              v-model="university"
                              :rules="nameRules"
                              label="University"
                              required
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>

                      <v-col>
                        
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
                              ><h5 class="mx-1 mb-2 text-left">Faculty</h5></v-text
                            >

                            <v-select
                              v-model="faculty"
                              :items="facultySelection"
                              :rules="nameRules"
                              label="faculty"
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
                              v-model="gpa"
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
                          Address
                        </h5></v-text>

                        <v-textarea
                        v-model="address"
                        :rules="nameRules"
                        label="Address"
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
                              name="radio1"
                              value="Male"
                              id="Male"
                              v-model="gender"
                            />
                            Male
                          </label>
                          <label for="Female">
                            <input class="mx-2"
                              type="radio"
                              name="radio1"
                              value="Female"
                              id="Female"
                              v-model="gender"
                            />
                            Female</label
                          >

                          <label for="Non-Binary">
                            <input class="mx-2"
                              type="radio"
                              name="radio1"
                              value="Yes"
                              id="Nonbinary"
                              v-model="gender"
                            />
                            Non-Binary
                          </label>
                        </v-col>
                        <v-col>
                          <v-text class="font"
                            ><h5 class="mx-1 mb-2 text-left">Marital Status</h5></v-text
                          >

                          <label for="Yes1">
                          <input class="mx-2"
                            type="radio"
                            name="radio2"
                            value= 1
                            id="Yes1"
                            v-model="maritalStatus"
                          />
                          Yes
                        </label>
                        <label for="No1">
                          <input class="mx-2"
                            type="radio"
                            name="radio2"
                            value= 0
                            id="No1"
                            v-model="maritalStatus"
                          />
                          No</label> 
                        </v-col>  
                        <v-col>
                          <v-text class="font"
                            ><h5 class="mx-1 mb-2 text-left">Military Status</h5></v-text
                          >

                          <label for="Yes2">
                          <input class="mx-2"
                            type="radio"
                            name="radio3"
                            value= 1
                            id="Yes2"
                            v-model="militaryStatus"
                          />
                          Yes
                        </label>
                        <label for="No2">
                          <input class="mx-2"
                            type="radio"
                            name="radio3"
                            value= 0
                            id="No2"
                            v-model="militaryStatus"
                          />
                          No</label>
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
                    <v-col cols="20" sm="26" md="12">
                      <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Full Name</h5></v-text
                      >

                      <v-text-field
                        v-model="partnerFullname"
                        :rules="nameRules"
                        label="Full Name"
                        required
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    
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
                        :rules="emailRules"
                        label="Email Address"
                        required
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    
                    <v-col>
                        <v-text class="font"
                      ><h5 class="mx-1 mb-2 text-left">
                        Partner's Address
                      </h5></v-text>

                      <v-textarea
                      v-model="partnerAddress"
                      :rules="nameRules"
                      label="Partner's Address"
                      required
                      outlined
                      dense
                      ></v-textarea>
                      </v-col>
                    
                    
                  </v-row>
                
                </v-form>
              <v-col class="text-right">
              <v-btn align="right" color="primary darken-3" @click="AP2();">  
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
                <v-btn dark text @click="dialog2 = false; submit()"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
            <v-card class="mx-8 my-8 py-2">
                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="AP1();">
                <v-text>1 Biographical</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="natural dark-grey" id="background-hover">
                <v-text>2 Working Requirement</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="AP3();">
                <v-text>3 General Evaluation</v-text>
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
                    
                        <input
                          accept=".pdf"
                          type="file"
                          id="file"
                          :rules="[(v) => !!v || 'This field is required']"
                          label="No file chosen"
                          outlined
                          dense
                          @change ="handleFile"
                        />
                        
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
                      counter="250"
                      maxlength="250"
                      ></v-textarea>

                      
                      <v-row>
                        
                        <v-text class="font"
                          ><h5 class="mx-5 mb-2 text-left">Do you have a driving license?</h5></v-text
                        >
                        <label for="Yes1">
                          <input
                            type="radio"
                            name="radio1"
                            value= 1
                            id="Yes1"
                            v-model="haveLicense"
                          />
                          Yes
                        </label>
                        <label for="No1">
                          <input class="mx-2"
                            type="radio"
                            name="radio1"
                            value= 0
                            id="No1"
                            v-model="haveLicense"
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
                            value= 1
                            id="Yes2"
                            v-model="haveCar"
                          />
                          Yes
                        </label>
                        <label for="No2">
                          <input class="mx-2"
                            type="radio"
                            name="radio2"
                            value= 0
                            id="No2"
                            v-model="haveCar"
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
                            value= 1 
                            id="Yes3"
                            v-model="havePC"
                          />
                          Yes
                        </label>
                        <label for="No3">
                          <input class="mx-2"
                            type="radio"
                            name="radio3"
                            value= 0
                            id="No3"
                            v-model="havePC"
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
                        :rules="nameRules"
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
                      v-model="emergencyName1"
                      :rules="nameRules"
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
                      v-model="emergencyName2"
                      :rules="nameRules"
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
                        v-model="emergencyNum1"
                        :rules="numRules"
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
                        v-model="emergencyNum2"
                        :rules="numRules"
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
                      v-model= "familyStatus1"
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
                        v-model= "familyStatus2"
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
                <v-btn align="end" color="natural dark-grey" @click="AP1();">  
                  Back
                </v-btn>
                <v-btn align="end" color="primary darken-3" @click="AP3();"> 
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
              <v-btn icon dark @click="dialog3 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Application form for {{ this.jobDetails.jobName }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog3 = false , submit()"> Submit </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
                <v-card class="mx-6 my-4" outlined color="transparent">

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="AP1();">
                <v-text>1 Biographical</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" @click="AP2();">
                <v-text>2 Working Requirement</v-text>
                </v-btn>

                <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" >
                <v-text>3 General Evaluation</v-text>
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
                    
                    <div v-for="(question,i) in all_q" :key="i" >
                      
                      Question {{i+1}}.{{ question.question}}

                      <v-text-field
                        v-model="question.answer" 
                        required
                        outlined
                        dense
                        placeholder="Enter Answer"     
                      />
                      
                    </div>
                    <p>user's answer</p>
                      {{ all_q2 }}

                  </v-col>

                      
                      <v-col class="text-right">
                        <v-btn align="end" color="natural dark-grey" @click="AP2();">  
                          Back
                        </v-btn>
                        <v-btn align="end" color="primary darken-3" @click="submit();dialog3=false"> 
                          Submit
                        </v-btn>
                        
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
import axios from 'axios'

export default {
  name: "Job Details",
  computed: {
    all_q2(){
      return this.all_q.map(value=>{return {
        question_id: value.question_id,
        answer: value.answer
      }})
    }
  },
  data (){
    return{
    dialog1: false,
    dialog2: false,
    dialog3: false,

    notifications: false,
    sound: true,
    widgets: false,
    
    Questions: [],
    jobs:[],
    all_q:[],

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

    
    //Dialog 1 
    
    fullName: "",
    nationality: "",
    statement: "",
    partnerFullname:"",
    partnerAddress:"",
    workingCompany:"",
    address:"",
    gender:"",
    
    email: "",
    partnerEmail:"",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],

    valid: true,
    contactNum: "",
    age:"",
    gpa:"",
    partnerNum: "",

    valid: true,
    citizenID: "",
    citizenID_Rules: [
      (v) => !!v || "This field is required, receiving only integers",
      (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],

    select: null,
    nationality: "",
    nationalitySelection:
      ["Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Anguillan",
       "Citizen of Antigua and Barbuda", "Argentine", "Armenian", "Australian", "Austrian", 
       "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi",	 "Barbadian", "Belarusian", 
       "Belgian", "Belizean", "Beninese", "Bermudian", "Bhutanese", "Bolivian",
       	"Botswanan", "Brazilian", "British", "Bruneian", "Bulgaria", "Burkinan", "Burmese", 
         "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean", 
        " Cayman Islander", "Central African",	"Chadian", "Chilean", "Chinese", "Colombian", 
        "Comoran", "Congolese (Congo)", "Costa Rican", "Croatian", "Cuban", "Cymraes", "Cymro",
         "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican", "Dutch","East Timorese", 
         "Ecuadorean", "Egyptian", "Emirati", "English", "Eritrean", "Estonian", "Ethiopian", "Faroese",
          "Fijian", "Filipino", "Finnish", "French", "Gabonese", "Gambian", "Georgian", "German",
           "Ghanaian", "Gibraltarian", "Greek", "Greenlandic", "Grenadian", "Guamanian", "Guatemalan", 
        "Hungarian", "Icelandic", "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli",	"Italian", 
        "Ivorian", "Jamaican", "Japanese", "Jordanian", "Kazakh", "Kenyan", "Kittitian", "Lao", "Latvian"
        ,"Malaysian", "Maldivian", "Malian", "Mexican", "Nepalese", "New Zealander", "Nigerian", "Nigerien",
       "North Korean", "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan", "Palestinian", "Polish",
        "Portuguese", "Russian", "Saudi Arabian", "Scottish", "Singaporean", 
        "South Korean", "Spanish", "Sri Lankan", "Swedish", "Swiss", "Syrian", "Taiwanese", "Thai", "Turkish",  
        "Venezuelan", "Vietnamese", "Vincentian", "Wallisian", "Welsh", "Yemeni", "Zambian", "Zimbabwean"],


    select: null,
    religious: "",
    religiousSelection: [
      "Buddhism",
      "Christianity",
      "Islam",
      "Hinduism",
      "Sikhism",
      "Atheist",
      "Others",
    ],

    select: null,
    faculty: "",
    facultySelection: [
      "Faculty of Engineering", "Faculty of Economics", "Faculty of Arts", "Chemistry","Computer Science & Information Technology"
    ],

    select: null,
    maritalStatus: "",
    maritalSelection: [
      "single", "married", "widowed", "divorced", "separated"
    ],

    select: null,
    militaryStatus: "",
    militarySelection: [
      "single", "married", "widowed", "divorced", "separated"
    ],

    select: null,
    occupation: "",
    occupationSelection: [
      "Engineer","Computer Engineer","UX/UI designer","Doctor","Dentist","Physical Therapist","Nurse Practitioner","Flight Attendant","Others"
    ],

    select: null,
    numChild: "",
    childSelection: [
      "1","2","3","4","5","6","7","8","None"
    ],

    activePicker: null,
    date: null,
    menu: false,
    checkbox: false,

    //Dialog 2
    file:"",
    statement:"",
    specialAbilities:"",
    emergencyName1:"",
    emergencyName2:"",
    emergencyNum1:"",
    emergencyNum2:"",
    date: "",
    university: "",
    haveLicense:"",
    haveCar: "",
    havePC: "",


    select: null,
    foreignLanguage: "",
    languageSelection: ["Thai", "English", "French", "Chinese"],

    select: null,
    proficiencyLevel: "",
    levelSelection: ["Novice", "Intermediate", "Advanced", "Superior", "Distinguished"],

    select: null,
    familyStatus1: "",
    statusSelection: ["Partner", "Legal Guardian", "Aunt", "Brother", "Cousin", "Father", "Mother", "Grandfather", "Grandmother", "Other"],
    
    select: null,
    familyStatus2: "",
    statusSelection: ["Partner", "Legal Guardian", "Aunt", "Brother", "Cousin", "Father", "Mother", "Grandfather", "Grandmother", "Other"],
    
    
    //common rules
    nameRules: [(v) => !!v || "This field is required"],
    numRules: [
      (v) => !!v || "This field is required, receiving only integers",
    ],

    //Dialog3 display from admin(jobDetails)
  
  }
  },
  async created() {
      const config = {
        headers:{
          Authorization : this.$auth.$storage._state["_token.local"],
          'Accept':'application/json'
        }
      }

      try{
        const res = await axios.get(`https://api.job-application.duckdns.org/getSingleJob/${this.$route.params.id}`,config);
        this.jobs = res.data.Jobs;

        } catch(err) {
          console.log(err)
        }
  },
  
  watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = "YEAR"));
    },
  },
  methods: {
    async qa(){
      for(let i of this.Questions)
      this.all_q.push({
        ...i,
        answer:""
      })
      console.log(this.all_q)
    },
    async getQues() {
    const config = {
      headers:{
        'Accept':'application/json'
      }
    }
    try{
    const res = await axios.get(`https://api.job-application.duckdns.org/getSetOfJobQuestions/${this.$route.params.id}`,config);
    this.Questions = res.data;
    this.qa()
    console.log(res.data)

    } catch(err) {
      console.log(err)
    }
  },
    handleFile(event){
      
      this.file=event.target.files[0];
      },

    save(date) {
      this.$refs.menu.save(date);
    },
    AP1(){
      this.dialog1= true;
      this.dialog2= false;
      this.dialog3= false;
      this.dialog4= false;
    },
    AP2(){
      this.dialog1= false;
      this.dialog2= true;
      this.dialog3= false;
      this.dialog4= false;
    },
    AP3(){
      this.dialog1= false;
      this.dialog2= false;
      this.dialog3= true;
      this.dialog4= false;
    },

    async submit(){
      let formData = new FormData();
      formData.append('pdf',this.file);
      formData.append('applicant_fullname',this.fullName);
      formData.append('applicant_citizen_id',this.citizenID);
      formData.append('applicant_contact_number',this.contactNum);
      formData.append('applicant_email',this.email);
      formData.append('age',this.age); 
      formData.append('DOB',this.date);
      formData.append('nationality',this.nationality);
      formData.append('religion',this.religious);
      formData.append('university',this.university);
      formData.append('degree',this.faculty);
      formData.append('GPA',this.gpa);
      formData.append('address',this.address);
      formData.append('gender',this.gender);
      formData.append('marital_status',this.maritalStatus);
      formData.append('military_status',this.militaryStatus);
      formData.append('partner_fullname',this.partnerFullname);
      formData.append('partner_occupation',this.occupation);
      formData.append('number_of_children',this.numChild);
      formData.append('partner_contact_number',this.partnerNum);
      formData.append('partner_email',this.partnerEmail);
      formData.append('partner_address',this.partnerAddress);
      formData.append('partner_company',this.workingCompany);
      formData.append('emergency_fullname',this.emergencyName1);
      formData.append('emergency_contact_number',this.emergencyNum1);
      formData.append('emergency_relationship',this.familyStatus1);
      formData.append('additional_fullname',this.emergencyName2);
      formData.append('additional_contact_number',this.emergencyNum2);
      formData.append('additional_relationship',this.familyStatus2);
      formData.append('statement_of_purpose',this.statement);
      formData.append('driving_license',this.haveLicense);
      formData.append('car_possession',this.haveCar);
      formData.append('pc_possession',this.havePC);
      formData.append('foreign_language',this.foreignLanguage);
      formData.append('proficiency',this.proficiencyLevel);
      formData.append('special_ability',this.specialAbilities);
      formData.append('job_id',3);
      formData.append('all_questions',this.all_q.map(value=>{return {
        question_id: value.question_id,
        answer: value.answer
      }}));
      
      // http://rienru.tk/foo/catchparams.php
      // http://143.198.77.144:8000/uploadApplication
      await axios.post('https://api.job-application.duckdns.org/uploadApplication', formData,{
        
        headers: {
          'Content-Type': 'multipart/form-data'
        }
        
      })

      // }))
      // .then(response => {
      //   console.log('success')
      // })
      // .catch(err => {
      //   console.log(err)
      // })
    },

    testPrint(){
      console.log(this.fullName)
    },
  },
};
</script>
