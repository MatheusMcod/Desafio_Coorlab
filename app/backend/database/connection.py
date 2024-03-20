from pymongo import MongoClient
from .mongoConfigs import mongoDbInfos

class DBConnectionHandler:
	def __init__(self) -> None:
		self.__connectionString = 'mongodb://{}:{}@{}:{}/authSource=admin'.format(
			mongoDbInfos["USERNAME"],
			mongoDbInfos["PASSWORD"],
			mongoDbInfos["HOST"],
			mongoDbInfos["PORT"]
		)

		self.__databaseName = mongoDbInfos["DBNAME"]
		self.__client = None
		self.__dbConnection = None

	def connectToDb(self):
		self.__client = MongoClient(self.__connectionString)
		self.__dbConnection = self.__client[self.__databaseName]

	def getDbConnection(self):
		return self.__dbConnection

	def getDbClient(self):
		return self.__client


