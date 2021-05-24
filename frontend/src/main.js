import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

//谨慎扩展原生类型
URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};

createApp(App).use(router).mount('#app')
