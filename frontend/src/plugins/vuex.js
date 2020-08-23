import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    funcionarios: [
      { nome: 'funcionario 1', departamento: 'IT', },
      { nome: 'funcionario 2', departamento: 'DESIGN', },
      { nome: 'funcionario 3', departamento: 'SUPORTE', },
    ],
  },
});
