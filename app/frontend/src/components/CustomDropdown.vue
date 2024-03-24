<template>
  <div class="relative">
    <div @click="toggleDropdown" class="w-full form-input px-4 py-2 rounded-md focus:outline-none hover:ring cursor-pointer bg-white flex items-center justify-between">
      <span>{{ selectedOption || placeholder }}</span>
      <i :class="['fas', {'fa-angle-right': !isDropdownOpen, 'fa-angle-down': isDropdownOpen}, 'ml-2']"></i>
    </div>
    <div v-if="isDropdownOpen" class="absolute z-10 mt-1 w-full bg-white rounded-md shadow-lg">
      <div v-for="(option, index) in options" :key="index" @click="selectOption(option)" class="cursor-pointer px-4 py-2 hover:bg-gray-100"><i class="fa-solid fa-circle text-gray-400"></i> {{ option }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: String,
    options: Array,
    placeholder: String
  },
  data() {
    return {
      selectedOption: this.value,
      isDropdownOpen: false
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    selectOption(option) {
      this.selectedOption = option;
      this.isDropdownOpen = false;
      this.$emit('input', option);
    }
  },
  watch: {
    value(newValue) {
      this.selectedOption = newValue;
    }
  }
};
</script>