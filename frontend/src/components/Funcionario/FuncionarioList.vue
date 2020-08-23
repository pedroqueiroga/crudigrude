<template>
<v-card
  class="mx-auto"
  v-if="funcionarios && funcionarios.count"
  >
  <v-pagination
    v-model="page"
    :length="Math.ceil(funcionarios.count / 10)"
    class="secondary"
    ></v-pagination>
  <v-list>
    <v-list-item-group color="primary">
      <v-list-item
        v-for="(item, i) in funcionarios.results"
        :key="i"
        >
        <router-link
          :to="{name:'funcionario-detail',params:{ id: item.id }}"
          >
          <v-list-item-content>
            <v-list-item-title v-text="item.nome"></v-list-item-title>
            <v-list-item-subtitle v-text="item.departamento"></v-list-item-subtitle>
          </v-list-item-content>
        </router-link>
      </v-list-item>
    </v-list-item-group>
  </v-list>
</v-card>
<v-content
  fill-height
  fluid
  v-else
  >
  <v-snackbar
    v-model="snackbar"
    top
    color="error"
    >
    Erro ao tentar acessar o servidor!
  </v-snackbar>
  <v-row
    align="center"
    justify="center"
    >
    <v-btn
      v-if="serverError"
      color="secondary"
      dark
      @click="tryAgainButton"
      >
      Tentar novamente
    </v-btn>
    <v-progress-circular
      indeterminate
      color="secondary"
      v-else
      >
    </v-progress-circular>
  </v-row>
</v-content>
</template>

<script>
export default {
  name: 'FuncionarioList',
  
  data: () => ({
    pageLen: 10,
    serverError: false,
    snackbar: false,
  }),
  
  computed: {
    funcionarios() {
      return this.$store.state.funcionarios;
    },
  },
  
  methods: {
    numPages() {
      return this.funcionarios.count / this.pageLen;
    },
    tryAgainButton() {
      this.snackbar = this.serverError = false;
      this.fetchList();
    },
    fetchList() {
      this.$store.dispatch('fetchFuncionarios')
        .catch(error => {
          console.log(error);
          this.serverError = true;
          this.snackbar = true;
        });
    },
  },
  
  created() {
    this.fetchList();
  },
}
</script>
