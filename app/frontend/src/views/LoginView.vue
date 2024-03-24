<template>
	<main class="container-lg h-screen grid grid-cols-2 lg:grid-cols-6 md:grid-cols-5">
    <div class="bg-gray-300 h-full w-full col-span-2 flex flex-col justify-center items-center">
			<h1 class="text-4xl font-bold text-black-800 mb-8 text-center">Faça o Login</h1>
			<form>
				<div class="mb-4">
					<label for="User" class="block text-black-700 text-2xl font-semibold mb-4">Usuario:</label>
					<input type="text" placeholder="Digite seu usuária" name="User" class="form-input px-4 lg:w-80 md:w-60 py-2 rounded-md focus:outline-none focus:ring">
				</div>
				<div class="mb-4">
					<label for="password" class="block text-black-700 text-2xl font-semibold mb-2">Senha:</label>
					<input type="password" placeholder="Digite sua senha" name="password" class="form-input px-4 lg:w-80 md:w-60 py-2 rounded-md focus:outline-none focus:ring">
				</div>

				<button type="button" @click="redirectHome" class="bg-blue-500 hover:bg-blue-700 font-semibold py-2 px-4 rounded focus:outline-none focus:shadow-outline lg:w-80 md:w-60"><i class="fa-solid fa-right-to-bracket"></i> Login</button>
			</form>
    </div>
    <div class="lg:col-span-4 md:col-span-3 sm:col-span-2 flex justify-center items-center">
			<img src="../assets/login.svg" alt="Imagem de um homem abrindo uma porta.">
    </div>
  </main>
</template>

<script>
export default {
  methods: {
    redirectHome() {
      this.$router.push('/home')
    }
  }
}
</script>

