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
        accent: colors.deep - colors.purple.base,
        error: colors.pink.base,
        warning: colors.amber.base,
        info: colors.blue - colors.grey.base,
        success: colors.green.base
      },
    },
  },
});
