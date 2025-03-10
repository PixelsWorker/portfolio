<template> 
    <section class="p-8">
      <!-- Section Header -->
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold text-white">Work Experience</h2>
      </div>
      <!-- Resume Items -->
      <div class="resume-items space-y-8">
        <div
          v-for="(item, index) in resumeItems"
          :key="index"
          class="resume__item p-6 rounded-lg shadow-lg bg-gray-900 transition-transform transform hover:-translate-y-1 hover:shadow-2xl"
        >
          <!-- Duration -->
          <div class="resume__duration text-sm text-gray-400">
            {{ item.duration }}
          </div>
          <!-- Heading -->
          <div class="resume__heading text-2xl font-bold text-white mt-2">
            {{ item.heading }}
          </div>
          <!-- Position -->
          <div class="resume__position text-lg text-gray-300 mt-1">
            {{ item.position }}
          </div>
          <!-- Description Text with truncation -->
          <div class="resume__text text-base text-gray-200 mt-2">
            <template v-if="item.text.length > 50">
              <span>
                {{ item.expanded ? item.text : item.text.substring(0, 50) + '...' }}
              </span>
              <button class="text-blue-400 hover:underline ml-2" @click="toggleExpand(index)">
                {{ item.expanded ? 'See Less' : 'See More' }}
              </button>
            </template>
            <template v-else>
              {{ item.text }}
            </template>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "ResumeSection",
    data() {
      return {
        resumeItems: [
          {
            duration: "2018 - Present",
            heading: "Awesome Company",
            position: "Senior Developer",
            text:
              "Developing web applications and leading a team of developers to build scalable solutions. This role involves a lot of collaboration and problem solving.",
            expanded: false
          },
          {
            duration: "2015 - 2018",
            heading: "Tech Innovators",
            position: "Frontend Developer",
            text:
              "Built responsive web interfaces and collaborated with design teams to deliver exceptional user experiences.",
            expanded: false
          }
          // Add more resume items as needed...
        ]
      };
    },
    methods: {
      toggleExpand(index) {
        this.resumeItems[index].expanded = !this.resumeItems[index].expanded;
      }
    }
  };
  </script>

  