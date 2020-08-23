<template>
<v-card
  class="mx-auto"
  v-if="funcionarios"
  >
  <v-pagination
    v-model="page"
    :length="Math.ceil(funcionarios.count / 10)"
    class="secondary"
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
</v-card>
<v-content
  fill-height
  fluid
  v-else
  >
  <v-row
    align="center"
    justify="center"
    >
    <v-progress-circular
      indeterminate
      color="secondary"
      >
    </v-progress-circular>
  </v-row>
</v-content>
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
