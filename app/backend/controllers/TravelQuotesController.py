from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from models.TravelQuotes import TravelQuotes


class TravelQuotesController:
	def __init__(self) -> None:
		pass

	def getAllTrips(self):
		try:
				trips = TravelQuotes().readJsonFileAndProcess('database/data.json')
				tripsToJson = jsonable_encoder(trips)
				return tripsToJson
		except ValueError as ve:
			raise HTTPException(status_code=400, detail=str(ve))
		except Exception as e:
			raise HTTPException(status_code=500, detail="Error getting trips: " + str(e))
