<template>
  <v-card
    ><v-form
      ><v-row>
        <v-col cols="12" sm="8" md="6">
          <v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field
          ><v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="2" md="2">
          <v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field
          ><v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field>
        </v-col>

        <v-col cols="12" sm="8" md="2">
          <v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field
          ><v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="8" md="2">
          <v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field
          ><v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field>
          
        </v-col>
        <v-col cols="12" sm="8" md="2">
          <v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field
          ><v-text-field
            class="mx-8 mt-2"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            outlined
          ></v-text-field>
          
        </v-col>
      </v-row> </v-form
  ></v-card>
</template>

<script>
export default {
  name: "Application Form Page",
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
  }),
};
</script>
