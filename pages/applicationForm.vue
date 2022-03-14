<template>
  <v-app>
    <!-- this page will be how users can submit their purpose and required information for the job, full page overlay can be used -->

    <v-card class="mx-4 my-4 py-2">
      <v-text-title class="font-weight-bold"
        ><h2 class="mx-8 mb-4 text-center">
          Job Application Form
        </h2></v-text-title
      >
      <v-row class="mx-4 justify-center align-center">
        <v-col>
          <div class="text-center justify-center" centered>
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
              centered
              width="150"
              height="150"
              src="~assets/upload.png"
            />
            <p class="mb-1 text-center">Upload your profile image.</p>
          </div>
        </v-col>
      </v-row>

      <v-form class="mx-4 mt-2 align-content-center" elevation-1>
        <!-- on real use case situation, the upload method will be included in the main save button -->
        <v-container bg>
          <v-layout
            row
            wrap
            align-center
            align-content-center
            justify-center
            class="mx-1"
          >
            <v-flex class="mx-2">
              <v-text class="font"
                ><h5 class="mb-1 text-left">Full Name</h5>
              </v-text>
              <v-text-field
                v-model="fullName"
                :rules="nameRules"
                label="Full Name"
                required
                outlined
                dense
              ></v-text-field>
            </v-flex>
            <v-flex class="mx-2">
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
            </v-flex>
          </v-layout>
        </v-container>

        <v-col class="text-right">
          <v-btn align="end" color="primary darken-3">
            Next
          </v-btn>
        </v-col>
      </v-form></v-card
    >
  </v-app>
</template>

<script>
export default {
  name: " Application Form Page",
  data: () => ({
    return: {
      selectedFile: null,
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
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
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
