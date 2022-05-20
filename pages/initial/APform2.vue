
<template>


  <v-app>
    
    <v-card class="mx-6 my-4" outlined color="transparent">

    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to ="/APform1">
    <v-text>1 Biographical</v-text>
    </v-btn>

    <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" nuxt to="/APform2">
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
              <label for="Yes">
                <input
                  type="radio"
                  name="radio"
                  value="Yes"
                  id="Yes"
                  @change="$emit('input', 'Yes')"
                />
                Yes
              </label>
              <label for="No">
                <input class="mx-2"
                  type="radio"
                  name="radio"
                  value="No"
                  id="No"
                  @change="$emit('input', 'No')"
                />
                No</label
              >

              <v-text class="font"
                ><h5 class="mx-5 mb-2 text-left">Do you have a car?</h5></v-text
              >
              <label for="Yes">
                <input class="mx-2"
                  type="radio"
                  name="radio"
                  value="Yes"
                  id="Yes"
                  @change="$emit('input', 'Yes')"
                />
                Yes
              </label>
              <label for="No">
                <input class="mx-2"
                  type="radio"
                  name="radio"
                  value="No"
                  id="No"
                  @change="$emit('input', 'No')"
                />
                No</label
              >
              <v-text class="font"
                ><h5 class="mx-5 mb-2 text-left">Do you have a PC?</h5></v-text
              >
              <label for="Yes">
                <input 
                  type="radio"
                  name="radio"
                  value="Yes"
                  id="Yes"
                  @change="$emit('input', 'Yes')"
                />
                Yes
              </label>
              <label for="No">
                <input class="mx-2"
                  type="radio"
                  name="radio"
                  value="No"
                  id="No"
                  @change="$emit('input', 'No')"
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
        <v-btn align="end" color="natural dark-grey" nuxt to="/APform1">  
          Back
        </v-btn>
        <v-btn align="end" color="primary darken-3" nuxt to="/APform3">  
          Next
        </v-btn>
      </v-col>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "APform2",
    data: () => ({
    return: {
      selectedFile: null,
      //ngong
    },
    
    select: null,
    foreignLanguage: "",
    LanguageSelection: ["Thai", "English", "French", "Chinese"],

    select: null,
    proficiencyLevel: "",
    levelSelection: ["Novice", "Intermediate", "Advanced", "Superior", "Distinguished"],

    select: null,
    familyStatus: "",
    statusSelection: ["Thai", "English", "French", "Chinese"],

  }),
  methods: {
    async selectFile1(e) {
      const file = e.target.files[0];

      /* Make sure file exists */
      if (!file) return;

      /* create a reader */
      const readData = (f) =>  new Promise((resolve) => {
          const reader = new FileReader();
          reader.onloadend = () => resolve(reader.result);
          reader.readAsDataURL(f);
      });

      /* Read data */
      const data = await readData(file);

      // /* upload the converted data */
      // const instance = this.$cloudinary.upload(data, {
      //   folder: 'upload-examples',
      //   uploadPreset: 'your-upload-preset',
      // })
    },
    async selectFile2(e) {
      const file = e.target.files[0];

      /* Make sure file exists */
      if (!file) return;

      /* create a reader */
      const readData = (f) =>  new Promise((resolve) => {
          const reader = new FileReader();
          reader.onloadend = () => resolve(reader.result);
          reader.readAsDataURL(f);
      });

      /* Read data */
      const data = await readData(file);

      // /* upload the converted data */
      // const instance = this.$cloudinary.upload(data, {
      //   folder: 'upload-examples',
      //   uploadPreset: 'your-upload-preset',
      // })
    }
  }  
}
</script>
<style></style>
