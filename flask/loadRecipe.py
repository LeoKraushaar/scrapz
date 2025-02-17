from flask import Blueprint, render_template, request
from mongodb.mongo_manager import MongoManager
from constants import DB, RECIPES
import os
from dotenv import load_dotenv
import json
from mongodb.preprocessing.fetch_pantry import fetchPantry
from mongodb.preprocessing.get_recipe import findRecipes
from mongodb.preprocessing.recipe_preprocessing import recipePreprocessing
from pymongo import MongoClient
import certifi

# Create a blueprint for recipe-related routes
load_recipe_bp = Blueprint('load_recipe', __name__)

# MongoManager instance
mongo = MongoManager(DB)

@load_recipe_bp.route('/recipes/results', methods=['GET', 'POST'])
def get_recipe():
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart']
    collection = db['recipes']

    # Load the pantry items from the MongoDB database
    pantryItems = fetchPantry()

    # Get the filters from the form (if any)
    meal_type = request.form.get('meal_type', '')
    diet = request.form.get('diet', '')
    max_cook_time = request.form.get('max_cook_time', '')

    # Fetch recipes from Edamam API
    recipesArr = findRecipes(pantryItems, mealTypes=[meal_type], healthLabels=[diet], time=[max_cook_time])

    # Preprocess the recipes (adjust ingredients, etc.)
    recipePreprocessing(json.dumps(recipesArr))

    # Save the recipes to MongoDB or query them if already saved
    # recipes = mongo.queryCollection(RECIPES)
    recipes = collection.aggregate([
        {"$sort": {"availableIngredients": 1}},
    ])

    # Return the rendered recipe page with the recipes data
    return render_template('recipe.html', recipes=recipes)