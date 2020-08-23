import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 1000,
});

const deleteInstance = axios.create({
  timeout: 1000,
});

const funcionariosUrl = 'funcionarios/';
const api = {
  fetchFuncionarios: function fetchFuncionarios() {
    return instance.get(funcionariosUrl);
  },
  fetchFuncionario: function fetchFuncionario(id) {
    const url = `${funcionariosUrl}${id}/`;
    return instance.get(url);
  },
  fetchDepartamentos: function fetchDepartamentos() {
    const url = 'departamentos/';
    return instance.get(url);
  },

  updateFuncionario: function updateFuncionario(id, nome, funcao, idade, departamento) {
    const url = `${funcionariosUrl}${id}/`;
    return instance.put(url, {
      nome,
      funcao,
      idade,
      departamento,
    });
  },

  deleteRequest: function deleteRequest(url) {
    return deleteInstance.delete(url);
  },

  createUser: function createUser(username, email, password) {
    const url = 'users/';
    return instance.post(url, {
      username,
      email,
      password,
    });
  }
};

export default api;
