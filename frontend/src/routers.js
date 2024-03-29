import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/Homepage.vue';
import LoginPage from './views/LoginPage.vue';
import ContactUs from './views/ContactUs.vue';
import SignUp from './views/SignUp.vue';
import QuestionSearch from './views/QuestionSearch.vue';
import SemanticSearch from './views/SemanticSearch.vue';
import AccountPage from './views/AccountPage.vue'
import ChangePassword from './views/ChangePassword.vue';

const routes = [
    {
        name: "HomePage",
        component: HomePage,
        path: "/",
    },
    {
        name: "SignUp",
        component: SignUp,
        path: "/sign-up",
    },
    {
        name: "LoginPage",
        component: LoginPage,
        path: "/login",
    },
    {
        name: "ContactUs",
        component: ContactUs,
        path: "/contact-us",
    },
    {
        name: "QuestionSearch",
        component: QuestionSearch,
        path: "/question",
    },
    {
        name: "SemanticSearch",
        component: SemanticSearch,
        path: "/semantic",
    },
    {
        name: "AccountPage",
        component: AccountPage,
        path: "/account"
    },
    {
        name: "ChangePassword",
        component: ChangePassword,
        path: "/change"
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
