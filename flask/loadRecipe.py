from flask import Blueprint, render_template, request
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

@load_recipe_bp.route('/recipes/results', methods=['GET', 'POST'])
def get_recipe():
    # Load the pantry items from the MongoDB database
    pantryItems = fetchPantry()

    # Get the filters from the form (if any)
    meal_type = request.form.get('meal_type', '')
    diet = request.form.get('diet', '')
    max_cook_time = request.form.get('max_cook_time', '')

    # Fetch recipes from Edamam API
    recipesArr = findRecipes(pantryItems, list(meal_type), list(diet), list(max_cook_time))

    # Preprocess the recipes
    recipePreprocessing(pantryItems, json.dumps(recipesArr))
    
    # Adjust the template and context as needed
    recipes = mongo.queryCollection(RECIPES)

    # Return the rendered recipe page with the recipes data
    return render_template('recipe.html', recipes=recipes)
