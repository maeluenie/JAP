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
              
            >
              EDIT
            </v-btn>
            
          </template>
          
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog1 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Application form for {{ this.jobs.rolename }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="submit();"> Done </v-btn>
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
                      v-model="jobs.rolename"
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
                      v-model="jobs.approx_salary"
                      :rules="numRules"
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
                          v-model="jobs.start_date"
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
                        v-model="jobs.start_date"
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
                    <v-select
                      v-model="jobs.manager_fullname"
                      :items="selectManager"
                      label="Manager Name"
                      required
                      dense
                      outlined
                    ></v-select>

                    <v-text class="font"
                      ><h5 class="mx-1 mb-2 text-left">Educational Degree</h5></v-text
                    >

                    <v-select
                      v-model="jobs.educational_degree_required"
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
                      v-model="jobs.working_time_details"
                      :rules="numRules"
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
                      v-model="jobs.position"
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
                      v-model="jobs.number_of_applicants"
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
                          v-model="jobs.application_deadline"
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
                        v-model="jobs.application_deadline"
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
                      v-model="jobs.working_location"
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
                      v-model="jobs.required_experiences"
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
                        value="Open for Application"
                        id="Open"
                        v-model="jobs.status"
                        @change="$emit('input', 'Open')"
                      />
                      Open for Application
                    </label>
                    <label for="Close">
                      <input
                        type="radio"
                        name="radio"
                        value="Close Temporarily"
                        id="Close"
                        v-model="jobs.status"
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
                        v-model="jobs.status"
                        @change="$emit('input', 'Urgent')"
                      />Urgent
                    </label>
                  </v-col>

                  <v-col cols="1" sm="1" md="12">
                    <v-text class="font"
                      ><h5 class="mx-1 mb-2 text-left">Required Skills</h5></v-text
                    >

                    <v-combobox
                      v-model="jobs.required_skills"
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

                    v-model="jobs.job_description"
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
              <v-toolbar-title>Edit form for {{ this.jobs.rolename }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="submit()"> Done </v-btn>
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
                      <div align="left">
                        <div class="my-2" v-for="(ques, i) of disQues" :key="i">
                          Question {{i+1}}
                          <v-text-field
                            v-model="ques.question" 
                            required
                            outlined
                            dense
                            placeholder="Enter Question"     
                          />
                    
                          
                          <v-btn
                          color="error"
                          @click="rmoQ(i)"
                          class=" white--text"
                          >
                          <v-icon
                          >
                            mdi-delete
                          </v-icon>Remove
                          </v-btn>

                        </div>

                      
                        <div class="my-2" v-for="(ques, j) in newQues" :key="j">
                          Question {{j+3}}
                          <v-text-field
                            v-model="newQues[j]" 
                            required
                            outlined
                            dense
                            placeholder="Enter Question"     
                          />
                    
                          
                          <v-btn
                          color="error"
                          @click="rmnQ(j)"
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
              <v-btn icon dark @click="dialog3 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Edit form for {{ this.jobs.rolename }} </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="submit()"> Done </v-btn>
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
                      v-model="jobs.accommodations"
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
                      v-model="jobs.transportation"
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
                      v-model="jobs.ot_per_hour"
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
                      v-model="jobs.laptop_provision"
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
                      v-model="jobs.insurance_provision"
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
                      v-model="jobs.bonus"
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
                      v-model="jobs.transportation_allowances"
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
                      v-model="jobs.leave_quota"
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
                      v-model="jobs.other_provision"
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
                      v-model="jobs.insurance_level"
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
                    v-model="jobs.additional_benefits_welfare"
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
                      <!-- <v-btn align="end" color="primary darken-3" @click="submit(); dialog1 = false" nuxt to= "/list_of_jobs">  -->
                      <v-btn align="end" color="primary darken-3" @click="submit();"> 
                        Done
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
import axios from 'axios';
export default {
  middleware:['is-admin'],
  name: "Job Details",
  data () {
    return{
    dialog1: false,
    dialog2: false,
    dialog3: false,

    notifications: false,
    sound: true,
    widgets: false,

    
    newQues:[],
    disQues:[],

    jobs: [],

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

    selectManager: ["Jonathan Doe","Josh Doe","Jane Doe", "Joshua Doe","John Doe","Jennifer Doe","George","Jonny Foo Doe"],
    valid: true,
    approximateSalary: "",
    numAccepting: "",
    workingTime: "",
    numRules: [
      (v) => !!v || "This field is required, receiving only integers",
      // (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],
    
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
    locationSelection: ["Ladkrabang HQ","Latkrabung", "Sathorn", "Bangsue", "Thonglor"],

    select: null,
    educationalDegree: "",
    degreeSelection: ["Associate Degree", "Bachelor's Degree", "Master’s Degree", "Doctoral Degree"],

    select: null,
    belongedTeam: "",
    teamSelection: [
    "product manager",
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
      "Ladkrabang",
      "None"
    ],
    select: null,
    transportation: "",
    transportationSelection: [
      "Vehicle Provisioning",
      "Bus Provisioning",
      "Bangsue",
      "Thonglor",
      "None"
    ],
    select: null,
    overTime: "",
    overtimeSelection: [
      "200",
      "500",
      "1000",
      "1500",
      "2000",
      "None"
    ],
    select: null,
    laptopProvision: "",
    laptopSelection: [
      "Mac", "ASUS TUF-GAMING A15", "Vivo", "MSI", "None"
    ],
    select: null,
    insuranceProvision: "",
    insuranceSelection: [
      "Yes",
      "No",
      "None"
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
      "2000 THB/months","5000 THB/months","10000 THB/months", "None"
    ],
    select: null,
    overTime: "",
    overtimeSelection: [
      500, 1000, 5000, 2000, "None"
    ],
    select: null,
    leaveQuota: "",
    leaveSelection: [
      "3 days/months",
      "10",
      "15",
      "20",
      "None",
    ],
    select: null,
    insuranceLevel: "",
    insuranceLSelection: [
      1,
      2,
      3,
      4,
    ],
    select: null,
    additionalProvision: "",
    additionalSelection: [
      "Latkrabung",
      "Sathorn",
      "Bangsue",
      "None",
    ],
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
        this.disQues = res.data.Jobs.list_of_questions
        console.log(res.data.Jobs.list_of_questions)

        } catch(err) {
          console.log(err)
        }
  },
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
    
    async submit(){
      const config = {
        headers:{
          Authorization : this.$auth.$storage._state["_token.local"],
        }
      }
      await axios.post(`https://api.job-application.duckdns.org/editJob/${this.$route.params.id}`,{
        "job_id": this.jobs.job_id, 
        "rolename": this.jobs.rolename, 
        "position": this.jobs.position, 
        "approx_salary":this.jobs.approx_salary, 
        "number_of_applicants":this.jobs.number_of_applicants, 
        "start_date":this.jobs.start_date, 
        "application_deadline":this.jobs.application_deadline, 
        "manager_name": this.manager_fullname,
        "working_location":this.jobs.working_location, 
        "educational_degree_required":this.jobs.educational_degree_required, 
        "required_experiences":this.jobs.required_experiences, 
        "required_skills":this.jobs.required_skills, 
        "status":this.jobs.status, 
        "working_time_details":this.jobs.working_time_details, 
        "job_description":this.jobs.job_description, 
        "accommodations":this.jobs.accommodations, 
        "bonus":this.jobs.bonus, 
        "transportation":this.jobs.transportation, 
        "transportation_allowances":this.jobs.transportation_allowances, 
        "ot_per_hour":this.jobs.ot_per_hour, 
        "leave_quota":this.jobs.leave_quota, 
        "laptop_provision":this.jobs.laptop_provision, 
        "other_provision":this.jobs.other_provision, 
        "insurance_provision":this.jobs.insurance_provision, 
        "insurance_level":this.jobs.insurance_level, 
        "additional_benefits_welfare":this.jobs.additional_benefits_welfare, 
        "prev_questions":this.disQues,
        "new_questions": this.newQues,
      },config)
      this.$router.push({name:'list_of_jobs'})
    },
   
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
    //editjob dialog 1
    remove(item) {
      this.requiredSkills.splice(this.requiredSkills.indexOf(item), 1);
      this.requiredSkills = [...this.requiredSkills];
    },
    addQ() {
      this.newQues.push('')
      console.log(this.newQues)
    },
    rmnQ(j) {
      this.newQues.splice(j, 1)
    },
    rmoQ(i) {
      this.disQues.splice(i, 1)
    },
    
    testPrint(){
      console.log(this.fullName)
    }
  },
};
</script>
