import json
import os
import certifi
from dotenv import load_dotenv
from pprint import pprint
from pymongo import MongoClient
from mongodb.preprocessing.fetch_pantry import fetchPantry
from mongodb.preprocessing.get_items import FindKnownAs
import inflect

def recipePreprocessing(recipe):
    # curInv: a list of the current inventory
    # recipe: a JSON object containing the recipe data

    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart'] # Database name
    collection = db['recipes'] # Collection name
    userCollection = db['useritems']

    # Clear the collection before adding new data
    collection.delete_many({})
    data = json.loads(recipe) # converts JSON to py dictionary
    p = inflect.engine()
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
                "availableIngredients" : set(),
                "missingIngredients" : set(),
                "totalTime" : recipe["totalTime"],
                "mealType" : recipe["mealType"]
            }
            
            # Search for all ingredients and put them in their respecitce lists (missingIngredient, or availableIngredient)
            # for doc in recipe["ingredients"]:
            #     result = userCollection.find_one({"foodId": doc["foodId"]})
            #     if result is None:
            #         updatedRecipe["missingIngredients"].append(doc["food"].title())
            #     else:
            #         updatedRecipe["availableIngredients"].append(doc["food"].title())
            
            pantry = fetchPantry()
            addedIngredients = []
            for food in pantry:
                normalized_food = food.lower() if p.singular_noun(food) == False else p.singular_noun(food).lower()
                for doc in recipe['ingredients']:
                    normalized_ingredients = doc["food"].lower() if p.singular_noun(doc["food"]) == False else p.singular_noun(doc["food"]).lower()
                    if normalized_food in normalized_ingredients:
                        updatedRecipe["availableIngredients"].add(food)
                        addedIngredients.append(normalized_ingredients)
                    elif normalized_food not in normalized_ingredients and normalized_ingredients in addedIngredients:
                        continue
                    else:
                        updatedRecipe["missingIngredients"].add(normalized_ingredients)
            
            updatedRecipe["availableIngredients"] = list(updatedRecipe["availableIngredients"])
            updatedRecipe["missingIngredients"] = list(updatedRecipe["missingIngredients"])
            try:
                collection.insert_one(updatedRecipe)
                #print("Added Successfully")
            except Exception as e:
                print(e)
    
    client.close()
    return None