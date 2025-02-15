import json
from pprint import pprint
from pymongo import MongoClient


def recipe_preprocessing(recipe):
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
        
    return recipes


data = recipe_preprocessing("recipe_test.json")
pprint(data)

client = MongoClient("mongodb+srv://cam:0HPmO2G3GVLNF8Hp@c-flat.t2z0j.mongodb.net")  # Use local MongoDB
db = client["SmartCart"]  # Database name
collection = db["recipes"]  # Collection name

# Inserting the data into the collection
result = collection.insert_many(data)