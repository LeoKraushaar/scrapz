import json
import os
import certifi
from dotenv import load_dotenv
from pprint import pprint
from pymongo import MongoClient

def recipePreprocessing(curInv, recipe):
    # curInv: a list of the current inventory
    # recipe: a JSON object containing the recipe data

    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart'] # Database name
    collection = db['recipes'] # Collection name

    data = json.loads(recipe) # converts JSON to py dictionary

    for hit in data:  # Loop through each recipe entry
        recipe = hit["recipe"]  # Access the "recipe" dictionary inside each hit
        
        # Extract the relevant information from the recipe dictionary
        #Edgecase for documents w/o these labels
        keys_to_check = ["image", "label", "source", "url", "dietLabels", "healthLabels", "ingredientLines", "ingredients", "calories", "cuisineType", "mealType", "dishType"]
        if all(key in recipe for key in keys_to_check):
            recipe = {
                "image" : recipe["image"],
                "label" : recipe["label"],
                "source" : recipe["source"],
                "url" : recipe["url"],
                "dietLabels" : recipe["dietLabels"],
                "healthLabels" : recipe["healthLabels"],
                "ingredientLines" : recipe["ingredientLines"],
                # Go through the ingredients to ensure the dictionary is flattened
                "allIngredients": [ingredient["food"] for ingredient in recipe["ingredients"]],
                "availableIngredients" : [ingredient for ingredient in recipe["ingredients"] if ingredient["food"].strip().lower() in curInv],
                "missingIngredients" : [ingredient for ingredient in recipe["ingredients"] if ingredient["food"].strip().lower() not in curInv],
                "calories" : recipe["calories"],
                "cuisineType" : recipe["cuisineType"],
                "mealType" : recipe["mealType"],
                # dishType might be useless, not sure atm
                "dishType" : recipe["dishType"]
                # Skip over nutrients and digest for now
            }
            
            try:
                collection.insert_one(recipe)
                print("Added Successfully")
            except Exception as e:
                print(e)
    
    client.close()
    return None