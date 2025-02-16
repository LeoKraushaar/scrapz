import os
import datetime
import inflect
from dotenv import load_dotenv
from pymongo import MongoClient
from food_categories import food_categories

def IsOwned(foodId):
    '''
    Checks if the item is in user inventory.
    Returns true if yes, else false.
    '''
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['SmartCart']
    collection = db['useritems']
    if collection.find_one({"foodId": foodId}):
        return True
    else:
        return False


def ProcessItems(dict):
    '''
    Adds the processed item into db.
    '''
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['SmartCart']
    collection = db['useritems']

    food = dict['hints'][0]['food']
    item = {}
    item['foodId'] = food['foodId']
    item['name'] = food['label']
    item['category'] = 'Others'
    item['quantity'] = 0
    item['expiryDate'] = datetime.datetime.now()
    item['Carbohydrate(g)'] = food['nutrients']['CHOCDF']
    item['Energy(kcal)'] = food['nutrients']['ENERC_KCAL']
    item['Fat(g)'] = food['nutrients']['FAT']
    item['Fiber(g)'] = food['nutrients']['FIBTG']
    item['Protein(g)'] = food['nutrients']['PROCNT']
    
    p = inflect.engine() # Helps convert nouns into singular form
    if any(p.singular_noun(item['name'].lower()) in vegetable.lower() for vegetable in food_categories['vegetables']):
        item['category'] = 'vegetable'
    elif any(p.singular_noun(item['name'].lower()) in fruit.lower() for fruit in food_categories['fruits']):
        item['category'] = 'fruit'
    elif any(p.singular_noun(item['name'].lower()) in meat.lower() for meat in food_categories['meat']):
        item['category'] = 'meat'
    elif any(p.singular_noun(item['name'].lower()) in dairy.lower() for dairy in food_categories['dairy']):
        item['category'] = 'dairy'
    elif any(p.singular_noun(item['name'].lower()) in seafood.lower() for seafood in food_categories['seafood']):
        item['category'] = 'seafood'
    elif any(p.singular_noun(item['name'].lower()) in condiments.lower() for condiments in food_categories['condiments/ingredients']):
        item['category'] = 'condiments/ingredients'

    try:
        collection.insert_one(item)
        print("Added successfully!")
    except Exception as e:
        print(e)
    finally:
        client.close()