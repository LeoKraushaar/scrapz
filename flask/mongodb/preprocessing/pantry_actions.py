import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

def openClient():
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart']
    collection = db['useritems']
    return client, collection

def closeClient(client: MongoClient):
    client.close()

def update_item(name, newQuantity=None, newDate=None):
    client, collection = openClient()
    update_fields = {}
    if newQuantity is not None:
        update_fields["quantity"] = newQuantity
    if newDate is not None:
        update_fields["expiryDate"] = newDate
    if update_fields:
        collection.update_one(
            {"name": name},
            {"$set": update_fields}
        )
    closeClient(client)


def delete_item(name):
    client, collection = openClient()
    collection.delete_one({'name': name})
    closeClient(client)