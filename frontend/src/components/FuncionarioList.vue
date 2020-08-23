<template>
  <v-container>
    <v-list>
      <v-list-item-group color="primary">
        <v-list-item
          v-for="(item, i) in funcionarios"
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

    computed: {
      funcionarios() {
        return this.$store.state.funcionarios
      },
    },
  }
</script>
