from fastapi import APIRouter

routerInstance = APIRouter()

@routerInstance.get("/")
def home():
    return "OK"


