import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: colors.purple.base,
        secondary: colors.teal.base,
        accent: '#673ab7',
        error: colors.pink.base,
        warning: colors.amber.base,
        info: '#607d8b',
        success: colors.green.base
      },
    },
  },
});
