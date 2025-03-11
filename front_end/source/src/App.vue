<template>
  <div class="min-h-screen text-gray-100 backgrund-qw">
    <NevModal />
    <br>
    <br>
    <router-view />
    <br>
    <br>
    <FooterModal />
  </div>
</template>

<script setup>
import NevModal from './components/Nev.vue'
import FooterModal from './components/Footer.vue'
</script>