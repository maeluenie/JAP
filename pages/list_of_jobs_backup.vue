<template>
  <div>
    <v-container bg>
      <v-layout
        row
        wrap
        align-center
        align-content-center
        justify-center
        class="mx-2"
      >
        <v-flex>
          <v-combobox
            v-model="select"
            :items="job_role"
            label="Select your dream jobs"
            hide-selected
            elevation-4
            multiple
            solo
            persistent-hint
            small-chips
            class="mx-4 mt-6 font-weight-bold"
            clearable
          ></v-combobox>
        </v-flex>
        <v-btn> test </v-btn>
      </v-layout>
      <v-layout
        row
        wrap
        align-center
        align-content-center
        justify-center
        class="mx-2 my-2"
      >
        <v-row justify="start" align="start">
          <v-col cols="auto" sm="12" md="6">
            <v-card class="ml-4">
              <v-list-item>
                <v-list-item-avatar
                  align="center"
                  tile
                  color="grey"
                ></v-list-item-avatar>

                <v-list-item-content>
                  <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

                  <v-container bg fill-height align-left>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Ladkrabang HQ </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                    </v-layout>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Start Date : April 2022 </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          Deadline : March 3 , 2022
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          Approx. Salary ≈ 100,000 THB
                        </v-flex>
                      </v-layout>
                    </v-layout>
                  </v-container>
                </v-list-item-content>
              </v-list-item>

              <hr class="my-1" />

              <v-col class="text-right">
                <v-btn align="end" color="primary darken-3" nuxt to="/inspire">
                  Apply
                </v-btn>
              </v-col>
            </v-card>
            <div class="row mb-4"></div>
          </v-col>
          <v-col cols="auto" sm="12" md="6">
            <v-card>
              <v-list-item>
                <v-list-item-avatar
                  align="center"
                  tile
                  color="grey"
                ></v-list-item-avatar>

                <v-list-item-content>
                  <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

                  <v-container bg fill-height align-left>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Ladkrabang HQ </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                    </v-layout>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Start Date : April 2022 </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          Deadline : March 3 , 2022
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          Approx. Salary ≈ 100,000 THB
                        </v-flex>
                      </v-layout>
                    </v-layout>
                  </v-container>
                </v-list-item-content>
              </v-list-item>

              <hr class="my-1" />

              <v-col class="text-right">
                <v-btn align="end" color="primary darken-3" nuxt to="/inspire">
                  Apply
                </v-btn>
              </v-col>
            </v-card>
            <div class="row mb-4"></div>
          </v-col>
        </v-row>
      </v-layout>
      <v-layout
        row
        wrap
        align-center
        align-content-center
        justify-center
        class="mx-2 my-2"
      >
        <v-row justify="start" align="start">
          <v-col cols="auto" sm="12" md="6">
            <v-card class="ml-4">
              <v-list-item>
                <v-list-item-avatar
                  align="center"
                  tile
                  color="grey"
                ></v-list-item-avatar>

                <v-list-item-content>
                  <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

                  <v-container bg fill-height align-left>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Ladkrabang HQ </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                    </v-layout>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Start Date : April 2022 </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          Deadline : March 3 , 2022
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          Approx. Salary ≈ 100,000 THB
                        </v-flex>
                      </v-layout>
                    </v-layout>
                  </v-container>
                </v-list-item-content>
              </v-list-item>

              <hr class="my-1" />

              <v-col class="text-right">
                <v-btn align="end" color="primary darken-3" nuxt to="/inspire">
                  Apply
                </v-btn>
              </v-col>
            </v-card>
            <div class="row mb-4"></div>
          </v-col>
          <v-col cols="auto" sm="12" md="6">
            <v-card>
              <v-list-item>
                <v-list-item-avatar
                  align="center"
                  tile
                  color="grey"
                ></v-list-item-avatar>

                <v-list-item-content>
                  <div class="text-h6 my-1 font-weight-bold">OVERLINE</div>

                  <v-container bg fill-height align-left>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Ladkrabang HQ </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          <v-icon class="mr-4"> mdi-domain </v-icon> Ladkrabang
                          HQ
                        </v-flex>
                      </v-layout>
                    </v-layout>
                    <v-layout column align-left>
                      <v-layout row align-left>
                        <v-flex class="my-1"> Start Date : April 2022 </v-flex>
                      </v-layout>
                      <v-layout row align-left justify-start>
                        <v-flex class="my-1">
                          Deadline : March 3 , 2022
                        </v-flex>
                      </v-layout>
                      <v-layout row align-left>
                        <v-flex class="my-1">
                          Approx. Salary ≈ 100,000 THB
                        </v-flex>
                      </v-layout>
                    </v-layout>
                  </v-container>
                </v-list-item-content>
              </v-list-item>

              <hr class="my-1" />

              <v-col class="text-right">
                <v-btn align="end" color="primary darken-3" nuxt to="/inspire">
                  Apply
                </v-btn>
              </v-col>
            </v-card>
            <div class="row mb-4"></div>
          </v-col>
        </v-row>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "List of Jobs Page",
  data() {
    return {
      select: [],
      job_role: [
        "UX/UI Designer",
        "DevOps",
        "Cyber Security",
        "Back-End Golang Developer",
        "Front-End Developer",
      ],
    };
  },
  methods: {
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
  },
};
</script>
