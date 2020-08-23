<template>
  <v-app>
    <v-app-bar
      app 
      clipped-left
      color="primary"
      dark
      >
      <span class="d-none d-sm-inline title ml-3 mr-5">
        CRUD<span class="d-none d-md-inline font-weight-light">IGRUDE</span>
      </span>

      <v-text-field
        solo-inverted
        flat
        hide-details
        label="Procurar Funcionário"
        prepend-inner-icon="mdi-magnify"
        clearable
        ></v-text-field>

      <v-btn
        class="ml-3 mr-3"
        outlined
        >
        <span class="d-none d-sm-inline">
          entrar
        </span>
        <v-icon class="d-sm-none">
          mdi-login
        </v-icon>
      </v-btn>
      <v-spacer></v-spacer>

      <v-btn
        href="#"
        text
      >
        <span class="d-none d-md-inline mr-2">Ver no GitHub</span>
        <v-icon>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
