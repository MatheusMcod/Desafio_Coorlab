from typing import Dict, List
import json

class TravelQuotes:
	def __init__(self, dbConnection) -> None:
		self.__collectionName = "TravelsQuotes"
		self.__dbConnection = dbConnection

	def readJsonFileAndProcess(self, filePath) -> List[Dict]:
			try:
				with open(filePath, 'r') as file:
					jsonData = json.load(file)
					if not isinstance(jsonData.get("transport"), list):
						raise ValueError("JSON file data is not a list")
					return jsonData
			except FileNotFoundError:
					print(f"The file '{filePath}' was not found.")
			except json.JSONDecodeError:
					print(f"Error decoding JSON file '{filePath}'.")
			except ValueError as e:
					print(e)
