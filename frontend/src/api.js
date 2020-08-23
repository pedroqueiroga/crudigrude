import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 1000,
});

const api = {
  fetchFuncionarios: function fetchFuncionarios() {
    const url = 'funcionarios/';
    return instance.get(url);
  },
  fetchFuncionario: function fetchFuncionario(id) {
    const url = `funcionarios/${id}/`;
    return instance.get(url);
  },
  fetchDepartamentos: function fetchDepartamentos() {
    const url = 'departamentos/';
    return instance.get(url);
  },

  updateFuncionario: function updateFuncionario(id, nome, funcao, idade, departamento) {
    console.log(nome, funcao, idade, departamento);
    const url = `funcionarios/${id}/`;
    return instance.put(url, {
      nome,
      funcao,
      idade,
      departamento,
    });
  },
};

export default api;
