<script setup>
import { ref, onMounted } from 'vue';

const scrollToProjects = () => {
  const projectsSection = document.getElementById('projects');
  if (projectsSection) {
    projectsSection.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>

<template>
  <section class="banner-section flex items-center justify-center h-screen w-full px-6 md:px-8">
    <div class="banner__inner flex flex-col md:flex-row items-center max-w-6xl w-full gap-8 text-center md:text-left">
      <!-- Left: Content -->
      <div class="banner__content text-white flex-1">
        <h1 class="banner__heading text-3xl md:text-4xl font-bold">Rockson Kathar</h1>
        <p class="general-text text-base md:text-lg mt-4">
          Experienced frontend developer specializing in JavaScript, delivering exceptional user experiences.
          Let's collaborate on your next digital venture.
        </p>
        <button 
          class="mt-6 px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-lg flex items-center justify-center md:justify-start"
          @click="scrollToProjects"
        >
          Get Started
          <font-awesome-icon :icon="['fas', 'arrow-right']" class="ml-2" />
        </button>
      </div>

      <!-- Right: Image -->
      <div class="banner__image flex-1 flex justify-center">
        <img 
          src="../assets/ProjectManagement.jpg" 
          alt="Banner Image" 
          class="w-64 md:w-full h-auto rounded-lg shadow-lg" 
        />
      </div>
    </div>
  </section>
</template>

<style scoped>
.banner-section {
  position: relative;
  overflow: hidden;
}
</style>
