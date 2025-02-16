import os
from dotenv import load_dotenv
import requests
from food_categories import food_categories
from items_preprocessing import items_preprocessing
import json
import time

load_dotenv()
OK =  200

id = os.getenv('API_USERNAME')
api_key = os.getenv('API_KEY')

calls = 0
for key, values in food_categories.items():
    for item in values:
        print(item)
        item = item.replace(' ', '%20')
        endpoint = f"https://api.edamam.com/api/food-database/v2/parser?app_id={id}&app_key={api_key}&ingr={item}&nutrition-type=cooking"
        if calls >= 8:
            time.sleep(60)
            calls = 0
        response = requests.get(endpoint)
        if response.status_code == OK:
            if len(response.json()) > 0:
                json_file_path = 'response.json' 
                with open(json_file_path, 'w') as f:
                    json.dump(response.json(), f)
                items_preprocessing(json_file_path, item)
            calls += 1
        else:
            print(response)
            print(f"Error: {response.status_code}")