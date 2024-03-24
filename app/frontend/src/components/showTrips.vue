<template>
  <div v-if="trips && trips.length">
		<h2 class="mb-8 font-semibold">Estas são as melhores alternativas de viagem para data selecionada</h2>
    <div class="flex gap-x-0">
			<div class="w-24 h-28 bg-blue-500 text-white rounded flex justify-center items-center text-6xl mb-5"><i class="fa-solid fa-hand-holding-dollar"></i></div>
			<div class="w-64 h-28 rounded bg-gray-300 flex flex-col justify-center pl-5">
				<h3 class="font-bold text-lg">{{ trips[0].name }}</h3>
				<p class="font-semibold">Leito: {{ trips[0].bed }} (Completo)</p>
				<p class="font-semibold">Tempo estimado: {{ trips[0].duration }}</p>
			</div>
			<div class="flex flex-col justify-center ml-5 h-28 w-40 rounded bg-gray-300 pl-4">
				<h3 class="font-bold text-lg">Preço</h3>
				<p class="font-semibold">{{ trips[0].price_confort }}</p>
			</div>
    </div>

    <div class="flex">
			<div class="w-24 h-28 bg-blue-500 text-white rounded flex justify-center items-center text-6xl"><i class="fa-regular fa-clock"></i></div>
			<div class="w-64 h-28 rounded bg-gray-300 flex flex-col justify-center pl-5">
				<h3 class="font-bold text-lg">{{ trips[1].name }}</h3>
				<p class="font-semibold">Poltrona: {{ trips[1].seat }} (Convencional)</p>
				<p class="font-semibold">Tempo estimado: {{ trips[1].duration }}</p>
			</div>
      <div class="flex flex-col justify-center ml-5 h-28 w-40 rounded bg-gray-300 pl-4">
				<h3 class="font-bold text-lg">Preço</h3>
				<p class="font-semibold">{{ trips[1].price_econ }}</p>
			</div>
    </div>
  </div>
	<div v-else>
    <h2 class="text-center text-xl font-bold">Nenhum dado selecionado...</h2>
  </div>
</template>

<script>
export default {
  props: {
    trips: Array
  }
}
</script>