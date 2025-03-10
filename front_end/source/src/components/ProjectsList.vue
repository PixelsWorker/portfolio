<template>
    <section class="projects-section p-8">
      <!-- Section Header -->
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold text-white">Projects</h2>
        <p class="mt-4 text-lg text-white">
          I made these in my spare time for learning purposes or experimentation.
        </p>
      </div>
  
      <!-- Projects List -->
      <div class="projects-list grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="project in projects"
          :key="project.id"
          class="project-card bg-gray-900 p-6 rounded-lg shadow-md transition-transform transform hover:-translate-y-1 hover:shadow-2xl"
        >
          <!-- Project Image -->
          <img
            :src="project.image"
            :alt="project.title"
            class="w-full h-auto mb-4 rounded"
          />
  
          <!-- Skills & Tech List -->
          <div class="project-skills mb-2">
            <h3 class="font-semibold text-white mb-2">Skills &amp; Tech:</h3>
            <ul class="flex flex-wrap gap-2">
              <li
                v-for="(skill, index) in project.skills"
                :key="'skill-' + index"
                class="text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded"
              >
                {{ skill }}
              </li>
              <li
                v-for="(tech, index) in project.tech"
                :key="'tech-' + index"
                class="text-sm bg-green-100 text-green-800 px-2 py-1 rounded"
              >
                {{ tech }}
              </li>
            </ul>
          </div>
  
          <!-- Project Short Description -->
          <p class="project__short-description text-white mt-3">
            {{ project.shortDescription }}
          </p>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import projectManagementImage from "../assets/ProjectManagement.jpg";
  
  export default {
    name: "ProjectsList",
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
        title: "Project Two",
        // Use the imported variable instead of require().
        image: projectManagementImage,
        skills: ["HTML", "CSS", "JavaScript"],
        tech: ["React", "Next.js"],
        shortDescription:
            "A short description of project two. It is a modern web application built with React."
        },
        {
        id: 3,
        title: "Project Two",
        // Use the imported variable instead of require().
        image: projectManagementImage,
        skills: ["HTML", "CSS", "JavaScript"],
        tech: ["React", "Next.js"],
        shortDescription:
            "A short description of project two. It is a modern web application built with React."
        },
          // Add more project objects as needed...
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  /* Additional styles can be added here if necessary */
  </style>
  