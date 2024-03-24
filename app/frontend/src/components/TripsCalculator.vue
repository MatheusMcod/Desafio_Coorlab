<template>
  <div class="col-span-6 mt-16 w-full h-3/5 lg:w-3/4 lg:shadow-md lg:shadow-gray-500 p-8">
    <div class="bg-gray-800 w-full h-16 rounded flex items-center pl-10 font-bold">
      <h2 class="text-2xl text-white"><i class="fa-solid fa-truck-arrow-right mr-1"></i> Calculadora de Viagem</h2>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8 h-full">
      <div class="bg-gray-300 w-full h-auto lg:h-5/6 flex flex-col items-center justify-center rounded p-8">
        <h2 class="mb-5 text-2xl lg:text-base md:text-sm font-semibold break-words"><i class="fa-solid fa-hand-holding-dollar"></i> Calcule o Valor da Viagem</h2>
        <form @submit.prevent="searchTrips" class="w-full">
          <label for="cities" class="block text-black-700 font-semibold mb-2">Destino</label>
          <CustomDropdown v-model="selectedCiti" :options="cities" @input="handleOptionSelected" placeholder="Selecione uma cidade" name="cities" />
          <label for="date" class="block text-black-700 font-semibold mb-2">Data</label>
          <input type="date" name="date" id="date" class="w-full form-input px-4 py-2 rounded-md focus:outline-none hover:ring cursor-pointer" v-model="selectedDate">
          <button type="submit" class="block bg-blue-500 hover:bg-blue-700 font-semibold rounded focus:outline-none focus:shadow-outline w-full h-10 mt-6">Buscar</button>
        </form>
      </div>

      <div class="w-full h-auto lg:h-3/4 flex flex-col items-center justify-center rounded p-4">
        <div class="w-full h-full">
          <showTrips :trips="tripsData"/>
        </div>
      </div>
    </div>
    <ModalAlert v-if="showModal" @close="closeModal" />
  </div>
</template>
<script>
import ShowTrips from './ShowTrips.vue'
import ModalAlert from './ModalAlert.vue'
import CustomDropdown from './CustomDropdown.vue'

export default {
  mounted() {
    this.searchCities();
  },
  components: {
    ShowTrips,
    ModalAlert,
    CustomDropdown
  },
  methods: {
    async searchCities() {
      try {
        const response = await fetch('http://localhost:3000/cities');
        const data = await response.json();

        this.cities = data.cities;
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
        this.tripsData = data.trips;
      } catch (error) {
        console.error('Erro ao obter cidades:', error);
      }
    },
    closeModal() {
      this.showModal = false;
    },
		handleOptionSelected(option) {
      this.selectedCiti = option;
    }
  },
  data() {
    return {
      selectedCiti: '',
      tripsData: [],
      showModal: false,
      selectedDate: '',
      cities: []
    };
  }
};
</script>

<style scoped>
.height {
  height: 40rem;
}
</style>