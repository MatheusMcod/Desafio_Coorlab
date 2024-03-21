from fastapi import APIRouter
from controllers.TravelQuotesController import TravelQuotesController
from typing import Any, Dict, List

routerInstance = APIRouter()

@routerInstance.get("/trips")
async def searchAllTrips() -> Dict[str, List]:
  response = await TravelQuotesController().searchAllTrips()
  return response

@routerInstance.get("/citys")
async def searchAllCitys() -> Dict[str, List]:
  response = await TravelQuotesController().searchAllCitys()
  return response

@routerInstance.get("/trips/{destination}")
async def searchTrips(destination: str) -> Dict[str, List]:
  response = await TravelQuotesController().searchDestinationTrips(destination)
  return response

