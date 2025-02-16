import os
from dotenv import load_dotenv
import requests

load_dotenv()
OK =  200

id = os.getenv('API_USERNAME')
api_key = os.getenv('API_KEY')

def FindItems(name=None, upc=None):
    '''
    Finds the food item on Edamam API.
    Returns a dictionary, if found on API, else 1
    '''
    if name:
        endpoint = f"https://api.edamam.com/api/food-database/v2/parser?app_id={id}&app_key={api_key}&ingr={name}&nutrition-type=cooking"
    if upc:
        endpoint = f"https://api.edamam.com/api/food-database/v2/parser?app_id={id}&app_key={api_key}&upc={upc}&nutrition-type=cooking"
    
    response = requests.get(endpoint)
    if response.status_code == OK:
        if len(response.json()['hints']) > 0:
            return response.json()
        else:
            return 1
    else:
        print(response)
        print('Error')


