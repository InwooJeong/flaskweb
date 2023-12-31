import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import { createI18n } from 'vue-i18n'
import messages from './i18n'

const app = createApp(App)

const i18n = createI18n({
    locale: 'ko',
    fallbackLocale: 'en',
    messages
})

app.use(router).use(i18n)

app.mount('#app')
