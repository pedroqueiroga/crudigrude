import Vue from 'vue';
import Vuex from 'vuex';
import api from '../api.js';

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    funcionarios: null,
  },
  mutations: {
    setFuncionarios(state, funcionarios) {
      state.funcionarios = funcionarios;
    }
  },
  actions: {
    fetchFuncionarios(context) {
      api.fetchFuncionarios().then(response => {
        if (response.status == 200) {
          context.commit('setFuncionarios', response.data);
        } else {
          Promise.reject(response);
        }
        return context.state.funcionarios;
      }).catch(error => {
        console.log(error);
        context.commit('setFuncionarios', null);
        return context.state.funcionarios;
      });
    },
  },
});
