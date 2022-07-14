import Vue from 'vue'
import Vuex from 'vuex'

// const Sqlite = require('sqlite3')
// // const db = new sqlite3.Database(':memory:')

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    database: null,
    data: [],
    users : [
      { username: "advay@gmail.com", password: "mehta" },
      { username: "nitish@gmail.com", password: "tiwari" },
      { username: "mdlucky@gmail.com", password: "lucky" },
    ],
  },

  actions: {
   }
});
