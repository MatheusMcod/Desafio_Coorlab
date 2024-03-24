from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from models.TravelQuotes import TravelQuotes
from typing import Dict, List
import re


class TravelQuotesController:
	def __init__(self) -> None:
		pass

	def __findCheapestTripAndComfortableTrip(self, trips: Dict[str, List], destination: str) -> Dict[str, List]:
		if not trips:
			raise ValueError("The array is empty")

		shorterTrip = None
		shorterTime = float('inf')
		economicTrip = None
		price = float('inf')

		for trip in trips:
			if trip["city"] == destination:
				tripTime = int(re.search(r'\d+', trip["duration"]).group())
				lowestPrice = float(re.search(r'\d+\.\d+', trip["price_econ"]).group())

				if tripTime < shorterTime:
					shorterTime = tripTime
					shorterTrip = trip

				if lowestPrice < price:
					price = lowestPrice
					economicTrip = trip

		return [shorterTrip, economicTrip]

	async def searchAllTrips(self) -> Dict[str, List]:
		try:
			trips = await TravelQuotes().readTransportFileAndProcess('database/transport.json')
			return jsonable_encoder(trips)
		except ValueError as ve:
			raise HTTPException(status_code=400, detail=str(ve))
		except Exception as e:
			raise HTTPException(status_code=500, detail="Error searching trips: " + str(e))

	async def searchAllCitis(self) -> Dict[str, List]:
		try:
			citis = await TravelQuotes().readCitisFileAndProcess('database/citis.json')
			return jsonable_encoder(citis)
		except ValueError as ve:
			raise HTTPException(status_code=400, detail=str(ve))
		except Exception as e:
			raise HTTPException(status_code=500, detail="Error searching citis: " + str(e))

	async def searchDestinationTrips(self, destination: str) -> Dict[str, List]:
		validDestinations = await TravelQuotes().readCitisFileAndProcess('database/citis.json')
		if destination not in validDestinations["citis"]:
			raise HTTPException(status_code=400, detail="The destination provided is not valid.")

		try:
			trips = await TravelQuotes().readTransportFileAndProcess('database/transport.json')
			destinationTrips =	self.__findCheapestTripAndComfortableTrip(trips["transport"], destination)
			return	{"trips": jsonable_encoder(destinationTrips)}
		except ValueError as ve:
			raise HTTPException(status_code=400, detail=str(ve))
		except Exception as e:
			raise HTTPException(status_code=500, detail="Error searching trips: " + str(e))