<template>
  <section class="about-page p-6 md:p-8 bg-gray-800 min-h-screen text-white">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl md:text-4xl font-bold mb-4 border-b border-gray-600 pb-2">
        About Me
      </h1>
      <p class="text-base md:text-lg mb-6 leading-relaxed">
        I'm Rockson Kathar, an experienced frontend developer specializing in modern JavaScript frameworks and building engaging user interfaces.
      </p>
      <div class="flex flex-col md:flex-row gap-6 mb-8">
        <img
          src="../assets/profile.jpg"
          alt="Profile Image"
          class="w-48 h-48 object-cover rounded-full mx-auto md:mx-0 transform transition duration-300 hover:scale-105"
        />
        <div class="flex flex-col justify-center">
          <p class="mb-4">
            With a passion for technology and a commitment to excellence, I strive to create seamless digital experiences.
          </p>
          <p>
            I enjoy collaborating on innovative projects and am always looking for new challenges.
          </p>
        </div>
      </div>
      <!-- Social Media Icons -->
      <div class="flex justify-center md:justify-start space-x-4">
        <a
          href="https://linkedin.com/in/yourprofile"
          target="_blank"
          class="text-blue-400 hover:text-blue-300"
        >
          <font-awesome-icon :icon="['fab', 'linkedin']" size="2x" />
        </a>
        <a
          href="https://github.com/yourusername"
          target="_blank"
          class="text-gray-300 hover:text-gray-400"
        >
          <font-awesome-icon :icon="['fab', 'github']" size="2x" />
        </a>
        <a href="mailto:rockson@gmail.com" class="text-red-400 hover:text-red-300">
          <font-awesome-icon :icon="['fas', 'envelope']" size="2x" />
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
</script>

<style scoped>
/* Additional custom styles if needed */
</style>
