<template>
<v-container>
  <div v-if="funcionarios">
    <v-pagination
      v-model="page"
      :length="funcionarios.next + funcionarios.previous"
      ></v-pagination>
    <v-list>
      <v-list-item-group color="primary">
        <v-list-item
          v-for="(item, i) in funcionarios.results"
          :key="i"
          >
          <v-list-item-content>
            <v-list-item-title v-text="item.nome"></v-list-item-title>
            <v-list-item-subtitle v-text="item.departamento"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </div>
  <v-progress-circular
    indeterminate
    v-else
    color="secondary"
    ></v-progress-circular>
</v-container>
</template>

<script>
  export default {
    name: 'FuncionarioList',

    computed: {
      funcionarios() {
        return this.$store.state.funcionarios
      },
    },
    
    created() {
      this.$store.dispatch('fetchFuncionarios')
    },
      
  }
</script>
