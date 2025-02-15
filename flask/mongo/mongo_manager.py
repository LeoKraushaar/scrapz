from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint
import os

class MongoManager:

    def __init__(self, db_name:str):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[db_name]

    def getCollection(self, coll_name:str):
        return self.db[coll_name]

    def queryCollection(self, coll_name:str, proj={}, filt={}):
        coll = self.getCollection(coll_name)
        results = coll.find(filt, proj)
        return list(results)
    


if __name__ == '__main__':
    load_dotenv()
    mongo = MongoManager()