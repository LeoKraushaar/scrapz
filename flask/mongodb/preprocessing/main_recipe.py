import json
from fetch_pantry import fetchPantry
from get_recipe import findRecipes
from recipe_preprocessing import recipePreprocessing

# Load the pantry items from the MongoDB database
pantryItems = fetchPantry()

# Load the recipes from the Edamam API
recipesArr = findRecipes(pantryItems)

# Preprocess the recipes
recipePreprocessing(json.dumps(recipesArr))