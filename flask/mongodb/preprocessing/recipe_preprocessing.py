import json
import os
import certifi
from dotenv import load_dotenv
from pprint import pprint
from pymongo import MongoClient
import inflect

def recipePreprocessing(recipe):
    # curInv: a list of the current inventory
    # recipe: a JSON object containing the recipe data

    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart'] # Database name
    collection = db['recipes'] # Collection name
    userCollection = db['useritems']

    data = json.loads(recipe) # converts JSON to py dictionary

    for hit in data:  # Loop through each recipe entry
        recipe = hit["recipe"]  # Access the "recipe" dictionary inside each hit
        
        # Extract the relevant information from the recipe dictionary
        #Edgecase for documents w/o these labels
        keys_to_check = ["image", "label", "source", "url", "healthLabels", "ingredientLines", "ingredients", "totalTime", "mealType"]
        
        # Check if all keys are present in the recipe
        if all(key in recipe for key in keys_to_check):
            updatedRecipe = {
                "image" : recipe["image"],
                "label" : recipe["label"],
                "source" : recipe["source"],
                "url" : recipe["url"],
                "healthLabels" : recipe["healthLabels"],
                "ingredientLines" : recipe["ingredientLines"],
                # Go through the ingredients to ensure the dictionary is flattened
                "allIngredients": [ingredient["food"] for ingredient in recipe["ingredients"]],
                "availableIngredients" : [],
                "missingIngredients" : [],
                "totalTime" : recipe["totalTime"],
                "mealType" : recipe["mealType"]
            }
            
            # Search for all ingredients and put them in their respecitce lists (missingIngredient, or availableIngredient)
            for doc in recipe["ingredients"]:
                result = userCollection.find_one({"foodId": doc["foodId"]})
                if result is None:
                    updatedRecipe["missingIngredients"].append(doc["food"])
                else:
                    updatedRecipe["availableIngredients"].append(doc["food"])
            
            try:
                collection.insert_one(updatedRecipe)
                print("Added Successfully")
            except Exception as e:
                print(e)
    
    client.close()
    return None