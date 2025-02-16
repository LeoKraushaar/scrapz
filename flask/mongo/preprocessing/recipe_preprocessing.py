import json
import os
from dotenv import load_dotenv
from pprint import pprint
from pymongo import MongoClient
#from mongo_manager import MongoManager
#from api.food_categories import food_categories

def recipe_preprocessing(recipe):
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['SmartCart'] # Database name
    collection = db['items'] # Collection name
    
    with open(recipe, "r") as file:
        data = json.load(file) # converts JSON to py dictionary

    recipes = []
    for hit in data["hits"]:  # Loop through each recipe entry
        recipe = hit["recipe"]  # Access the "recipe" dictionary inside each hit

        # Extract the relevant information from the recipe dictionary
        recipe = {
            "image" : recipe["image"],
            "label" : recipe["label"],
            "source" : recipe["source"],
            "url" : recipe["url"],
            "dietLabels" : recipe["dietLabels"],
            "healthLabels" : recipe["healthLabels"],
            "cautions" : recipe["cautions"],
            "ingredientLines" : recipe["ingredientLines"],
            # Go through the ingredients to ensure the dictionary is flattened
            "ingredients" : recipe["ingredients"],
            "calories" : recipe["calories"],
            "cuisineType" : recipe["cuisineType"],
            "mealType" : recipe["mealType"],
            # dishType might be useless, not sure atm
            "dishType" : recipe["dishType"],
            # Skip over nutrients and digest for now
        }
        
        recipes.append(recipe)
        
    try:
        # test_doc = {"test": "data"}
        # result = collection.insert_one(test_doc)
        # print("Inserted ID:", result.inserted_id)
        collection.insert_many(recipes)
        print("Added successfully!")
    except Exception as e:
        print(e)
    finally:
        client.close()
        
    return recipes


data = recipe_preprocessing("recipe_test.json")
#pprint(data)