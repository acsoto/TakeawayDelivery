import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
export default createStore({
  state: {
    userID: '',
    username: '',
    islogin: false,
    path: [
      { isFather: true, name: '个人中心', index: 0 },
      {
        isFather: false,
        name: '个人信息',
        to: '/home/userinfo',
        index: 1
      }
    ]
  },
  mutations: {
    login(state, user) {
      state.islogin = true
      state.username = user.username
      state.userID = user.userID
    },

    setPath(state, param) {
      state.path = []
      state.path.push({ isFather: true, name: param.name, index: 0 })
    },

    pushPath(state, param) {
      var length = state.path.length
      state.path.push({
        isFather: false,
        name: param.name,
        to: param.to,
        index: length
      })
    },

    deletePath(state, param) {
      for (var i = state.path.length - 1; i >= param.index; i--) {
        state.path.splice(i, 1)
      }
    },

    changeName(state, username) {
      state.username = username
    },

    logout(state) {
      state.islogin = false
      state.username = ''
      state.userID = ''
    }
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState()]
})
