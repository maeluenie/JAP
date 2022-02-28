<template>
  <v-card class="mx-4 mt-4">
    <v-card-title class="mx-4 font-weight-bold">
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
    <v-data-table :headers="headers" :items="applicants" :search="search"
      ><template v-slot:item.control="item">
        <v-btn
          class="mx-2"
          fab
          dark
          x-small
          color="primary"
          @click="deleteItem(item)"
          ref="deleteItem"
        >
          <v-icon dark @click="$refs.deleteItem.click()">mdi-send</v-icon>
        </v-btn>
        <v-dialog
        hide-overlay
        persistent
          v-model="dialogDelete"
          transition="dialog-bottom-transition"
          max-width="700px"
          class="elevation-1"
        >
          <v-card>
            <v-card-title class="text-h6"
              >Please confirm your action to contact this applicant</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card> </v-dialog></template
    ></v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "Applicants Page",
  data() {
    return {
      dialogDelete: false,
      search: "",
      headers: [
        {
          text: "Applicants",
          align: "start",
          value: "name",
        },
        { text: "Job Department", value: "department", filterable: false },
        { text: "Telephone Number", value: "tel_number", filterable: false },
        { text: "Location", value: "location", filterable: false },
        { text: "Application Deadline", value: "deadline", filterable: false },
        { text: "Approved Date", value: "approved", filterable: false },
        { text: "Contacted", value: "contact", sortable: false },
        { text: "Actions", value: "control", sortable: false },
      ],
      editedIndex: -1,
      editedItem: {
        name: "",
        department: "",
        tel_number: "",
        location: "",
        deadline: "",
        approved: "",
        contact: "",
      },
      defaultItem: {
        name: "",
        department: "",
        tel_number: "",
        location: "",
        deadline: "",
        approved: "",
        contact: "",
      },
      applicants: [
        {
          name: "John Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "George Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Johnny Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Jonathan Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Joni Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Jinny Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Jelly Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Giorno Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Giorgio Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Jitney Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
        {
          name: "Silly Doe",
          department: "Team A",
          tel_number: "0888888888",
          location: "Lad Krabang",
          deadline: "March 29th, 2023",
          approved: "No",
          contact: "No",
        },
      ],
      watch: {
        dialogDelete(val) {
          val || this.closeDelete();
        },
      },
      deleteItem(item) {
        this.editedIndex = this.applicants.indexOf(item);
        this.editedItem = Object.assign({}, item);
        this.dialogDelete = true;
      },
      deleteItemConfirm() {
        this.applicants.contact = "Yes"
        // this line must connect to the applicant's email, providing them the URL to do the test
        // this.applicants.splice(this.editedIndex, 1);
        this.closeDelete();
      },
      closeDelete() {
        this.dialogDelete = false;
        // this.$nextTick(() => {
        //   this.editedItem = Object.assign({}, this.defaultItem);
        //   this.editedIndex = -1;
        // });
      },
    };
  },
};
</script>
