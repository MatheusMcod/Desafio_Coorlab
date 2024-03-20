from fastapi import FastAPI
import uvicorn
from routes.app import App
from routes.routes import routerInstance
from controllers.TravelQuotesController import TravelQuotesController

app_instance = App().getAppInstance()

app_instance.include_router(routerInstance)

if __name__ == "__main__":
  uvicorn.run(app_instance, host="0.0.0.0", port=3000)