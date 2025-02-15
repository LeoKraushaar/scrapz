import json

def items_preprocessing(file):
    data = json.loads(file)
    all_items = data['parsed']
    individual_items = []
    for recipe in all_items:

    pass