import Vue from 'vue';
import Vuex from 'vuex';
import api from '../api.js';

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    funcionarios: null,
    departamentos: null,
  },
  mutations: {
    setFuncionarios(state, funcionarios) {
      state.funcionarios = funcionarios;
    },
    setDepartamentos(state, departamentos) {
      state.departamentos = departamentos;
    },
  },
  actions: {
    fetchFuncionarios(context) {
      return api.fetchFuncionarios().then(response => {
        if (response.status === 200) {
          const funcionarios = response.data;
          for (let i = 0; i < funcionarios.count; i++) {
            const funcionario = funcionarios.results[i];
            funcionario.departamento = funcionario.departamento.nome;
          }
          context.commit('setFuncionarios', funcionarios);
        } else {
          Promise.reject(response);
        }
        return context.state.funcionarios;
      });
    },
    fetchDepartamentos(context) {
      return api.fetchDepartamentos().then(response => {
        if (response.status === 200) {
          context.commit('setDepartamentos', response.data);
        } else {
          Promise.reject(response);
        }
        return context.state.departamentos;
      });
    },
  },
});
