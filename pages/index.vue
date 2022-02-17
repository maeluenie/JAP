<template>
  <v-row justify="start" align="start">
    <v-col cols="auto" sm="8" md="6">
      <v-card class="mx-8 my-4" max-width="700" elevation="4">
        <v-list-item three-line>
          <v-list-item-avatar
            align="center"
            tile
            size="80"
            color="grey"
          ></v-list-item-avatar>

          <v-list-item-content>
            <!-- <div class="text-h6 mb-1 font-weight-bold">OVERLINE</div> -->

            <v-container bg fill-height grid-list-md text-xs-center>
              <v-layout column wrap align-left>
                <v-flex>
                  Hello I am center to vertically using "align-center".
                </v-flex>
              </v-layout>
            </v-container>
          </v-list-item-content>
          <v-list-item-content>
            <!-- <div class="text-h6 mb-1 font-weight-bold">OVERLINE</div> -->

            <v-container bg fill-height align-left>
              <v-layout column align-left>
                <v-layout row align-left>
                  <v-flex class="font-weight-bold "> <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang HQ </v-flex> 
                </v-layout>
                <v-layout row align-left justify-start>
                  <v-flex> <v-icon> mdi-domain </v-icon> </v-flex>
                  <v-flex> B </v-flex>
                </v-layout>
                <v-layout row align-left>
                  <v-flex> <v-icon> mdi-domain </v-icon> </v-flex>
                  <v-flex> B </v-flex>
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
