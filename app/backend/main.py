from fastapi import FastAPI
import uvicorn
from routes.app import App
from routes.routes import routerInstance
from controllers.TravelQuotesController import TravelQuotesController
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
]

app_instance = App().getAppInstance()
app_instance.include_router(routerInstance)
app_instance.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

if __name__ == "__main__":
  uvicorn.run(app_instance, host="0.0.0.0", port=3000)