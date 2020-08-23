import Vue from 'vue';
import Vuex from 'vuex';
import api from '../api.js';

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    funcionarios: null,
    departamentos: null,
    deptosUrlNome: null,
  },
  getters: {
    funcionariosResults: (state) => {
      console.log(state.funcionarios.results);
      console.log('^state.funcionarios.results^');
      return state.funcionarios.results?.map(funcionario => {
        const f = funcionario;
        f.departamento = state.deptosUrlNome[funcionario.departamento];
        return f;
      });
    },
    deptosNomeUrl: (state) => {
      // o inverso do deptosUrlNome
      const inv = {};
      for (const key in state.deptosUrlNome) {
        inv[state.deptosUrlNome[key]] = key;
      }
      return inv;
    },
  },
  mutations: {
    setFuncionarios(state, funcionarios) {
      state.funcionarios = funcionarios;
    },
    setDepartamentos(state, departamentos) {
      state.departamentos = departamentos;
    },
    setDeptosUrlNome(state, deptosUrlNome) {
      state.deptosUrlNome = deptosUrlNome;
    },
  },
  actions: {
    fetchFuncionarios(context, props) {
      const page = props?.page;
      return api.fetchFuncionarios(page).then(response => {
        if (response.status === 200) {
          const funcionarios = response.data;
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
          const data = response.data;
          const newDep = {};
          for (const dep of data) {
            newDep[dep.url] = dep.nome;
          }
          context.commit('setDeptosUrlNome', newDep);

          context.commit('setDepartamentos', response.data);
        } else {
          Promise.reject(response);
        }
        return context.state.departamentos;
      });
    },
  },
});
