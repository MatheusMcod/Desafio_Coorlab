<template>
  <div class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center" @click="closeModal">
    <div class="bg-white p-8 rounded-lg w-2/5 h-2/5 flex flex-col justify-center items-center">
      <h3 class="text-blue-700 text-7xl mb-5"><i class="fa-solid fa-triangle-exclamation"></i></h3>
      <p class="font-semibold text-2xl mb-10">Insira os valores para realizar a cotação.</p>
      <button class="bg-blue-500 hover:bg-blue-700 font-semibold py-2 px-4 rounded focus:outline-none focus:shadow-outline lg:w-80 md:w-60" @click="closeModal">Fechar</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    closeModal() {
      this.$emit('close');
    }
  }
}
</script>