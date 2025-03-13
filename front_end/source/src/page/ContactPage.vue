<template>
    <section class="contact-page min-h-screen bg-gray-800 text-white p-6 md:p-8">
      <div class="max-w-4xl mx-auto">
        <h1 class="text-3xl md:text-4xl font-bold mb-6">Contact Me</h1>
        <p class="mb-4">
          If you have any questions or would like to collaborate on a project, please send me a message.
        </p>
        <form class="space-y-4" @submit.prevent="handleSubmit">
          <div>
            <label for="name" class="block mb-1">Name</label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              required
              class="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white"
            />
          </div>
          <div>
            <label for="email" class="block mb-1">Email</label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              class="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white"
            />
          </div>
          <div>
            <label for="message" class="block mb-1">Message</label>
            <textarea
              id="message"
              v-model="form.message"
              required
              rows="5"
              class="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white"
            ></textarea>
          </div>
          <button type="submit" class="mt-4 px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-lg">
            Send Message
          </button>
        </form>
      </div>
    </section>
  </template>
  
  <script setup>
  import { reactive } from 'vue';
  
  const form = reactive({
    name: '',
    email: '',
    message: ''
  });
  
  const handleSubmit = () => {
    // Implement form submission logic here
    console.log("Form submitted:", form);
    // Reset form after submission
    form.name = '';
    form.email = '';
    form.message = '';
    alert("Your message has been sent!");
  };
  </script>
  
  <style scoped>
  /* Add any custom styles if needed */
  </style>
  