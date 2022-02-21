<template>
  <v-card class = "mx-4 mt-4">
    <v-card-title class = "mx-4 font-weight-bold">
      Suitable Applicants
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search by Full Name / Applied Jobs / Teams"
        single-line
        hide-details
      ></v-text-field>
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "Applicants Page",
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Applicants",
          align: "start",
          value: "name",
        },
        { text: "Job Department", value: "department", filterable: false},
        { text: "Telephone Number", value: "tel_number", filterable: false },
        { text: "Location", value: "location", filterable: false },
        { text: "Application Deadline", value: "deadline" , filterable: false},
        { text: "Approved Date", value: "approved", filterable: false },
      ],
      desserts: [
        {
          name: "John Doe",
          department: 159,
          tel_number: 6.0,
          location: 24,
          deadline: 4.0,
          approved: "1%",
        },
        {
          name: "George Doe",
          department: 237,
          tel_number: 9.0,
          location: 37,
          deadline: 4.3,
          approved: "1%",
        },
        {
          name: "Johnny Doe",
          department: 262,
          tel_number: 16.0,
          location: 23,
          deadline: 6.0,
          approved: "7%",
        },
        {
          name: "Jonathan Doe",
          department: 305,
          tel_number: 3.7,
          location: 67,
          deadline: 4.3,
          approved: "8%",
        },
        {
          name: "Joni Doe",
          department: 356,
          tel_number: 16.0,
          location: 49,
          deadline: 3.9,
          approved: "16%",
        },
        {
          name: "Jinny Doe",
          department: 375,
          tel_number: 0.0,
          location: 94,
          deadline: 0.0,
          approved: "0%",
        },
        {
          name: "Jelly Doe",
          department: 392,
          tel_number: 0.2,
          location: 98,
          deadline: 0,
          approved: "2%",
        },
        {
          name: "Giorno Doe",
          department: 408,
          tel_number: 3.2,
          location: 87,
          deadline: 6.5,
          approved: "45%",
        },
        {
          name: "Giorgio Doe",
          department: 452,
          tel_number: 25.0,
          location: 51,
          deadline: 4.9,
          approved: "22%",
        },
        {
          name: "Jitney Doe",
          department: 518,
          tel_number: 26.0,
          location: 65,
          deadline: 7,
          approved: "6%",
        },
        {
          name: "Silly Doe",
          department: 518,
          tel_number: 26.0,
          location: 65,
          deadline: 7,
          approved: "6%",
        },
      ],
    };
  },
};
</script>
