
# Guia de uso do projeto base

## INSTALAÇÂO

### Ferramentas Necessarias
* Baixe e instale o python (Preferivel versao 3.7.4)
```
https://www.python.org/downloads/
```

* Baixe e instale o node 
```
https://nodejs.org/en/download/
```

### Iniciar projeto do Backend
* Crie um virtualenv com Python 3.
* Abra o terminal e entre na pasta do boilerplate até a pasta chamada backend
```
cd backend
```

* Ative o virtualenv.
```
python -m venv .venv
source .venv/bin/activate

Caso nao consiga executar o comando source:
- Windows
    - Verifique se as variaveis de ambiente do python estao setadas (Ex: C:\Users\fulano\AppData\Local\Programs\Python\Python37\ e C:\Users\fulano\AppData\Local\Programs\Python\Python37\Scripts\) e tente novamente.
    - Outra forma é entrar na pasta criada .venv e execute: ./Scripts/activate
```

* Instale as dependências.
```
pip install -r requirements.txt
python contrib/env_gen.py
```

* Rode as migrações.
```
python manage.py migrate
```

* Crie um super usuário
```
python manage.py createsuperuser
```

Para rodar o Django, dentro da pasta backend, digite:

```
python manage.py runserver
```

Isso vai rodar o servidor de back na porta **8000**.


### Frontend

Para rodar o VueJS, abra uma **nova aba no terminal** e va ate a pasta frontend, faça:

```
cd ../frontend
```
### Dentro da pasta frontend, primeiro precisa instalar o vue e suas dependências.
```
npm install
```

### Rode o servidor frontend
```
npm run serve
```

Isso vai rodar o servidor de front na porta **8080**.


## DESAFIO

- Crie um CRUD de funcionários onde seja possível inserir, listar, editar e deletar os funcionarios ja cadastrados.
- Os funcionários devem conter as informações: nome, funcao e idade.
- Cada funcionario pertence a um departamento (TI, SUPORTE e DESIGN) que somente possui um atributo: nome.

## Observações

- Não precisa instalar nenhum banco pois o boilerplate já está utilizando o sqlite mas caso tenha familiariedade com outro banco de dados, pode utiliza-lo mas configure o projeto para utilizar o banco desejado.
- Dê o seu máximo em relação a organização do código e funcionalidades.
- Sabemos que nem todos conseguirão concluir o desafio, por isso não desista e entregue oque conseguir.
- O intuito do desafio é apenas mensurar a capacidade do candidato em utilizar as tecnologias em um projeto.
- Dê preferencia a interface utilizando Vue (Vuetify) mas caso não seja possivel pode se utilizar html/css e JS ou outro framework.
- Ao finalizar o projeto, suba para o github e nos envie por email com o link do seu projeto, verificaremos o ultimo commit antes do horario máximo estabelecido.

## Links Relacionados (Uteis)
- https://vuejs.org/
- https://v15.vuetifyjs.com/pt-BR/getting-started/quick-start
- https://www.django-rest-framework.org/
- https://github.com/axios/axios
- https://www.python.org/about/gettingstarted/



