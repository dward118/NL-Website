import { createStore } from 'vuex'

import { populateStore, depopulateStore } from './token.js'

export default createStore({
    state: {
        access: '',
        refresh: '',
        isAuthenticated: false,

        username: '',
        first_name: '',
        last_name: '',
        email: '',
        institution: '',
        experience: '',
        approved: false
    },

    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('refresh')) {
                state.refresh = localStorage.getItem('refresh')
                console.log("init")
                populateStore(state, state.refresh)

            } else {
                state.access = ''
                state.refresh = ''

                depopulateStore(state)
            }
        },
        setToken(state, accessToken, refreshToken) {
            state.access = accessToken
            state.refresh = refreshToken //TODO refreshToken is always undefined
            console.log("set token")
            console.log(state.access)
            console.log(state.refresh)

            populateStore(state, accessToken) 

            console.log(state.username)
            console.log(state.institution)
        },
        removeToken(state) {
            state.access = ''
            state.refresh = ''

            depopulateStore(state)
        },
    },

    actions: {},

    modules: {}
})
