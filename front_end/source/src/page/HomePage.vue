<script setup>
import BannerSection from '../components/BannerSection.vue';
import ProjectsList from '../components/ProjectsList.vue';
import ResumeSection from '../components/ResumeSection.vue';
import SkillSection from '../components/SkillSection.vue';
import bgImage from '../assets/background.jpg';
</script>

<template>
  <section
    class="home-page min-h-screen bg-fixed bg-center bg-cover bg-no-repeat text-white"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <div class="max-w-6xl mx-auto p-6 md:p-8">
      <!-- Banner Section -->
      <BannerSection />
      <!-- Projects Section -->
      <ProjectsList />
      <!-- Resume Section -->
      <ResumeSection />
      <!-- Skills Section -->
      <SkillSection />
    </div>
  </section>
</template>

<style scoped>
/* Additional custom styles if needed */
</style>
