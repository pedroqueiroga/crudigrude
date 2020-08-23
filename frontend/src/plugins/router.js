import Vue from 'vue';
import VueRouter from 'vue-router';

import FuncionarioDetail from '../components/Funcionario/FuncionarioDetail';
import FuncionarioList from '../components/Funcionario/FuncionarioList';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/funcionarios/:id/',
      component: FuncionarioDetail,
      name: 'funcionario-detail',
    },
    {
      path: '/funcionarios/',
      component: FuncionarioList,
      name: 'funcionario-list',
    }
  ],
});
