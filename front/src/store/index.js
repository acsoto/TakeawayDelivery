import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate"
export default createStore({
    state: {
        userID:"",
        username:"",
        islogin: false,
        
    },
    mutations: {
        login(state, user) {
            state.islogin = true
            state.username = user.username
            state.userID=user.userID
        },
        
        changeName(state,username){
            state.username = username
        },
        
        logout(state) {
            state.islogin = false
            state.username = ""
            state.userID = ""
        },
        // 标签页相关操作
        // delTagsItem(state, data) {
        //     state
        //         .tagsList
        //         .splice(data.index, 1);
        // },
        // setTagsItem(state, data) {
        //     state
        //         .tagsList
        //         .push(data)
        // },
        // clearTags(state) {
        //     state.tagsList = []
        // },
        // closeTagsOther(state, data) {
        //     state.tagsList = data;
        // },
        // closeCurrentTag(state, data) {
        //     for (let i = 0, len = state.tagsList.length; i < len; i++) {
        //         const item = state.tagsList[i];
        //         if (item.path === data.$route.fullPath) {
        //             if (i < len - 1) {
        //                 data
        //                     .$router
        //                     .push(state.tagsList[i + 1].path);
        //             } else if (i > 0) {
        //                 data
        //                     .$router
        //                     .push(state.tagsList[i - 1].path);
        //             } else {
        //                 data
        //                     .$router
        //                     .push("/");
        //             }
        //             state
        //                 .tagsList
        //                 .splice(i, 1);
        //             break;
        //         }
        //     }
        // },
        // 侧边栏折叠
        // hadndleCollapse(state, data) {
        //     state.collapse = data;
        // }
    },
    actions: {},
    modules: {},
    plugins: [createPersistedState()]
})