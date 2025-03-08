import { createApp } from 'vue'
import App from './App.vue'
import './style.css'  // Your Tailwind CSS file

// Import the Motion plugin from VueUse/motion
import { MotionPlugin } from '@vueuse/motion'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faEnvelope, faCode } from '@fortawesome/free-solid-svg-icons'
import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons'

// Add icons to the library
library.add(faEnvelope, faCode, faLinkedin, faGithub)

const app = createApp(App)
app.use(MotionPlugin)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
