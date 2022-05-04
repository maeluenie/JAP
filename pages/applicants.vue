<template>
  <div id="app">
    <v-app id="inspire">
      <v-data-table
        :headers="headers"
        :items="applicants"
        :search="search"
        @click:row="submittedform"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title class="mx-4 font-weight-bold"
              >Suitable Applicants</v-toolbar-title
            >
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search by Full Name / Applied Jobs / Teams"
              single-line
              hide-details
            >
            <v-spacer></v-spacer>
            </v-text-field>

            <v-spacer></v-spacer>
            <v-dialog
              v-model="dialog1"
              fullscreen
              hide-overlay
              transition="dialog-bottom-transition"
            >
              <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog1 = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Applicants Submitted form</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog1 = false"> Done </v-btn>
                <!-- this line must link a function to submit the data to the database -->
              </v-toolbar-items>
            </v-toolbar>
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
                      counter="250"
                      maxlength="250"
                      ></v-textarea>
                      <span>{{ totalcharacter }} characters</span>
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

                      </v-row>
                    </v-form>
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
                
                <!-- pack into json send through API -->
                <v-btn align="end" color="primary darken-3" @click="dialog4 = false"> 
                  Done
                </v-btn>
              </v-col>
              </v-row>
            </v-form>
          </v-card>

          </v-card>

            </v-dialog>
            <v-dialog v-model="detailsDialog" max-width="500px">
              <!-- this section is the "new item" button on the top-right of the page -->
              <!-- <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                New Item
              </v-btn>
            </template> -->

              <!-- this v-card section is the dialog of item's modification ( initially, it is edit item page )
            <!-- <v-card>
              <v-card-title>
                <span class="text-h5">{{ dialogTitle }}</span>
              </v-card-title>
  
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.name"
                        label="Dessert name"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.calories"
                        label="Calories"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.fat"
                        label="Fat (g)"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.carbs"
                        label="Carbs (g)"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.protein"
                        label="Protein (g)"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card> -->
              <v-card>
                <v-card-title>
                  <span class="font-weight-bold">Applicant's Details</span>
                </v-card-title>

                <v-card-text>
                  this will appear below the dialog title
                  <v-container>
                    this will be the applicant's detail from the application,
                    appearing within the card's container form</v-container
                  >
                </v-card-text>

                <v-card-actions>
                  <v-btn
                    class="my-2 mx-2"
                    color="red darken-1"
                    text
                    @click="deleteApplicantConfirm"
                  >
                    Delete
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn
                    class="my-2 mx-2"
                    color="blue darken-1"
                    outlined
                    @click="closeDetailsDialog"
                  >
                    Close
                  </v-btn>
                  <v-btn
                    class="my-2 mx-2 white--text"
                    color="blue darken-1"
                    @click="verify"
                    >Verify
                    <!-- must be changed to verification function ( change the state(?) ) -->
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-dialog v-model="sendEmailDialog" max-width="500px">
              <v-card>
                <!-- initial line of code below is <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title> -->
                <v-card-title class="text-h6"
                  >Do you want to send this person an offer?</v-card-title
                >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="closeSendEmailDialog"
                    >Cancel</v-btn
                  >
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="sendEmailOfferConfirm"
                    >Confirm</v-btn
                  >
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="openApplicantDetailsDialog(item)">
            mdi-magnify
          </v-icon>
          <!-- this commented section is used for the deletion of that specific item ( Desserts as in the source code )
        <!-- <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon> -->
          <v-icon small @click="openOfferDialog(item)"> mdi-send </v-icon>
        </template>
        <!-- this section is used to display a reset button when there are no items -->
        <!-- <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template> -->
      </v-data-table>
    
    </v-app>
      <v-btn @click="dispApp"> test </v-btn>

  </div>
</template>

<script>
export default {
  name: "Applicants Page",
  data: () => ({
    detailsDialog: false,
    sendEmailDialog: false,
    dialog1: false,
    search: "",
    headers: [
      {
        text: "Applicants",
        align: "start",
        value: "name",
      },
      { text: "Job Role", value: "role", filterable: true },
      { text: "Job Department", value: "department", filterable: true },
      { text: "Telephone Number", value: "tel_number", filterable: false },
      { text: "Location", value: "location", filterable: false },
      { text: "Application Deadline", value: "deadline", filterable: false },
      { text: "Approved Date", value: "approved", filterable: false },
      { text: "Validation", value: "validate", sortable: false },
      { text: "Sent Offer", value: "contact", sortable: false },
      { text: "Actions", value: "actions", sortable: false },
      // {
      //   text: "Dessert (100g serving)",
      //   align: "start",
      //   sortable: false,
      //   value: "name",
      // },
      // { text: "Calories", value: "calories" },
      // { text: "Fat (g)", value: "fat" },
      // { text: "Carbs (g)", value: "carbs" },
      // { text: "Protein (g)", value: "protein" },
      // { text: "Actions", value: "actions", sortable: false },
    ],
    applicants: [],
    editedIndex: -1,
    // editedItem: {
    //   name: "",
    //   calories: 0,
    //   fat: 0,
    //   carbs: 0,
    //   protein: 0,
    // },
    // for "passed" and "failed" field, it should also consider the approved date also.
    passed: {
      validate: "Yes",
    },
    failed: {
      validate: "No",
    },
    offered: {
      contact: "Yes",
    },
    // defaultItem: {
    //   name: "",
    //   calories: 0,
    //   fat: 0,
    //   carbs: 0,
    //   protein: 0,
    // },
  }),

  computed: {
    dialogTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },

  watch: {
    detailsDialog(val) {
      val || this.closeDetailsDialog();
    },
    sendEmailDialog(val) {
      val || this.closeSendEmailDialog();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    submittedform(){
      this.dialog1 = true;
    },

    initialize() {
      this.applicants = [
        // retrieve data from the API, taking from the database.
        {
          name: "John Doe",
          role: "UX/UI Designer",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "George Doe",
          role: "Back-End Developer ( Javascript )",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Johnny Doe",
          role: "Back-End Developer ( Golang )",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Jonathan Doe",
          role: "Back-End Developer ( Golang )",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Joni Doe",
          role: "Front-End Developer ( React.js )",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Jinny Doe",
          role: "DevOps",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Jelly Doe",
          role: "DevOps",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Giorno Doe",
          role: "Program Manager",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Giorgio Doe",
          role: "Cybersecurity",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Jitney Doe",
          role: "Networking and Routing",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
        {
          name: "Silly Doe",
          role: "Hardware Programmer ( Python )",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          approved: "March 29th, 2023",
          deadline: "March 29th, 2023",
          validate: "No",
          contact: "No",
        },
      ];
    },

    openApplicantDetailsDialog(item) {
      this.editedIndex = this.applicants.indexOf(item);
      // this.editedItem = Object.assign({}, item);
      this.detailsDialog = true;
    },
    verify() {
      // this is the function used to verify applicants
      if (this.editedIndex > -1) {
        Object.assign(this.applicants[this.editedIndex], this.passed);
      } else {
        this.applicants.push(this.passed);
      }
      this.closeDetailsDialog();
      // this function must continues to send validation success to the database, via the API too!
    },
    closeDetailsDialog() {
      this.detailsDialog = false;
      this.$nextTick(() => {
        // this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    openOfferDialog(item) {
      this.editedIndex = this.applicants.indexOf(item);
      // this.editedItem = Object.assign({}, item);
      this.sendEmailDialog = true;
    },
    sendEmailOfferConfirm() {
      // this.applicants.splice(this.editedIndex, 1);
      if (this.applicants[this.editedIndex].validate == "No") {
        console.log(this.applicants[this.editedIndex].name , "has not been validated yet")
        this.closeSendEmailDialog();
      } else {
        Object.assign(this.applicants[this.editedIndex], this.offered);
        console.log("Offer submitted to",this.applicants[this.editedIndex].name)
        this.closeSendEmailDialog();
      }
    },
    closeSendEmailDialog() {
      this.sendEmailDialog = false;
      this.$nextTick(() => {
        // this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    deleteApplicantConfirm() {
      this.applicants.splice(this.editedIndex, 1);
      this.detailsDialog = false;
    },
    dispApp(){   // for testing purposes, don't forget to remove this line of code before launching the product
      console.log(this.applicants)
    }
  },
};
</script>
