import json
import os
import certifi
from dotenv import load_dotenv
from pprint import pprint
from pymongo import MongoClient

def fetchPantry() -> None:
    # PantryItems: an array of all the items in the user's pantry
    # Functionality: Fetches the data from the MongoDB database and returns the recipes that can be made with the pantry items
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart'] # Database name
    collection = db['useritems'] # Collection name
    
    documents = collection.find()

    pantryFood = []
    # Retreive all food from pantry (duplicates allowed)
    for document in documents:
        pantryFood.append(document["name"].strip().lower())
    
    client.close()
    
    ### Implement Later ###
        # If food is expired, auto remove document from DB
        
    return pantryFood