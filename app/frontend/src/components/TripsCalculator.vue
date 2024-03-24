<template>
	<div class="col-span-6 mt-20 w-3/4">

		<div class="bg-gray-800 w-full h-16 rounded flex items-center pl-10 font-bold">
			<h2 class="text-2xl text-white"><i class="fa-solid fa-truck-arrow-right mr-1"></i> Calculadora de Viagem</h2>
		</div>

		<div class="grid grid-cols-2 height">
			<div class="bg-gray-300 w-3/4 h-5/6 mt-8 ml-8 flex flex-col items-center justify-center rounded">
				<h2 class="mb-5 text-2xl font-semibold"><i class="fa-solid fa-hand-holding-dollar"></i> Calcule o Valor da Viagem</h2>
				<form @submit.prevent="searchTrips">
					<label for="citis" class="block text-black-700 font-semibold mb-2">Destino</label>
					<select id="citis" name="citis" class="w-80 form-input px-4 py-2 rounded-md focus:outline-none hover:ring cursor-pointer" v-model="selectedCiti"><option></option></select>
					<label for="date" class="block text-black-700 font-semibold mb-2">Data</label>
					<input type="date" name="date" id="date" class="w-80 form-input px-4 py-2 rounded-md focus:outline-none hover:ring cursor-pointer" v-model="selectedDate">
					<button type="submit" class="block bg-blue-500 hover:bg-blue-700 font-semibold rounded focus:outline-none focus:shadow-outline w-52 h-8 mt-10 mx-auto">Buscar</button>
				</form>
			</div>

			<div class="flex flex-col items-center justify-center">
				<div>
					<showTrips :trips="tripsData"/>
				</div>
			</div>
		</div>
		<ModalAlert v-if="showModal" @close="closeModal" />
	</div>
</template>

<script>
	import ShowTrips from './ShowTrips.vue'
	import ModalAlert from './ModalAlert.vue';

	export default {
  mounted() {
    this.searchCities();
  },
	components: {
		ShowTrips,
		ModalAlert
	},
  methods: {
    async searchCities() {
      try {
        const response = await fetch('http://localhost:3000/citis');
        const data = await response.json();

        const datalist = document.getElementById('citis');
        datalist.innerHTML = '';
				datalist.appendChild(document.createElement('option'));

        data.citis.forEach(citi => {
          const option = document.createElement('option');
          option.textContent = citi;
          datalist.appendChild(option);
        });
      } catch (error) {
        console.error('Erro ao obter cidades:', error);
      }
    },

		async searchTrips() {
			try {
				if (!this.selectedCiti || !this.selectedDate) {
          this.showModal = true;
          return;
        }

				const response = await fetch(`http://localhost:3000/trips/${this.selectedCiti}`);
				const data = await response.json();
				console.log(data.trips)
				this.tripsData = data.trips;
			} catch (error) {
					console.error('Erro ao obter cidades:', error);
			}
    },

		closeModal() {
      this.showModal = false;
    }
  },
	data() {
    return {
      selectedCiti: '',
			tripsData: [],
			showModal: false,
			selectedDate: ''
  	}
	}
}
</script>

<style scoped>
	.height {
		height: 40rem;
	}
</style>