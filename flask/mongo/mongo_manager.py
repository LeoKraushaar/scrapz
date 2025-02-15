from pymongo import MongoClient
from dotenv import load_dotenv
import os
from constants import *

class MongoManager:

    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[DB]
        
    def queryCollection(self, collection):
        return list(self.db[collection])

if __name__ == '__main__':
    load_dotenv()
    mongo = MongoManager()