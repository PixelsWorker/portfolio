<template>
  <div class="min-h-screen bg-gray-950 text-gray-100">
    <NevModal />
    <router-view />
    <FooterModal />
  </div>
</template>

<script setup>
import NevModal from './components/Nev.vue'
import FooterModal from './components/Footer.vue'
</script>