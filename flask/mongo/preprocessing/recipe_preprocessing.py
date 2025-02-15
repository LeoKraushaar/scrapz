import json
import pprint

def recipe_preprocessing(recipe):
    with open(recipe, 'r') as file:
        recipe = file.read()
    
    recipe = json.loads(recipe)
    
    
    
    return recipe


data = recipe_preprocessing("recipe_test.json")
pprint.pprint(data)
