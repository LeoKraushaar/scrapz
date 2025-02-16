import os
from dotenv import load_dotenv
import requests
import json
import time
from pprint import pprint
from mongodb.preprocessing.recipe_preprocessing import recipePreprocessing
from mongodb.preprocessing.fetch_pantry import fetchPantry

load_dotenv()
id = os.getenv('APP_ID')
api_key = os.getenv('API_KEY')

def findRecipes(query, mealTypes = None, dishTypes = None, cuisineTypes = None, dietLabels = None, healthLabels = None):
    # Assume the array holds item arrays, such that they represent the following:
    # [dietLabels, healthLabels, cautions, cuisineType, mealType, dishType]
    #### EXAMPLES ####
    # query: a str (required)***
    # dietLabels: [balanced, high-fiber, high-protein, low-carb, low-fat, low-sodium]
    # healthLabels: [sugar-conscious, vegetarian, peanut-free, tree-nut-free]
    # cautions: [nuts, treenuts]
    # cuisineType: [american, asian, italian, mexican]
    # mealType: [breakfast, lunch, dinner, snack]
    # dishType: [desserts, main-course, side-dish, appetizers]
    
    base_url = f"https://api.edamam.com/api/recipes/v2?type=public&"
    #"https://api.edamam.com/api/recipes/v2?type=public&"
    
    if query: # If non-empty arr, continue
        for q in query:
            # Edgecase: If the user input is empty (input blank), skip (IFF, there is no dropdown)
            if q.strip() == "":
                continue
            ### Logic of f"q={"-".join(q.strip().lower().split())}&" ###
                # q.strip() removes leading/trailing whitespaces
                # q.lower() converts the string to lowercase
                # q.split() splits the string into an array of words
                # "-".join() joins the array of words into a string with "-" as the separator (API formatted)
                # f"q={...}&" formats the string into the query format for the API
            base_url += f"q={"-".join(q.strip().lower().split())}&"
        
        # Add the app_id and app_key to the base_url after the query (format of the API req.)
        base_url += f"app_id={id}&"
        base_url += f"app_key={api_key}&"
    
    if mealTypes:
        for meal in mealTypes:
            if meal.strip() == "":
                continue
            base_url += f"mealType={"-".join(meal.strip().lower().split())}&"
    
    if dishTypes:
        for dish in dishTypes:
            if dish.strip() == "":
                continue
            base_url += f"dishType={"-".join(dish.strip().lower().split())}&"
    
    if cuisineTypes:
        for cuisine in cuisineTypes:
            if cuisine.strip() == "":
                continue
            base_url += f"cuisineType={"-".join(cuisine.strip().lower().split())}&"
    
    if dietLabels:
        for dietLabel in dietLabels:
            if dietLabel.strip() == "":
                continue
            base_url += f"diet={"-".join(dietLabel.strip().lower().split())}&"
            
    if healthLabels:
        for healthLabel in healthLabels:
            if healthLabel.strip() == "":
                continue
            base_url += f"health={"-".join(healthLabel.strip().lower().split())}&"
    
    ##### Unsure if this is the correct format for cautions (i.e., unsure if it's for dietary restrictions) #####
    # if excluded:
    #     for caution in excluded:
    #         if caution.strip() == "":
    #             continue
    #         base_url += f"excluded={"-".join(caution.strip().lower().split())}&"
    
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


# Call fetPantry to fetch all user items (food) available
#curInv = fetchPantry()

#### To be removed once Front End is implemented ####
# mealTypes = ["breakfast"]
# dishTypes = []
# cuisineTypes = []
# dietLabels = ["high protein"]
# healthLabels = []
#excluded = []

#recipesArr = findRecipes(curInv, mealTypes, dishTypes, cuisineTypes, dietLabels, healthLabels)

#recipePreprocessing(json.dumps(recipesArr)) # Convert to JSON string