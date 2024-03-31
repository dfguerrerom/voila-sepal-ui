Vue.component('loading-card', {
  template: `
    <v-layout v-show="loading" align-center justify-center>
      <v-card style="min-width: 600px">
        <v-progress-linear indeterminate="true" height="8"></v-progress-linear>
        <v-card-text
          style="display: flex; flex-direction: column; align-items: center"
        >
          <v-card-title>
            <h2>Loading the module</h2>
          </v-card-title>

          <v-card-subtitle>
            <h3>{{ loading_text }}</h3>
          </v-card-subtitle>
          <img
            :src="imageUrl"
            alt="SEPAL loading"
            align-center
            justify-center
            width="250px"
          />
        </v-card-text>
      </v-card>
    </v-layout>
  `,
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
    loading_text: {
      type: String,
      default: "Loading...",
    },
    imageUrl: {
      type: String,
      default: "/img/loading.gif",
    },
  },
});