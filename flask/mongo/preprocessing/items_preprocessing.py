import os
from dotenv import load_dotenv
import json
from pymongo import MongoClient
from food_categories import food_categories

def items_preprocessing(file, name):
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['SmartCart']
    collection = db['items']

    with open(file, 'r') as file:
        food = file.read()
    data = json.loads(food)
    all_items = data['hints']
    individual_items = []
    for item in all_items:
        individual_item = item['food']
        individual_item['quantity_owned'] = 0
        individual_item['expiry date'] = 'MM-DD-YYYY'
        if name in food_categories['vegetables']:
            individual_item['category'] = 'vegetable'
        elif name in food_categories['fruits']:
            individual_item['category'] = 'fruit'
        elif name in food_categories['meat']:
            individual_item['category'] = 'meat'
        elif name in food_categories['dairy']:
            individual_item['category'] = 'dairy'
        elif name in food_categories['seafood']:
            individual_item['category'] = 'seafood'
        individual_items.append(individual_item)

    try:
        collection.insert_many(individual_items, ordered=False)
        print("Added successfully!")
    except Exception as e:
        print(e)
    finally:
        client.close()