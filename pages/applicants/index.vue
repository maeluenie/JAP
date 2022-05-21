<template>
  <div id="app">
    
    <v-app id="inspire">
      <v-data-table 
        :headers="headers"
        :id ="applicants.applicant_id"
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
           
     
          
 <!-- dialog1 -->
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
                            <!-- <div class="ml-2">{{ this.Applicant.fullname }}</div> -->
                            <v-text-field
                              v-model="Applicant.fullname"
                              disabled
                              outlined
                              dense
                            ></v-text-field>
                            <!-- <div v-for="(form,i) in Applicant" :key="i">
                              {{form}}
                              <div v-for="(list,i) in form" :key ="i">
                              {{list.form}}
                              </div> -->
                            
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
                              v-model="Applicant.citizen_id"
                              disabled
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
                              v-model="Applicant.contact_number"
                              disabled
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
                              v-model="Applicant.email"
                              disabled
                              outlined
                              dense
                            ></v-text-field>

                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">Religious</h5></v-text
                            >

                            <v-text-field
                              v-model="Applicant.religion"
                              disabled
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            
                            
                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">Nationality</h5></v-text
                            >

                            <v-text-field
                              v-model="Applicant.nationality"
                              disabled
                              outlined
                              dense
                            >
                            </v-text-field>
                            
                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">University</h5></v-text
                            >

                            <v-text-field
                              v-model="Applicant.university"
                              disabled
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
                              v-model="Applicant.age"
                              disabled
                              outlined
                              dense
                            ></v-text-field>

                            <v-text class="font"
                              ><h5 class="mx-1 mb-2 text-left">Faculty</h5></v-text
                            >

                            <v-text-field
                              v-model="Applicant.degree"
                              disabled
                              outlined
                              dense
                            ></v-text-field>
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
                                v-model="Applicant.DOB"
                                disabled
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
                              v-model="Applicant.GPA"
                              disabled
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
                        v-model="Applicant.address"
                        disabled
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
                              disabled
                              v-model="Applicant.gender"
                            />
                            Male
                          </label>
                          <label for="Female">
                            <input class="mx-2"
                              type="radio"
                              name="radio1"
                              value="Female"
                              id="Female"
                              disabled
                              v-model="Applicant.gender"
                            />
                            Female</label
                          >

                          <label for="Non-Binary">
                            <input class="mx-2"
                              type="radio"
                              name="radio1"
                              value="Yes"
                              id="Nonbinary"
                              disabled
                              v-model="Applicant.gender"
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
                            disabled
                            v-model="Applicant.marital_status"
                          />
                          Yes
                        </label>
                        <label for="No1">
                          <input class="mx-2"
                            type="radio"
                            name="radio2"
                            value= 0
                            id="No1"
                            disabled
                            v-model="Applicant.marital_status"
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
                            disabled
                            v-model="Applicant.military_status"
                          />
                          Yes
                        </label>
                        <label for="No2">
                          <input class="mx-2"
                            type="radio"
                            name="radio3"
                            value= 0
                            id="No2"
                            disabled
                            v-model="Applicant.military_status"
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
                          v-model="Partner.partner_fullname"
                          disabled
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
                      <v-text-field 
                        v-model="Partner.partner_occupation"
                        disabled
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="16" sm="8" md="8">
                      <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Working Company</h5></v-text
                      >

                      <v-text-field
                        v-model="Partner.partner_company"
                        disabled
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Number of Children</h5></v-text
                        >
                      <v-text-field 
                        v-model="Partner.number_of_children"
                        disabled
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>

                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Contact Number</h5></v-text
                      >

                      <v-text-field
                        v-model="Partner.partner_contact_number"
                        disabled
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Email Address</h5></v-text
                      >

                      <v-text-field
                        v-model="Partner.partner_email"
                        disabled
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
                      v-model="Partner.partner_address"
                      disabled
                      outlined
                      dense
                      ></v-textarea>
                      </v-col>
                    
                    
                  </v-row>
                
                </v-form>

<!-- dialog2 -->
                <v-text-title class="font-weight-bold"

                  ><h2 class="mx-8 my-4 text-left">
                    Experience and Achievements
                  </h2></v-text-title>
              


                <v-form class="mx-8 mt-2 align-content-center">

                  <v-row>
                    <v-col cols="1" sm="1" md="12">
                        
                      <v-text class="font"
                      ><h5 class="mx-1 mb-2 text-left">
                        Statement of Purpose
                      </h5></v-text>

                      <v-textarea
                      v-model="Skill.statement_of_purpose"
                      disabled
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
                            disabled
                            type="radio"
                            name="radio1"
                            value= 1
                            id="Yes1"
                            v-model="Skill.driving_license"
                          />
                          Yes
                        </label>

                        <label for="No1">
                          <input class="mx-2"
                            disabled
                            type="radio"
                            name="radio1"
                            value= 0
                            id="No1"
                            v-model="Skill.driving_license"
                          />
                          No</label
                        >

                        <v-text class="font"
                          ><h5 class="mx-5 mb-2 text-left">Do you have a car?</h5></v-text
                        >
                        <label for="Yes2">
                          <input class="mx-2"
                            disabled
                            type="radio"
                            name="radio2"
                            value= 1
                            id="Yes2"
                            v-model="Skill.car_possession"
                          />
                          Yes
                        </label>
                        <label for="No2">
                          <input class="mx-2"
                            disabled
                            type="radio"
                            name="radio2"
                            value= 0
                            id="No2"
                            v-model="Skill.car_possession"
                          />
                          No</label
                        >
                        <v-text class="font"
                          ><h5 class="mx-5 mb-2 text-left">Do you have a PC?</h5></v-text
                        >
                        <label for="Yes3">
                          <input 
                            disabled
                            type="radio"
                            name="radio3"
                            value= 1 
                            id="Yes3"
                            v-model="Skill.pc_possession"
                          />
                          Yes
                        </label>
                        <label for="No3">
                          <input class="mx-2"
                            disabled
                            type="radio"
                            name="radio3"
                            value= 0
                            id="No3"
                            v-model="Skill.pc_possession"
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
                      <v-text-field 
                        v-model= "Skill.foreign_language"
                        disabled
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Proficiency level</h5></v-text
                      >
                      <v-text-field 
                          v-model= "Skill.foreign_language"
                          disabled
                          outlined
                          dense
                        ></v-text-field>
                    </v-col>
                    <v-col cols="16" sm="8" md="4">
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Special Abilities</h5></v-text
                      >
                      <v-text-field
                        v-model="Skill.special_ability"
                        disabled
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
                      v-model="Emergency.emergencycont_fullname"
                      disabled
                      dense
                      outlined
                    >
                    </v-text-field>
                    <v-text class="font"
                        ><h5 class="mx-1 mb-2 text-left">Additional Contact Name</h5></v-text
                    >
                    <v-text-field
                      v-model="Emergency.emergencycont_additional_fullname"
                      disabled
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
                        v-model="Emergency.emergencycont_contact_number"
                        disabled
                        required
                        dense
                        outlined
                      >
                      </v-text-field>
                      <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Contact Number</h5></v-text
                      >
                      <v-text-field
                        v-model="Emergency.emergencycont_contact_number"
                        disabled
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
                    <v-text-field 
                      v-model="Emergency.emergencycont_relationship"
                      disabled
                      outlined
                      dense
                    ></v-text-field>
                    <v-text class="font"
                          ><h5 class="mx-1 mb-2 text-left">Family Status</h5></v-text
                        >
                    <v-text-field 
                      v-model="Emergency.emergencycont_relationship"
                      disabled
                      outlined
                      dense
                    ></v-text-field>
                    </v-col>
              
                  </v-row>
              </v-form>
              

<!-- display answer dialog -->
            <v-text-title class="font-weight-bold"

              ><h2 class="mx-8 my-4 text-left">
                General Questions
              </h2></v-text-title>
          


            <v-form class="mx-8 mt-2 align-content-center">

              <v-row>
                <v-col cols="1" sm="1" md="12">

                  <div v-for="(question,i) in Questions" :key="question.id">
                  <v-card  class="mx-4 my-2 py-2">
                    <v-row class="mt-2">
                      <v-col cols="20" sm="20" md="12">
                  
                      <v-text class="font"
                      ><h5 class="mx-1 mb-2 text-left">
                        Question {{i+1}}. {{ question.questions}}
                      </h5></v-text
                    >
                      <v-text-field
                        v-model="question.answer" 
                        disabled
                        required
                        outlined
                        dense 
                      />
              
                </v-col>
              </v-row>
            </v-card>
          </div>
        <v-col class="text-right">
          <v-text class="font"
            ><h5 class="mx-1 mb-2 text-left">
              Is this Applicant Suitable?
            </h5></v-text>
          <v-btn align="end" color="natural dark-grey" @click="deleteApplicantConfirm();">  
            NO
          </v-btn>
          <v-btn align="end" color="primary darken-3" @click="confirm();"> 
            YES
          </v-btn>
        </v-col>
      </v-col>
      </v-row>
    </v-form>
    </v-card>
        

    
      </v-dialog>
            
          </v-toolbar>
          
        </template>
        
          <!-- this commented section is used for the deletion of that specific item ( Desserts as in the source code ) -->
        <!-- <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon> -->
          <!-- <v-icon small @click="openOfferDialog(item)"> mdi-send </v-icon> -->
        
        <!-- this section is used to display a reset button when there are no items -->
        <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template>
      
      </v-data-table>
    </v-app>
   

  </div>
  
</template>

<script>
import axios from "axios";
export default {
  middleware:['is-admin'],

  data(){
    return{
    detailsDialog: false,
    sendEmailDialog: false,
    dialog1: false,
    search: "",
    headers: [
      {
        text: "Applicants",
        align: "start",
        value: "fullname",
      },
      { text: "Job Role", value: "rolename", filterable: true },
      { text: "Job Department", value: "department", filterable: true },
      { text: "Telephone Number", value: "contact_number", filterable: false },
      { text: "Location", value: "working_location", filterable: false },
      { text: "Application Deadline", value: "application_deadline", filterable: false },
      { text: "Sent Offer", value: "sent_offer", sortable: false },

    ],
    applicants: [],
    editedIndex: -1,
    
    Applicant:[],
    Application: [],
    Emergency: [],
    Job:[],
    Manager: [],
    Organization: [],
    Partner:[],
    Questions:[],
    Skill:[],

    id : 0,
    passed: {
      validate: "Yes",
    },
    failed: {
      validate: "No",
    },
    offered: {
      contact: "Yes",
    },
    
    }
    
  },
  async created() {
    const config = {
      headers: {
        Authorization : this.$auth.$storage._state["_token.local"],
        Accept: "application/json"
      }
    };
    try{
    const res = await axios.get("https://api.job-application.duckdns.org/getAllApplicants",config);
    this.applicants = res.data;
    console.log(res.data)

    } catch(err) {
      console.log(err)
    }
  },
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

  // created() {
  //   this.initialize();
  // },

  methods: {
    confirm(){
      console.log(this.id)
      this.$router.push({name:'adminSelect', params: {id:this.id}}); 
      
    },
  
    async submittedform(item){
      this.dialog1 = true;
      console.log(item)
      this.id = item.application_id.toString()
      console.log(this.id)

      const config = {
      headers: {
        Authorization : this.$auth.$storage._state["_token.local"],
        Accept: "application/json"
      }
      };
      try{
      // const res = await axios.get(`https://api.job-application.duckdns.org/getApplication/${this.$route.params.id}`,config);
      const res = await axios.get(`https://api.job-application.duckdns.org/getApplication/`+item.application_id.toString(),config);
      this.Applicant = res.data.Applicant;
      this.Application = res.data.Application;
      this.Emergency = res.data.Emergency;
      this.Job = res.data.Job;
      this.Manager = res.data.Manager;
      this.Organization = res.data.Organization;
      this.Partner = res.data.Partner;
      this.Questions = res.data.Questions;
      this.Skill = res.data.Skill;
      console.log(res.data.Applicant)

      } catch(err) {
        console.log(err)
      }
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
      this.dialog1 = false;
    },
    dispApp(){   // for testing purposes, don't forget to remove this line of code before launching the product
      console.log(this.applicants)
    }
  }

};
</script>
