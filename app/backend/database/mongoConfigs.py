import os
from dotenv import load_dotenv

load_dotenv()

mongoDbInfos = {
	"HOST": os.getenv('HOST'),
	"PORT": os.getenv('PORT'),
	"USERNAME": os.getenv('USERNAME'),
	"PASSWORD": os.getenv('PASSWORD'),
	"DBNAME": os.getenv('DBNAME')
}