<template>
  <div class="min-h-screen flex flex-col">
    <Nev />
    <main class="flex-grow">
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Nev from './components/Nev.vue';
import Footer from './components/Footer.vue';
</script>

<style>
/* Global styles or component-specific styles if needed */
</style>
