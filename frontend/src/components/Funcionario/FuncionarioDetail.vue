<template>
<div>
  <v-card dark>
    <v-card-title class="secondary">
      <v-btn
        text
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
      <v-spacer></v-spacer>
      <v-btn
        text
        >
        <v-icon>mdi-pencil-outline</v-icon>
      </v-btn>
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
    <div
      v-else
      >
      <v-row>
        <v-card-text
          class="ml-5"
          >
          <strong>Departamento:</strong> {{ funcionario.departamento }}
        </v-card-text>
      </v-row>
      <v-divider></v-divider>
      <v-row>
        <v-card-text
          class="ml-5"
          >
          <strong>Idade:</strong> {{ funcionario.idade }}
        </v-card-text>
        
    </v-row>
    </div>
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
            const funcionario = response.data;
            console.log(funcionario);
            funcionario.departamento = funcionario.departamento.nome;
            this.funcionario = funcionario;
            console.log(this.funcionario);
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
