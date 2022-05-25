<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
              <v-toolbar-title>Login form</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    name="username"
                    label="Username"
                    type="text"
                    v-model="username"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    name="password"
                    label="Password"
                    :append-icon="value ? 'mdi-eye':'mdi-eye-off'"
                    @click:append="()=>(value=!value)"
                    :type="value? 'password':'text'"
                    v-model="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <!-- v-if role=admin go to listofjobs while else go to userQA page -->
                <!-- <v-btn color="primary" @click="loginHandler" v-if="$auth.data=='admin'" nuxt to="/list_of_jobs">Login</v-btn> -->
                <!-- <v-btn color="primary" v-else nuxt to="/userQA" @click="loginHandler">Login</v-btn> -->
                <v-btn color="primary" @click="loginHandler">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// for the home-landing page, the search button will provide a keywords at the end of the API request line
// to "wild-card" search the database upon the searched job, however, will still navigate to the list of jobs page.
export default {
  layout: "empty",

  name: "Login",
  data() {
    return {
      // username: 'admin',
      // password: 'test12345',
      // username: 'AP126TAGUNJIVASITTHIKUL',
      // password: '4)B3J2?ZgL',
      value: String,
      //role: true,
    };
  },
  methods:{

    async loginHandler(){
      try{
        const response = await this.$auth.loginWith("local",{
          data: {'username': this.username, 'password': this.password}
        });
        
        if (this.$auth.user=='admin') {
          this.$router.push("/list_of_jobs")
        }
        else {
          this.$router.push("/userQA")
          }
        

      } catch (err) {
        //console.log(this.username,this.password)
        console.log(err);
      }
      },

    switchVisibility(){
      this.passwordFieldType = this.passwordFieldType == "password" ? "text" :"password";
    }
  }
};
</script>
