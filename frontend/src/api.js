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
};

export default api;
