<template>

<!-- this is the backup file for the job applicable cards -->

  <v-row justify="start" align="start">
    <v-col cols="auto" sm="8" md="6">
      <v-card class="mx-8 my-4" max-width="700" elevation="4">
        <v-list-item three-line class="align-content-start">
          <v-list-item-avatar
            justify-center
            align-content-center
            tile
            size="80"
            color="grey"
          ></v-list-item-avatar>
          <!-- this is the icon -->
          <v-list-item-content class="mx-4">
            <v-list-item-title class="text-h5 my-2 font-weight-bold"
              >UX/UI Designer</v-list-item-title
            >
            <!-- this is the job title -->
            <v-list-item-subtitle class="text-body-1 my-1">
              User Experience Team
            </v-list-item-subtitle>
            <!-- this is job team description -->
            <v-list-item-subtitle class="text-body-1 my-1">
              Ladkrabang HQ
            </v-list-item-subtitle>
            <!-- this is working location -->
            <v-list-item-subtitle class="text-body-1 my-1"
              >Full-time, Weekdays</v-list-item-subtitle
            >
            <!-- this is job working time -->
          </v-list-item-content>

          <v-list-item-content class="align-content-center">
            <v-list-item-subtitle class="text-body-1 my-1 text-right">
              Start Date : April 2022
            </v-list-item-subtitle>
            <!-- this is job team description -->

            <v-list-item-subtitle class="text-body-1 my-1 text-right">
              Deadline : March 3 , 2022
            </v-list-item-subtitle>

            <v-list-item-subtitle class="text-body-1 my-1 text-right">
              Approx. Salary ≈ 100,000 THB
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <hr class="my-1" />

        <v-spacer />

        <v-col class="text-right">
          <v-btn align="end" color="primary" nuxt to="/inspire"> Apply </v-btn>
        </v-col>
      </v-card>
      <div class="row mb-4"></div>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "IndexPage",
  data() {
    return {
      items: [
        
        
      ],
    };
  },
};
</script>
