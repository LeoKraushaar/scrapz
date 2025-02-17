import os
from dotenv import load_dotenv
import requests
import json
import time
from pprint import pprint
# from mongodb.preprocessing.recipe_preprocessing import recipePreprocessing
# from mongodb.preprocessing.fetch_pantry import fetchPantry

load_dotenv()
id = os.getenv('APP_ID_C')
api_key = os.getenv('API_KEY_C')

def findRecipes(query, mealTypes = None, healthLabels = None, time = None):
    # Assume the array holds item arrays, such that they represent the following:
    # [dietLabels, healthLabels, cautions, cuisineType, mealType, dishType]
    #### EXAMPLES ####
    # query: a str (required)***
    # mealType: [breakfast, lunch, dinner, snack]
    # healthLabels: [sugar-conscious, vegetarian, peanut-free, tree-nut-free]
    # time: [5-15 (RANGE: MIN-MAX), 15+ (MIN), 30 (MAX)]
    
    base_url = f"https://api.edamam.com/api/recipes/v2?type=public"
    # "https://api.edamam.com/api/recipes/v2?type=public&"
    
    if query: # If non-empty arr, continue
        base_url += "&q="

        for i in range(len(query)):
            if query[i].strip() == "":
                continue
            if i == 0:
                base_url += f"{query[i].replace(' ', '%20')}"
            else:
                base_url += f"%20or%20{query[i].replace(' ', '%20')}"
        
        # Add the app_id and app_key to the base_url after the query (format of the API req.)
        base_url += f"&app_id={id}"
        base_url += f"&app_key={api_key}"
    
    if mealTypes:
        if mealTypes[0] != "":
            base_url += f"&mealType={mealTypes[0]}"
            
    if healthLabels:
        if healthLabels[0] != "":
            base_url += f"&health={healthLabels[0]}"
    
    # time = ["num"] then convert to range format (0-num)
    if time and time[0].strip() != "":
        if (time[0].strip() != "") and (int(time[0].strip()) > 0):
            base_url += f"&time={int(time[0].strip())}"

    # WORKS: test
    #response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q=chicken&app_id=e02cd94b&app_key=f4a12877af8d3e2fad24f7152087dd77&diet=balanced&diet=high-fiber&cuisineType=Nordic&mealType=Breakfast&dishType=Soup&excluded=nuts&excluded=tree-nuts")
    response = requests.get(base_url)
    
    # Testing response and correctness of the base_url
    print(response)
    print(base_url)
    
    # If success API call
    if response.status_code == 200:
        data = response.json()
        return data["hits"]
    else:   #Error
        print(f"Error: {response.status_code} - {response.text}")
        return None