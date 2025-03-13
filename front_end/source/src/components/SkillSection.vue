<template>
  <section class="skill-section p-6 md:p-8 bg-gray-800">
    <!-- Section Header -->
    <div class="text-center mb-6 md:mb-12">
      <h2 class="text-3xl md:text-4xl font-bold text-white">Skills &amp; Tools</h2>
      <p class="mt-2 text-base md:text-lg text-white max-w-xl mx-auto">
          These are the things I love working with as a web developer.
      </p>
    </div>

    <!-- Two-column layout: Skill Categories and Skill Icons -->    
    <div class="grid grid-cols-1 md:grid-cols-[70%_30%] gap-6">
      <!-- Left Column: Skill Categories -->
      <div class="skill-categories p-4 bg-gray-900 rounded">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div v-for="(category, index) in categories" :key="index">
            <h3 class="text-xl md:text-2xl font-bold text-white mb-2">{{ category.title }}</h3>
            <ul class="space-y-1">
              <li
                v-for="(skill, idx) in category.skills"
                :key="idx"
                class="text-white text-sm md:text-base"
              >
                {{ skill.name }} <span class="text-gray-400 text-xs md:text-sm">({{ skill.level }})</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Right Column: Skill Icons -->
      <div class="skill-icons">
        <div class="grid grid-cols-3 gap-4 place-items-center md:grid-cols-2 lg:grid-cols-1">
          <div
            v-for="(iconItem, index) in skillIcons"
            :key="index"
            class="flex items-center justify-center rounded-full p-4 w-20 h-20 bg-gray-900"
          >
            <font-awesome-icon :icon="iconItem.icon" class="text-4xl text-white" />  
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faJs, faHtml5, faCss3Alt, faVuejs, faReact, faNodeJs } from '@fortawesome/free-brands-svg-icons';

export default {
  name: "SkillSection",
  components: {
    FontAwesomeIcon
  },
  data() {
    return {
      categories: [
        {
          title: "Language",
          skills: [
            { name: "JavaScript", level: "Expert" },
            { name: "HTML", level: "Expert" },
            { name: "CSS", level: "Expert" },
            { name: "TypeScript", level: "Intermediate" }
          ]
        },
        {
          title: "Data",
          skills: [
            { name: "REST APIs", level: "Expert" },
            { name: "MongoDB", level: "Intermediate" },
            { name: "Mongoose", level: "Intermediate" }
          ]
        },
        {
          title: "Libraries",
          skills: [
            { name: "Node", level: "Intermediate" },
            { name: "React JS", level: "Expert" },
            { name: "Redux", level: "Expert" },
            { name: "jQuery", level: "Expert" },
            { name: "Bootstrap", level: "Expert" },
            { name: "Express", level: "Intermediate" },
            { name: "Next JS", level: "Expert" }
          ]
        },
        {
          title: "Others",
          skills: [
            { name: "Git", level: "Intermediate" },
            { name: "Performance Optimization", level: "Expert" },
            { name: "Linux & Cyber Security", level: "Intermediate" },
            { name: "VS Code", level: "Expert" }
          ]
        }
      ],
      skillIcons: [
        { icon: faJs, title: "JavaScript" },
        { icon: faHtml5, title: "HTML" },
        { icon: faCss3Alt, title: "CSS" },
        { icon: faVuejs, title: "Vue.js" },
        { icon: faReact, title: "React" },
        { icon: faNodeJs, title: "Node.js" }
      ]
    };
  }
};
</script>

<style scoped>
/* Additional custom styles if needed */
</style>
