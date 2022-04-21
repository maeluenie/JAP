<template>
  <v-app>
    <!-- this page will be how users can submit their purpose and required information for the job, full page overlay can be used -->
    
    <v-card class="mx-6 my-4" outlined color="transparent">

    <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" nuxt to ="/APform1">
    <v-text>1 Biographical</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/APform2">
    <v-text>2 Working Requirement</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/APform3">
    <v-text>3 General Evaluation</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/APform4">
    <v-text>4 Personalized Evaluation</v-text>
    </v-btn>

    </v-card>


    <v-card class="mx-4 my-2 py-2">
      <v-text-title class="font-weight-bold"

        ><h2 class="mx-8 my-4 text-left">
          Personal Information
        </h2></v-text-title>
    
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

      <v-text-title class="font-weight-bold"><h2 class="mx-8 my-4 text-left">
        Partner's Information
      </h2></v-text-title>

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
          <v-btn align="end" color="primary darken-3" nuxt to="/APform2">  Next </v-btn>
        </v-col> 
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
    foreignLanguage1: "",
    languageSelection: [
      "English",
      "Chinese",
      "Islam",
      "Hindi",
      "French",
      "Spanish",
      "Others",
    ],

    select: null,
    foreignLanguage2: "",
    languageSelection: [
      "English",
      "Chinese",
      "Islam",
      "Hindi",
      "French",
      "Spanish",
      "Others",
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
