<template>
  <v-app>
    <v-app-bar
      app 
      clipped-left
      color="primary"
      dark
      >
      <v-btn
        text
        @click="goHome"
        v-show="shouldShow"
        >
        <span class="title">C<span class="d-none d-sm-inline title ">RUD<span class="d-none d-md-inline font-weight-light">IGRUDE</span>
        </span>
        </span>
      </v-btn>

      <v-text-field
        solo-inverted
        flat
        hide-details
        label="Procurar Funcionário"
        prepend-inner-icon="mdi-magnify"
        clearable
        class="ml-2"
        @focus="shouldShow = $vuetify.breakpoint.smAndUp || false"
        @blur="shouldShow = true"
        ></v-text-field>

      <v-btn
        class="ml-3 mr-3"
        outlined
        :to="{ name: 'register' }"
        v-show="shouldShow"
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
        v-show="shouldShow"
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
    shouldShow: true,
  }),
  methods: {
    goHome(){
      this.$router.push({ name: 'funcionario-list' });
    }
  }
};
</script>
