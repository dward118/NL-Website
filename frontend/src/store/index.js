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
                populateStore(state, state.refresh)

            } else {
                state.access = ''
                state.refresh = ''

                depopulateStore(state)
            }
        },
        setToken(state, tokens) {
            state.access = tokens.access
            state.refresh = tokens.refresh

            populateStore(state, state.refresh) 
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
