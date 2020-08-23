<template>
  <v-container>
    <v-list>
      <v-list-item-group v-model="item" color="primary">
        <v-list-item
          v-for="(item, i) in list"
          :key="i"
          >
          <v-list-item-content>
            <v-list-item-title v-text="item.nome"></v-list-item-title>
            <v-list-item-subtitle v-text="item.departamento"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-container>
</template>

<script>
  export default {
    name: 'FuncionarioList',

    data: () => ({
      list: [
        { nome: 'funcionario 1', departamento: 'IT', },
        { nome: 'funcionario 2', departamento: 'DESIGN', },
        { nome: 'funcionario 3', departamento: 'SUPORTE', },
      ],
    }),
  }
</script>
