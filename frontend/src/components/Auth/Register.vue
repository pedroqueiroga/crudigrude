<template>
<v-row
  align="center"
  justify="center"
  >
  {{ email }}
  {{ username }}
  {{ password }}
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
</v-row>
</template>

<script>
  import api from '../../api';
export default {
  name: 'Register',

  data: () => ({
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
        const url = response.data.funcionario.split('/api/');
        this.$router.push(url[1]);
      }).catch(error => {
        console.log('erro tentando criar conta', error);
      });
    },
  },
}
</script>
