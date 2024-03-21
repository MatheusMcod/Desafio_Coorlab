from fastapi import APIRouter
from controllers.TravelQuotesController import TravelQuotesController
from typing import Any

routerInstance = APIRouter()

@routerInstance.get("/trips")
async def searchAllTrips():
  response = await TravelQuotesController().searchAllTrips()
  return response


@routerInstance.get("/trips/{destination}")
async def searchTrips(destination: str):
  response = await TravelQuotesController().searchDestinationTrips(destination)
  return response

