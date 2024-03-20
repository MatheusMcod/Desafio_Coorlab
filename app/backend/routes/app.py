from fastapi import FastAPI

class App:
	def __init__(self):
		self.__app = FastAPI()

	def getAppInstance(self):
		return self.__app