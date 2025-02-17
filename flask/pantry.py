import os
import json
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from mongodb.mongo_manager import MongoManager
from constants import DB, RECIPES
from mongodb.preprocessing.get_items import FindItems
from mongodb.preprocessing.items_preprocessing import ProcessUnknownItems, ProcessItems
from mongodb.preprocessing.pantry_actions import update_item, delete_item
from mongodb.preprocessing.fetch_pantry import fetchPantry
from mongodb.preprocessing.get_recipe import findRecipes
from mongodb.preprocessing.recipe_preprocessing import recipePreprocessing
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi

# Create a blueprint for the pantry route
pantry_bp = Blueprint('pantry', __name__)
mongo = MongoManager(DB)

@pantry_bp.route('/pantry', methods=['GET', 'POST'])
def pantry():
    if request.method == 'POST':
        item_name = request.form['name']
        quantity = request.form['quantity'] # may delete it
        expiry_date = request.form['expiry_date']

        found_item = FindItems(item_name)

        if found_item == 1:  # Item not found
            ProcessUnknownItems(item_name, quantity, expiry_date)
        elif isinstance(found_item, dict):
            ProcessItems(found_item, quantity, expiry_date)

        # Redirect to the pantry page after processing
        # return redirect(url_for('pantry.view_pantry'))

    # return render_template('pantry.html')  # Render the form for the user
    return redirect(url_for('pantry.view_pantry'))

@pantry_bp.route('/pantry/view')
def view_pantry():
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client['SmartCart']
    collection = db['useritems']

    # Fetch pantry items from the database
    pantry_items = collection.aggregate([
        {"$sort": {"expiryDate": 1}},
        {"$project": {"_id": 0, "name": 1, "category": 1, "quantity": 1, "expiryDate": 1, "image": 1}}
    ])
    pantry_items = list(pantry_items)

    client.close()

    # Render the template and pass pantry items
    return render_template('pantry.html', pantry_items=pantry_items)

@pantry_bp.route('/pantry/recipes')
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

@pantry_bp.route('/pantry/update/<item_name>', methods=['POST'])
def update_pantry_item(item_name):
    new_quantity = request.form.get('quantity')
    new_expiry_date = request.form.get('expiry_date')

    # If no new values are provided, don't update
    if not new_quantity and not new_expiry_date:
        return redirect(url_for('pantry.view_pantry'))
    elif new_quantity == '':
        update_item(item_name, newQuantity=None, newDate=new_expiry_date)
    elif new_expiry_date == '':
        update_item(item_name, newQuantity=new_quantity, newDate=None)
    else:
        # Update item
        update_item(item_name, newQuantity=new_quantity, newDate=new_expiry_date)
    
    return redirect(url_for('pantry.view_pantry'))

# Route to delete an item
@pantry_bp.route('/pantry/delete/<item_name>', methods=['POST'])
def delete_pantry_item(item_name):
    # Delete item
    delete_item(item_name)
    
    return redirect(url_for('pantry.view_pantry'))


@pantry_bp.route('/recipe')
def recipe():
    # Your logic to fetch recipe data
    return render_template('recipe.html')