<template>
	<div class="col-span-6 mt-20 w-3/4">

		<div class="bg-gray-800 w-full h-16 rounded flex items-center pl-10 font-bold">
			<h2 class="text-2xl text-white"><i class="fa-solid fa-truck-arrow-right mr-1"></i> Calculadora de Viagem</h2>
		</div>

		<div class="grid grid-cols-2 height">
			<div class="bg-gray-300 w-3/4 h-5/6 mt-8 ml-8 flex flex-col items-center justify-center rounded">
				<h2 class="mb-5 text-2xl font-semibold"><i class="fa-solid fa-hand-holding-dollar"></i> Calcule o Valor da Viagem</h2>
				<form>
					<label for="inputCitys" class="block text-black-700 font-semibold mb-2">Destino</label>
					<input type="text" list="citys" id="inputCitys" name="inputCitys" placeholder="Selecione o Destino" class="w-80 form-input px-4 py-2 rounded-md focus:outline-none focus:ring">
					<datalist id="citys"></datalist>
					<label for="date" class="block text-black-700 font-semibold mb-2">Data</label>
					<input type="date" name="date" id="date" class="w-80 form-input px-4 py-2 rounded-md focus:outline-none focus:ring">
					<button type="submit" class="block bg-blue-500 hover:bg-blue-700 font-semibold rounded focus:outline-none focus:shadow-outline w-52 h-8 mt-10 mx-auto">Buscar</button>
				</form>
			</div>

			<div class="flex flex-col items-center justify-center">
				<h2 class="text-center text-xl font-bold">Nenhum dado selecionado...</h2>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.height {
		height: 40rem;
	}
</style>