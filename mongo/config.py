import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CONNECTION = os.getenv("MONGO_URI")
    DB = os.getenv("DB_NAME")