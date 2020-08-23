<template>
<div>
  <v-card color="white" dark>
    <v-card-title class="secondary">
      <v-btn
        outlined
        @click="backToList"
        class="mr-3"
        >
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <span
        v-if="funcionario"
        >
        {{ funcionario.nome }}
      </span>
    </v-card-title>
    <v-divider></v-divider>
    <v-row
      align="center"
      justify="center"
      v-if="!funcionario"
      >
      <v-progress-circular
        indeterminate
        color="secondary"
        align="center"
        justify="center"
        class="mb-3 mt-3"
        >
      </v-progress-circular>
    </v-row>
    <v-card-subtitle
      v-else
      >
      {{ funcionario.departamento }}
    </v-card-subtitle>
  </v-card>
</div>
</template>

<script>
import api from '../../api';
export default {
  name: 'FuncionarioDetail',
  
  data: () => ({
    funcionario: null,
    fetchError: false,
  }),
  
  computed: {
    funcionarioId() {
      return this.$route.params.id;
    },
  },
  methods: {
    backToList() {
      this.$router.push({ name: 'funcionario-list' });
    },
    fetchFuncionario() {
      api.fetchFuncionario(this.funcionarioId)
        .then(response => {
          if (response.status == 200) {
            this.funcionario = response.data;
          } else {
            Promise.reject(response);
          }
        })
        .catch(error => {
          console.log(error);
          this.fetchError = true;
        });
    },
  },
  
  created() {
    setTimeout(() => {
      try {
        const funcionario = this.$store.state.funcionarios.results
              .filter(funcionario => funcionario.id === this.funcionarioId)[0];
        if (!funcionario) {
          this.fetchFuncionario();
        } else {
          this.funcionario = funcionario;
        }
      } catch {
        this.fetchFuncionario();
      }
    }, 1500);
  },
}
</script>
