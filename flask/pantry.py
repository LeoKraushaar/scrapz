import os
from flask import Blueprint, render_template, request, redirect, url_for
from mongodb.preprocessing.get_items import FindItems
from mongodb.preprocessing.items_preprocessing import ProcessUnknownItems, ProcessItems
from pymongo import MongoClient
from dotenv import load_dotenv

# Create a blueprint for the pantry route
pantry_bp = Blueprint('pantry', __name__)

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
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['SmartCart']
    collection = db['useritems']

    # Fetch pantry items from the database
    pantry_items = collection.find({}, {'_id': 0, 'name': 1, 'category': 1, 'quantity': 1, 'expiryDate': 1, 'image': 1})
    pantry_items = list(pantry_items)

    client.close()

    # Render the template and pass pantry items
    return render_template('pantry.html', pantry_items=pantry_items)