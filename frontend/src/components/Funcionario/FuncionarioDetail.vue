<template>
<div>
  <v-snackbar
    v-model="snackbar"
    top
    :color="editSuccess ? 'success' : 'error'"
    >
    <span
      v-if="editSuccess"
      >
      Deu tudo certo!
    </span>
    <span v-else>
      Erro ao tentar acessar o servidor!
    </span>
  </v-snackbar>
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
        v-if="funcionario && departamentos && !editting"
        >
        {{ funcionario.nome }}
      </span>
      <v-text-field
        v-if="editting"
        label="Nome"
        clearable
        v-model="nome"
        >
      </v-text-field>
      <v-spacer></v-spacer>
      <v-btn
        text
        @click="editting = !editting"
        :disabled="editting || !funcionario"
        >
        <v-icon>mdi-pencil-outline</v-icon>
      </v-btn>
    </v-card-title>
    <v-divider></v-divider>
    <v-row
      align="center"
      justify="center"
      v-if="fetchError"
      @click="tryAgainButton"
      >
      <v-btn
        class="mb-3 mt-3"
        >
        tentar novamente
      </v-btn>
      
    </v-row>
    <v-row
      align="center"
      justify="center"
      v-else-if="!funcionario || !departamentos"
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
    <v-container
      v-else
      >
      <v-row>
        <v-card-text
          v-if="!editting"
          >
          <strong>Departamento:</strong> {{ funcionario.departamento }}
        </v-card-text>
        <v-autocomplete
          class="ml-3 mr-3"
          :items="departamentosOptions"
          v-else-if="departamentos"
          label="Departamento"
          v-model="departamento"
          >
        </v-autocomplete>
      </v-row>
      <v-divider></v-divider>
      <v-row>
        <v-card-text
          v-if="!editting"
          >
          <strong>Função:</strong> {{ funcionario.funcao }}
        </v-card-text>
        <v-col
          v-else
          >
          <v-text-field
            label="Função"
            v-model="funcao"
            >
          </v-text-field>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row>
        <v-card-text
          v-if="!editting"
          >
          <strong>Idade:</strong> {{ funcionario.idade }}
        </v-card-text>
        <v-col
          class="col-3"
          v-else
          >
          <v-text-field
            type="number"
            label="Idade"
            v-model="idade"
            :rules="[idadeRule]"
            >
          </v-text-field>
        </v-col>
      </v-row>
        <v-card-actions
        v-if="editting"
          >
          <v-row
            justify="center"
            >
          <v-btn
            class="col-6 col-sm-4"
            color="success"
            @click="confirmEdit"
            >
            confirmar
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            color="error"
            class="col-4"
            @click="cancelEdit"
            >
            cancelar
          </v-btn>
          </v-row>
        </v-card-actions>
    </v-container>
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
    editting: false,
    departamentosError: false,
    editError: false,
    editSuccess: false,
    snackbar: false,
    nome: null,
    funcao: null,
    departamento: null,
    idade: null,
    idadeRule: idade => {
      if (!idade.trim()) return true;
      if (idade >= 0) return true;
      return 'Idade precisa ser positiva';
    }
  }),
  
  computed: {
    funcionarioId() {
      return this.$route.params.id;
    },
    departamentos() {
      return this.$store.state.departamentos;
    },
    departamentosOptions() {
      return this.$store.state.departamentos.map(dep =>
        dep = dep.nome
      );
    },
    deptosUrlNome() {
      return this.$store.state.deptosUrlNome;
    },
    funcionariosResults() {
      return this.$store.getters.funcionariosResults;
      }
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
            const departamento = this.deptosUrlNome[funcionario.departamento]
            if (!departamento) {
              Promise.reject(response);
            }
            funcionario.departamento = departamento;
            this.funcionario = funcionario;
            this.nome = this.funcionario.nome;
            this.idade = this.funcionario.idade;
            this.departamento = this.funcionario.departamento;
            this.funcao = this.funcionario.funcao;
          } else {
            Promise.reject(response);
          }
        })
        .catch(error => {
          console.log('err',error);
          this.fetchError = true;
          this.snackbar = true;
        });
    },
    fetchDepartamentos() {
      return this.$store.dispatch('fetchDepartamentos')
        .catch(error => {
          console.log(error);
          this.departamentosError = true;
          this.snackbar = true;
        });
    },
    tryAgainButton() {
      this.snackbar = false;
      this.fetchError = false;
      this.departamentosError = false;
      this.fetchFuncionario();
      const departamentos = this.$store.departamentos;
      if (!departamentos) {
        this.fetchDepartamentos();
      }
    },
    
    confirmEdit() {
      api.updateFuncionario(
        this.funcionarioId,
        this.nome,
        this.funcao,
        this.idade,
        this.departamento
      ).then(response => {
        console.log('update response:', response);
        this.fetchFuncionario();
        this.editting = false;
        this.snackbarEditSuccess = true;
      }).catch(error => {
        console.log('update error:', error);
        this.snackbar = true;
        this.editError = true;
      });
    },
    
    cancelEdit() {
      this.editting = false;
      this.nome = this.funcionario.nome;
      this.funcao = this.funcionario.funcao;
      this.idade = this.funcionario.idade;
      this.departamento = this.funcionario.departamento;
    },
  },
  
  created() {
    setTimeout(() => {
      const departamentos = this.departamentos;
      if (!departamentos) {
        this.fetchDepartamentos().then(() => {
          try {
            const funcionario = this.funcionariosResults.find(funcionario =>
              funcionario.id === this.funcionarioId
            );
            if (!funcionario) {
              this.fetchFuncionario();
            } else {
              const departamento = this.deptosUrlNome[funcionario.departamento]
              funcionario.departamento = departamento;
              this.funcionario = funcionario;
            }
          } catch {
            this.fetchFuncionario();
          }
        });
      } else { this.fetchFuncionario(); }
    }, 1500);
  },
}
</script>
