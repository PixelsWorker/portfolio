<template>
  <div class="min-h-screen bg-gray-950 text-gray-100">
    <NevModal />
    <SkillSectionModal />
    <ResumeSectionModal />
    <ProjectsListModel />
    <FooterModal />
  </div>
</template>

<script setup>
import NevModal from './components/Nev.vue'
import SkillSectionModal from './components/SkillSection.vue'
import ResumeSectionModal from './components/ResumeSection.vue'
import ProjectsListModel from './components/ProjectsList.vue'
import FooterModal from './components/Footer.vue'
</script>
