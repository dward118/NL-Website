import { createStore } from 'vuex'

import { decodeToken } from './token'

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
                state.token = localStorage.getItem('refresh')
                state.isAuthenticated = true

            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, accessToken, refreshToken) {
            state.access = accessToken
            state.refresh = refreshToken
            state.isAuthenticated = true

            const decodedRefresh = decodeToken(refreshToken)

            state.username = decodedRefresh['username']
            state.first_name = decodedRefresh['first_name']
            state.last_name = decodedRefresh['last_name']
            state.email = decodedRefresh['email']
            state.institution = decodedRefresh['institution']
            state.experience = decodedRefresh['experience']
            state.approved = decodedRefresh['approved']

            console.log(state.username)
            console.log(state.institution)
        },
        removeToken(state) {
            state.access = ''
            state.refresh = ''
            state.isAuthenticated = false

            state.username = ''
            state.first_name = ''
            state.last_name = ''
            state.email = ''
            state.institution = ''
            state.experience = ''
            state.approved = ''
        },
    },

    actions: {},

    modules: {}
})
