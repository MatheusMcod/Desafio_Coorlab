from fastapi import APIRouter
from controllers.TravelQuotesController import TravelQuotesController

routerInstance = APIRouter()

@routerInstance.get("/trips")
def home():
  response = TravelQuotesController().getAllTrips()
  return response


