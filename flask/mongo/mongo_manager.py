from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint
import os
from ..constants import *

class MongoManager:

    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[DB]

    def getCollection(self, coll_name:str):
        return self.db[coll_name]

    def queryCollection(self, coll_name:str):
        coll = self.getCollection(coll_name)
        return list(coll.find())

if __name__ == '__main__':
    print(os.getcwd())
    load_dotenv()
    mongo = MongoManager()