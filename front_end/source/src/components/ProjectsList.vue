<template>
  <section id="projects" class="projects-section p-8 bg-gradient-dark">
    <!-- Section Header -->
    <div class="text-center mb-12 animate-fade-in">
      <h2 class="section-heading">Projects</h2>
      <p class="mt-4 text-lg text-white">
        I made these in my spare time for learning purposes or experimentation.
      </p>
    </div>

    <!-- Projects List -->
    <div class="projects-list grid gap-8 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="(project, i) in projects"
        :key="project.id"
        class="hover-card bg-gray-900 p-6 rounded-lg stagger-item"
        :class="'stagger-delay-' + ((i % 5) + 1)"
      >
        <!-- Project Image -->
        <img
          :src="project.image"
          :alt="project.title"
          class="w-full h-48 object-cover mb-4 rounded"
        />

        <!-- Project Title -->
        <h3 class="text-xl font-bold text-white mb-3">{{ project.title }}</h3>

        <!-- Skills & Tech List -->
        <div class="project-skills mb-3">
          <h4 class="font-semibold text-white mb-2">Skills &amp; Tech:</h4>
          <ul class="flex flex-wrap gap-2">
            <li
              v-for="(skill, index) in project.skills"
              :key="'skill-' + index"
              class="text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded-full"
            >
              {{ skill }}
            </li>
            <li
              v-for="(tech, index) in project.tech"
              :key="'tech-' + index"
              class="text-sm bg-green-100 text-green-800 px-2 py-1 rounded-full"
            >
              {{ tech }}
            </li>
          </ul>
        </div>

        <!-- Project Short Description -->
        <p class="text-gray-300 mt-3">
          {{ project.shortDescription }}
        </p>
        
        <!-- Links -->
        <div class="mt-4 flex space-x-4">
          <a href="#" class="primary-button">View Project</a>
          <a href="#" class="text-gray-400 hover:text-white">
            <font-awesome-icon :icon="['fab', 'github']" class="mr-1" /> Code
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import projectManagementImage from "../assets/ProjectManagement.jpg";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
  name: "ProjectsList",
  components: {
    FontAwesomeIcon
  },
  data() {
    return {
      projects: [
        {
          id: 1,
          title: "Project One",
          image: projectManagementImage,
          skills: ["Vue", "TailwindCSS", "JavaScript"],
          tech: ["Vue 3", "Vite"],
          shortDescription:
            "A short description of project one. It demonstrates how to use Vue components effectively."
        },  
        {
          id: 2,
          title: "E-commerce Platform",
          image: projectManagementImage,
          skills: ["HTML", "CSS", "JavaScript"],
          tech: ["React", "Next.js"],
          shortDescription:
            "A modern e-commerce platform with product listings, shopping cart, and checkout functionality."
        },
        {
          id: 3,
          title: "Task Management App",
          image: projectManagementImage,
          skills: ["Vue", "Firebase", "JavaScript"],
          tech: ["Vue 3", "Vuex"],
          shortDescription:
            "A collaborative task management application with real-time updates and team features."
        }
      ]
    };
  }
};
</script>