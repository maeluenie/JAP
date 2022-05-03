<template>
  <div id="app">
    <v-app id="inspire">
      <v-data-table
        :headers="headers"
        :items="applicants"
        :search="search"
        sort-by="calories"
        class="elevation-1"
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

              <!-- this v-card section is the dialog of item's modification ( initially, it is edit item page ) -->
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
          <!-- this commented section is used for the deletion of that specific item ( Desserts as in the source code ) -->
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
