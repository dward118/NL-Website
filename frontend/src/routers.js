import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/Homepage.vue';
import SignIn from './views/SignIn.vue';
import ContactUs from './views/ContactUs.vue';
import SignUp from './views/SignUp.vue';
import QuestionSearch from './views/QuestionSearch.vue';
import SemanticSearch from './views/SemanticSearch.vue';

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
        name: "SignIn",
        component: SignIn,
        path: "/sign-in",
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