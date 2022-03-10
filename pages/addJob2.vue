<template>
  <v-app>

    <!-- addJob1 must be the user's personal details , it must also be an editable form with original content for modification too --> 
    <v-card class="mx-6 my-4" outlined color="transparent">
    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover">
    <v-text>1 Job Details</v-text>
    </v-btn>
    <v-btn :ripple="false" text color="natural dark-grey" id="no-background-hover" nuxt to="/addJob2">
    <v-text>2 General Question</v-text>
    </v-btn>
    <v-btn :ripple="false" text color="primary darken-3" id="no-background-hover" nuxt to="/.">
    <v-text>3 Benefits and Welfare</v-text>
    </v-btn>
    </v-card>

    <v-card class="mx-4 my-4 py-2">
      <v-text-title class="font-weight-bold"
        ><h2 class="mx-8 my-4 text-left">
          General Questions
        </h2></v-text-title>
     

      <v-form class="mx-8 mt-2 align-content-center">
        <!-- on real use case situation, the upload method will be included in the main save button -->
        <v-row>
          
          <div class="form-group" v-for="(input,k) in inputs" :key="k">
              <input type="text" class="form-control" v-model="input.name">
              <span>
                  <i class="fas fa-minus-circle" @click="remove(k)" v-show="k || ( !k && inputs.length > 1)"></i>
                  <i class="fas fa-plus-circle" @click="add(k)" v-show="k == inputs.length-1"></i>
              </span>
          </div>
    


        <v-col class="text-right">
          <v-btn align="end" color="primary darken-3" nuxt to="/addJob2">  
            Next
          </v-btn>
        </v-col>
          
        </v-row>
      </v-form>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: " Add Job Questions",
  data: () => ({
    inputs: [
      {
          name: ''
      }
    ]
  }),

  methods: {
    add(index) {
        this.inputs.push({ name: '' });
    },
    remove(index) {
        this.inputs.splice(index, 1);
    }
  }
};

//   //calendar 1
//   watch: {
//     menu1 (val) {
//       val && setTimeout(() => (this.activePicker1 = 'YEAR'))
//     },
//   },

//   //calender 2
//   watch: {
//     menu2 (val) {
//       val && setTimeout(() => (this.activePicker2 = 'YEAR'))
//     },
//   },

//   //calender 1
//   methods: {
//     save (date) {
//       this.$refs.menu1.save(date)
//     },
//   },

//   //calender 2
//   methods: {
//     save (date) {
//       this.$refs.menu2.save(date)
//     },
//   },

//   //chips
//   methods: {
//     remove (item) {
//       this.requiredSkills.splice(this.requiredSkills.indexOf(item), 1)
//       this.requiredSkills = [...this.requiredSkills]
//     },
//   },

// };
</script>
<style></style>
