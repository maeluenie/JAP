<template>
  <v-div>
    <!-- <v-btn
      class="mx-2"
      fab
      dark
      x-small
      color="primary"
      @click="dialog = true"
      ref="deleteItem"
    >
      <v-icon dark>mdi-send</v-icon>
    </v-btn> -->
    <v-dialog
      content-class="dialogNew"
      hide-overlay
      persistent
      v-model="dialog"
      ref="dialog"
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
          <v-btn color="blue darken-1" text @click="cancelContact"
            >Cancel</v-btn
          >
          <v-btn color="blue darken-1" text @click="confirmContact">OK</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-div>
</template>


<script>
export default {
  methods: {
    closeDialog() {
      console.log(this.tel_number);
      this.dialog = false;
    },
    // deleteItem(item) {
    //   this.editedIndex = this.applicants.indexOf(item);
    //   this.editedItem = Object.assign({}, item);
    //   this.dialog = true;
    // },
    confirmContact() {
      // this.applicants.contacted = "Yes"
      console.log("completed");
      // this line must connect to the applicant's email, providing them the URL to do the test
      // this.applicants.splice(this.editedIndex, 1);
      this.dialog = false;
    },
    cancelContact() {
      console.log("cancelling the process, incompleted");
      this.dialog = false;
      // this.$nextTick(() => {
      //   this.editedItem = Object.assign({}, this.defaultItem);
      //   this.editedIndex = -1;
      // });
    },
  },
};
</script>

<style>
.dialogNew {
  box-shadow: 2px 2px 5px 0.05px !important;
}
</style>
