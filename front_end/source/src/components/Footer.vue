<template>
    <section class="bg-gray-900 text-white py-16 text-center">
    <h2 class="text-4xl font-bold mb-4">Say hello!</h2>
    <p class="text-gray-400 max-w-2xl mx-auto">
        If you want to talk to me about something that could interest me or just want to say hi,
        you can send me an email at 
        <a href="mailto:rockson@gmail.com" class="text-blue-400 hover:underline">@rockson</a>.
        My inbox is always open.
    </p>
    </section>
    
  <footer class="text-white py-6 mt-10">
    <div class="container mx-auto text-center">
      <div class="mb-4">
        <img src="../assets/logo.png" alt="Logo" class="h-12 mx-auto" />
      </div>
      <p class="mb-4 text-gray-400">
        Crafting digital experiences with passion and precision.
      </p>
      <div class="flex justify-center space-x-6">
        <a
          href="https://linkedin.com/in/YOUR_PROFILE"
          target="_blank"
          class="text-white hover:text-gray-400"
        >
          <!-- Using array syntax for brand icon -->
          <font-awesome-icon :icon="['fab', 'linkedin']" class="text-2xl" />
        </a>
        <a
          href="https://github.com/YOUR_GITHUB"
          target="_blank"
          class="text-white hover:text-gray-400"
        >
          <!-- Using array syntax for brand icon -->
          <font-awesome-icon :icon="['fab', 'github']" class="text-2xl" />
        </a>
        <a href="mailto:rockson@gmail.com" class="text-white hover:text-gray-400">
          <!-- Using array syntax for solid icon -->
          <font-awesome-icon :icon="['fas', 'envelope']" class="text-2xl" />
        </a>
      </div>
    </div>
  </footer>
</template>


  