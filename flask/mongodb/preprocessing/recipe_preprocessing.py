import json
import os
import certifi
from dotenv import load_dotenv
from pprint import pprint
from pymongo import MongoClient
#from mongo_manager import MongoManager
#from api.food_categories import food_categories

def recipePreprocessing(recipe):
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart'] # Database name
    collection = db['recipes'] # Collection name
    
    #with open(recipe, "r") as file:
        #recipe = file.read()
    data = json.loads(recipe) # converts JSON to py dictionary

    recipes = []
    for hit in data:  # Loop through each recipe entry
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
            "dishType" : recipe["dishType"]
            # Skip over nutrients and digest for now
        }
        
        recipes.append(recipe)
        
    try:
        # test_doc = {"test": "data"}
        # result = collection.insert_one(test_doc)
        # print("Inserted ID:", result.inserted_id)
        pprint(recipes)
        collection.insert_many(recipes)
        print("Added successfully!")
    except Exception as e:
        print(e)
    finally:
        client.close()
        
    return recipes


#data = recipePreprocessing("recipe_test.json")
#pprint(data)