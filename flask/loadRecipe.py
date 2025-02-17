# loadRecipe.py
from flask import Blueprint, render_template
from mongodb.mongo_manager import MongoManager
from constants import DB, RECIPES
import json
from mongodb.preprocessing.fetch_pantry import fetchPantry
from mongodb.preprocessing.get_recipe import findRecipes
from mongodb.preprocessing.recipe_preprocessing import recipePreprocessing

# Create a blueprint for recipe-related routes
load_recipe_bp = Blueprint('load_recipe', __name__)

# MongoManager instance
mongo = MongoManager(DB)

@load_recipe_bp.route('/recipes/results')
def get_recipe():
    # Load the pantry items from the MongoDB database
    pantryItems = fetchPantry()

    # Load the recipes from the Edamam API
    recipesArr = findRecipes(pantryItems)

    # Preprocess the recipes
    recipePreprocessing(pantryItems, json.dumps(recipesArr))
    
    # Adjust the template and context as needed
    recipes = mongo.queryCollection(RECIPES)
    return render_template('recipe.html', recipes=recipes)