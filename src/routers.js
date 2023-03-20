import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/Homepage.vue';
import LoginPage from './components/LoginPage.vue';
import ContactUs from './components/ContactUs.vue';
import SignUp from './components/SignUp.vue';
import QuestionSearch from './components/QuestionSearch.vue';
import SemanticSearch from './components/SemanticSearch.vue';

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
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;