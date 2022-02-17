<template>
  <v-row justify="start" align="start">
    <v-col cols="auto" sm="8" md="6">
      <v-card class="ml-4 mt-4" elevation="4">
        <v-list-item>
          <v-list-item-avatar
            align="center"
            tile
            size="80"
            color="grey"
          ></v-list-item-avatar>

          <v-list-item-content>
            <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

            <v-container bg fill-height align-left>
              <v-layout column align-left>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                    Ladkrabang HQ
                  </v-flex>
                </v-layout>
                <v-layout row align-left justify-start>
                  <v-flex class='my-1'>
                    <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang HQ
                  </v-flex>
                </v-layout>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                    <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang HQ
                  </v-flex>
                </v-layout>
              </v-layout>
              <v-layout column align-left>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                   Start Date : April 2022
                  </v-flex>
                </v-layout>
                <v-layout row align-left justify-start>
                  <v-flex class='my-1'>
                    Deadline : March 3 , 2022
                  </v-flex>
                </v-layout>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                    Approx. Salary ≈ 100,000 THB
                  </v-flex>
                </v-layout>
              </v-layout>
            </v-container>
          </v-list-item-content>
        </v-list-item>

        <hr class="my-1" />

        <v-col class="text-right">
          <v-btn align="end" color="primary" nuxt to="/inspire"> Apply </v-btn>
        </v-col>
      </v-card>
      <div class="row mb-4"></div>
    </v-col>
    <v-col cols="auto" sm="8" md="6">
      <v-card class="ml-4 mt-4" elevation="4">
        <v-list-item>
          <v-list-item-avatar
            align="center"
            tile
            size="80"
            color="grey"
          ></v-list-item-avatar>

          <v-list-item-content>
            <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

            <v-container bg fill-height align-left>
              <v-layout column align-left>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                    Ladkrabang HQ
                  </v-flex>
                </v-layout>
                <v-layout row align-left justify-start>
                  <v-flex class='my-1'>
                    <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang HQ
                  </v-flex>
                </v-layout>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                    <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang HQ
                  </v-flex>
                </v-layout>
              </v-layout>
              <v-layout column align-left>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                   Start Date : April 2022
                  </v-flex>
                </v-layout>
                <v-layout row align-left justify-start>
                  <v-flex class='my-1'>
                    Deadline : March 3 , 2022
                  </v-flex>
                </v-layout>
                <v-layout row align-left>
                  <v-flex class='my-1'>
                    Approx. Salary ≈ 100,000 THB
                  </v-flex>
                </v-layout>
              </v-layout>
            </v-container>
          </v-list-item-content>
        </v-list-item>

        <hr class="my-1" />

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
        { text: "Real-Time", icon: "mdi-clock" },
        { text: "Audience", icon: "mdi-account" },
        { text: "Conversions", icon: "mdi-flag" },
      ],
    };
  },
};
</script>
