<template>
    <section class="bg-[#111827] min-h-screen flex flex-col">
      <!-- Navigation Modal -->
      <NevModal />
  
      <!-- Main Content -->
      <div class="container mx-auto flex-grow p-8 text-center">
        <!-- Personal Image -->
        <img
          src="./assets/ProjectManagement.jpg"
          alt="My Photo"
          class="w-48 h-48 rounded-full mx-auto mb-6 object-cover border-4 border-gray-600"
        />
  
        <!-- Heading Section -->
        <h2 class="heading--section text-4xl font-bold text-white mb-4">
          Here's My Story
        </h2>
  
        <!-- General Text -->
        <p class="text-white text-lg max-w-3xl mx-auto">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel neque sed neque convallis convallis. Curabitur lacinia, sapien eu tempor fermentum, eros ex finibus mi, ac luctus orci risus id arcu. Praesent aliquam, justo vitae maximus ultricies, arcu felis vulputate dolor, in sollicitudin erat nunc et nisi.
        </p>
      </div>
  
      <!-- Footer Modal -->
      <FooterModal />
    </section>
  </template>
  
  <script>
  import NevModal from "./components/Nev.vue";
  import FooterModal from "./components/Footer.vue";
  
  export default {
    name: "AboutPage",
    components: {
      NevModal,
      FooterModal,
    },
  };
  </script>

  