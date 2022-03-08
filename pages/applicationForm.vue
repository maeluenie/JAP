<template>
  <v-app>

    <!-- this page will be how users can submit their purpose and required information for the job -->

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

      <v-form class="mx-8 mt-2 align-content-center">
        <!-- on real use case situation, the upload method will be included in the main save button -->
        <v-row>
          <v-col cols="12" sm="8" md="6">
            <v-text-field
              v-model="firstName"
              :rules="nameRules"
              label="First Name"
              required
              outlined
              dense
            ></v-text-field
            ><v-text-field
              v-model="citizenID"
              :rules="citizenID_Rules"
              type="number"
              label="Citizen ID"
              required
              dense
              outlined
            ></v-text-field
            ><v-text-field
              v-model="name"
              :rules="nameRules"
              label="Full Name"
              required
              dense
              outlined
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="8" md="6">
            <v-text-field
              v-model="lastName"
              :rules="nameRules"
              label="Last Name"
              required
              dense
              outlined
            ></v-text-field>
            <v-select
              v-model="religion"
              :items="religionSelection"
              :rules="[(v) => !!v || 'This field is required']"
              label="Religion"
              required
              outlined
              dense
            ></v-select>
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
            label="Birthday date"
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
          dense
          :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
          min="1950-01-01"
          @change="save"
        ></v-date-picker>
      </v-menu>
          </v-col>
        </v-row> </v-form
    ></v-card>
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
    firstName: "",
    lastName: "",
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
    menu (val) {
      val && setTimeout(() => (this.activePicker = 'YEAR'))
    },
  },
  methods: {
    save (date) {
      this.$refs.menu.save(date)
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
