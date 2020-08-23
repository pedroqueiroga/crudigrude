<template>
<v-row
  align="center"
  justify="center"
  >
  <v-card
    max-width=600
    >
    <v-card-title
      align="center"
      justify="center"
      >
      Registrar
    </v-card-title>
    <v-container>
      <v-text-field
        label="username"
        v-model="username"
        :rules="[usernameRule]"
        >
      </v-text-field>
      <v-text-field
        label="e-mail"
        v-model="email"
        :rules="[emailRule]"
        >
      </v-text-field>
      <v-text-field
        label="senha"
        v-model="password"
        :rules="[passwordRule]"
        >
      </v-text-field>
      <v-card-actions>
        <v-btn
          color="accent"
          @click="createUser"
          >
          registrar
        </v-btn>
      </v-card-actions>
      Já possui uma conta?
      <router-link
        :to="{ name: 'login' }"
        >
        <span>
          Entrar
        </span>
      </router-link>
    </v-container>
  </v-card>
  <v-snackbar
    v-model="snackbar"
    top
    :color="createSuccess ? 'success' : 'error'"
    >
    <span
      v-if="createSuccess"
      >
      Conta criada com sucesso!
    </span>
    <span v-else-if="snackbarText && snackbarText.length > 0">
      {{ snackbarText }}
    </span>
    <span v-else>
      Erro!
    </span>
  </v-snackbar>
</v-row>
</template>

<script>
  import api from '../../api';
export default {
  name: 'Register',

  data: () => ({
    snackbar: false,
    snackbarText: null,
    createSuccess: false,
    username: null,
    email: null,
    password: null,
    emailRule: () => {
      return true; // email é opcional
    },
    usernameRule: usr => {
      if (!usr?.trim()) return "Nome de usuário é obrigatório"
      return true;
    },
    passwordRule: pwd => {
      if (!pwd?.trim()) return "Senha é obrigatória"
      return true;
    },
  }),

  methods: {
    createUser() {
      if (this.passwordRule(this.password) !== true ||
          this.usernameRule(this.username) !== true ||
          this.emailRule(this.email) !== true) {
        console.log(this.passwordRule(), this.usernameRule, this.emailRule);
        console.log('não validou');
        return;
      }
      console.log(this.username, this.email, this.password, 'username email pwd');
      const email = this.email?.trim() || '';
      api.createUser(
        this.username.trim(),
        email,
        this.password
      ).then(response => {
        console.log(response);
        this.createSuccess = true;
        this.snackbar = true;
        const url = response.data.funcionario.split('/api/');
        this.$router.push(url[1]).then().catch(error => {
          console.log(error);
          this.snackbar = true;
          this.createSuccess = false;
          this.snackbarText = 'Conta criada com sucesso, porém não foi possível acessar o perfil. Tente novamente mais tarde.';
        });
      }).catch(error => {
        this.createSuccess = false;
        console.log('erro tentando criar conta', error);
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          console.log(error.response.data);
          this.snackbarText = ''
          for (const er in error.response.data) {
            this.snackbarText += error.response.data[er].join('\n') + '\n';
          }
          this.snackbarText = this.snackbarText.trim();
          this.snackbar = true;
          console.log(error.response.status);
          console.log(error.response.headers);
        } else if (error.request) {
          // The request was made but no response was received
          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          // http.ClientRequest in node.js
          console.log(error.request);
          this.snackbar = true;
        } else {
          // Something happened in setting up the request that triggered an Error
          this.snackbar = true;
          console.log('Error', error.message);
        }
        console.log(error.config);
      });
    },
  },
}
</script>
