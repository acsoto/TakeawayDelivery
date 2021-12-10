import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
export default createStore({
  state: {
    userID: '',
    username: '',
    islogin: false,
    path: [],
    change: { star: false, orderNow: false }
  },
  mutations: {
    login(state, user) {
      state.islogin = true
      state.username = user.username
      state.userID = user.userID
    },

    setChange(state, param) {
      state.change[param.name] = param.value
    },

    setPath(state, param) {
      if (!state.initializing) {
        state.path = []
        state.path.push({ isFather: true, name: param.name, index: 0 })
      }
    },

    pushPath(state, param) {
      var length = state.path.length
      var hasPath = false
      var index = 0
      for (var i = 0; i < length; i++) {
        if (state.path[i].name == param.name) {
          hasPath = true
          index = i
          break
        }
      } //如果面包屑中已经有了这一项，则删除原来的面包屑及之后的所有内容
      if (hasPath) {
        for (i = length - 1; i > index; i--) {
          state.path.splice(i, 1)
        }
      }
      length = state.path.length
      if (state.path[length - 1].name != param.name)
        state.path.push({
          isFather: false,
          name: param.name,
          to: param.to,
          index: length
        })
    },

    deletePath(state, param) {
      for (var i = state.path.length - 1; i > param.index; i--) {
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
