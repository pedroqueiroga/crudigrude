<template>
<v-card
  class="mx-auto"
  v-if="funcionarios && funcionarios.count"
  >
  <v-pagination
    v-model="page"
    :length="numPages()"
    class="secondary"
    ></v-pagination>
  <v-list>
    <v-list-item-group color="primary">
      <v-list-item
        v-for="(item, i) in funcionariosResults"
        :key="i"
        :to="{name:'funcionario-detail',params:{ id: item.id }}"
        >
        <v-list-item-content>
          <v-list-item-title v-text="item.nome"></v-list-item-title>
          <v-list-item-subtitle v-text="item.departamento"></v-list-item-subtitle>
        </v-list-item-content>
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
    page: 1,
    pageLen: 10,
    serverError: false,
    snackbar: false,
  }),

  watch: {
    page: function() {
      this.fetchList();
    },
  },
  
  computed: {
    funcionarios() {
      return this.$store.state.funcionarios;
    },
    funcionariosResults() {
      return this.$store.getters.funcionariosResults;
    },
    departamentos() {
      return this.$store.state.departamentos;
    },
  },
  
  methods: {
    numPages() {
      return Math.ceil(this.funcionarios.count / this.pageLen);
    },
    tryAgainButton() {
      this.snackbar = this.serverError = false;
      this.fetchList();
    },
    fetchList() {
      this.$store.dispatch('fetchFuncionarios', { page: this.page })
        .catch(error => {
          console.log(error);
          this.serverError = true;
          this.snackbar = true;
        });
    },
    fetchDepartamentos() {
      return this.$store.dispatch('fetchDepartamentos')
        .catch(error => {
          console.log(error);
          this.snackbar = true;
          this.serverError = true;
        });
    },
  },
  
  created() {
    if (!this.departamentos) {
      this.fetchDepartamentos().then(() => {
        return this.fetchList();
      });
    } else if (!this.funcionarios) {
      this.fetchList();
    }
  },
}
</script>
