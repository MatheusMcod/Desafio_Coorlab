<script setup>
import TripsCalculator from '../components/TripsCalculator.vue'
</script>

<template>
  <div class="grid h-screen grid-cols-6">
		<nav class="col-span-1 bg-gray-800 text-white">
			<div class="my-14 ml-5 w-52">
				<img src="../assets/logo.png" alt="Logo da empresa.">
			</div>
			<ul class="text-center">
        <li><button class="w-full h-10 hover:border hover:border-blue-500"><i class="fa-solid fa-calculator mr-2"></i> Calculadora de Viagem</button></li>
      </ul>
		</nav>
		<main class="col-span-5">
			<div class="w-full h-20 shadow-md shadow-gray-500 p-8"></div>
			<div class="flex justify-center"><TripsCalculator /></div>
		</main>
  </div>
</template>
