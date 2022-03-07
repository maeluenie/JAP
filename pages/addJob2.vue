<template>
  <v-app>

    <!-- addJob2 page will be the second page of job details with navigation after addJob1 --> 

    <v-card class="mx-4 my-4 py-2">
      <v-text-title class="font-weight-bold"
        ><h2 class="mx-8 my-4 text-left">
          Job Details
        </h2></v-text-title
      >
     

      <v-form class="mx-8 mt-2 align-content-center">
        <!-- on real use case situation, the upload method will be included in the main save button -->
        <v-row>
          <v-col cols="12" sm="8" md="6">
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">
                Role Name
              </h5></v-text
            >

            <v-text-field
              v-model="roleName"
              :rules="nameRules"
              label="Role Name"
              required
              outlined
              dense
            ></v-text-field
            >
            <v-text class="font"
              ><h5 class="mx-1 mb-1 text-left">
                Approximate Salary
              </h5></v-text
            >
            <v-text-field
              v-model="citizenID"
              :rules="saralyRules"
              type="number"
              label="Citizen ID"
              required
              dense
              outlined
            ></v-text-field
            >
            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">
                Start Date
              </h5></v-text
            >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date"
              label="startDate"
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
          :active-picker.sync="activePicker1"
          :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
          min="1950-01-01"
          elevation="4"
          class="mb-4"
          @change="save"
        ></v-date-picker>
        

            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">
                Manager Name
              </h5></v-text
            >
            <v-text-field
              v-model="managerName"
              :rules="nameRules"
              label="Manager Name"
              required
              dense
              outlined
            ></v-text-field>
          </v-col>

          <v-col cols="12" sm="8" md="6">

            <v-text class="font"
              ><h5 class="mx-1 mb-2 text-left">
                Belonged Name
              </h5></v-text
            >

            <v-text-field
              v-model="belongedName"
              :rules="nameRules"
              label="Belonged Team"
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
          v-model="date"
          :active-picker.sync="activePicker2"
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
  name: " Job Edit Page",
  data: () => ({
    return: {
      selectedFile: null,
    },
    valid: true,
    citizenID: "",
    saralyRules: [
      (v) => !!v || "This field is required, receiving only integers",
      (v) => (v && v.length == 13) || "Please fill all your Citizen ID",
    ],
    roleName: "",
    lastName: "",
    belongedTeam: "",
    nameRules: [
      (v) => !!v || "This field is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    activePicker1: null,
    date: null,
    menu: false,
    checkbox: false,

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
    activePicker2: null,
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
  },
};
</script>
<style></style>
