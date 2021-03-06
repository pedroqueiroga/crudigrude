import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 1000,
});

// essa daqui pode ser útil pois no backend estou usando hyperlinks
const blankInstance = axios.create({
  timeout: 1000,
});

const funcionariosUrl = 'funcionarios/';
const api = {
  fetchFuncionarios: function fetchFuncionarios(page, search) {
    let url = funcionariosUrl;
    let searchurl = '';
    let pageurl = '';
    if (search) {
      searchurl += `search=${search}`;
    }
    if (page) {
      pageurl += `page=${page}`;
    }
    if (search && page) {
      url += `?${searchurl}&${pageurl}`;
    } else if (search) {
      url += `?${searchurl}`;
    } else if (page) {
      url += `?${pageurl}`;
    }
    console.log('im sending the string', url);
    return instance.get(url);
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

  getRequest: function getRequest(url) {
    return blankInstance.get(url);
  },

  deleteRequest: function deleteRequest(url) {
    return blankInstance.delete(url);
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
