<template>
  <v-app>

    <!-- addJob1 must be the user's personal details , it must also be an editable form with original content for modification too --> 
    <v-card class="mx-6 my-4" outlined color="transparent">
    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/addJob1">
    <v-text>1 Job Details</v-text>
    </v-btn>
    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/addJob2">
    <v-text>2 General Question</v-text>
    </v-btn>
    <v-btn :ripple="false" text color="natural dark-grey" id="background-hover" nuxt to="/addJob3">
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
                <v-btn align="end" color="natural dark-grey" nuxt to="/OPaddJob2">  
                  Back
                </v-btn>
                <v-btn align="end" color="primary darken-3" nuxt to="/list_of_jobs">  
                  Done
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
  name: " Add Job Page",
  data: () => ({
    return: {
      selectedFile: null,
    },

    //alphabet
    additional: "",
    nameRules: [
      (v) => !!v || "This field is required",
      // (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],

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
      "Latkrabung",
      "Sathorn",
      "Bangsue",
      "Thonglor",
    ],
    select: null,
    leaveQuota: "",
    leaveSelection: [
      "Latkrabung",
      "Sathorn",
      "Bangsue",
      "Thonglor",
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
};
</script>
<style></style>
