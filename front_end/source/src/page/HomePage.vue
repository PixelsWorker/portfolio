<template>
    <div class="min-h-screen bg-gray-950 text-gray-100">
      <SkillSectionModal />
      <ResumeSectionModal />
      <ProjectsListModel />
    </div>
  </template>
  
  <script setup>
  import SkillSectionModal from '../components/SkillSection.vue'
  import ResumeSectionModal from '../components/ResumeSection.vue'
  import ProjectsListModel from '../components/ProjectsList.vue'
  </script>
  