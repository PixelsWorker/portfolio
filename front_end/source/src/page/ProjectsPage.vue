<template>
    <section class="projects-page min-h-screen bg-gray-800 text-white p-6 md:p-8">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl md:text-4xl font-bold mb-6">Projects</h1>
        <ProjectsList />
      </div>
    </section>
  </template>
  
  <script setup>
  import ProjectsList from '../components/ProjectsList.vue';
  </script>
  
  <style scoped>
  /* Add additional styles if needed */
  </style>
  