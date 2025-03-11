<template>
  <nav class="bg-black text-white py-4 fixed top-0 left-0 w-full z-50 shadow-lg">
    <div class="container mx-auto flex justify-between items-center px-4">
      <!-- Logo -->
      <div>
        <img src="../assets/logo.png" alt="Logo" class="h-10" />
      </div>
      
      <!-- Desktop Navigation & Resume (visible on md and up) -->
      <div class="hidden md:flex items-center space-x-6">
        <ul class="flex space-x-6">
          <li>
            <router-link to="/about" class="hover:text-gray-300">About</router-link>
          </li>
          <li>
            <a href="#projects" class="hover:text-gray-300">Projects</a>
          </li>
          <li>
            <a href="#contact" class="hover:text-gray-300">Contact</a>
          </li>
        </ul>
        <a
          href="https://docs.google.com/document/d/YOUR_DOCUMENT_ID/view"
          target="_blank"
          rel="noopener noreferrer"
          class="bg-slate-500 hover:bg-blue-600 text-black hover:text-white font-bold py-2 px-4 rounded"
        >
          Resume
        </a>
      </div>
      
      <!-- Mobile Menu Button (visible on small screens) -->
      <div class="md:hidden relative">
        <Menu as="div" class="relative inline-block text-left">
          <MenuButton class="focus:outline-none">
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </MenuButton>
          
          <transition 
            enter-active-class="transition-opacity ease-out duration-300" 
            enter-from-class="opacity-0" 
            enter-to-class="opacity-100" 
            leave-active-class="transition-opacity ease-in duration-200" 
            leave-from-class="opacity-100" 
            leave-to-class="opacity-0"
          >
            <MenuItems class="absolute right-0 mt-2 w-48 bg-black shadow-lg ring-1 ring-white ring-opacity-5 divide-y divide-gray-700 rounded-md z-50">
              <div class="py-1">
                <MenuItem v-slot="{ active }">
                  <router-link 
                    to="/about" 
                    :class="[active ? 'bg-gray-700' : '', 'block px-4 py-2 text-white']"
                  >
                    About
                  </router-link>
                </MenuItem>

                <MenuItem v-slot="{ active }">
                  <a 
                    href="#projects" 
                    :class="[active ? 'bg-gray-700' : '', 'block px-4 py-2 text-white']"
                  >
                    Projects
                  </a>
                </MenuItem>

                <MenuItem v-slot="{ active }">
                  <a 
                    href="#contact" 
                    :class="[active ? 'bg-gray-700' : '', 'block px-4 py-2 text-white']"
                  >
                    Contact
                  </a>
                </MenuItem>

                <MenuItem v-slot="{ active }">
                  <a 
                    href="https://docs.google.com/document/d/YOUR_DOCUMENT_ID/view"
                    target="_blank"
                    rel="noopener noreferrer"
                    :class="[active ? 'bg-gray-700' : '', 'block px-4 py-2 text-white text-center font-bold bg-slate-500 rounded']"
                  >
                    Resume
                  </a>
                </MenuItem>
              </div>
            </MenuItems>
          </transition>
        </Menu>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue';
</script>
