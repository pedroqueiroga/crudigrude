import Vue from 'vue';
import VueRouter from 'vue-router';

import FuncionarioDetail from '../components/Funcionario/FuncionarioDetail';
import FuncionarioList from '../components/Funcionario/FuncionarioList';
import Register from '../components/Auth/Register';

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
    },
    {
      path: '/registrar/',
      component: Register,
      name: 'register',
    },
    {
      path: '/entrar/',
      name: 'entrar',
    },
  ],
});
