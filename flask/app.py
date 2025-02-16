from flask import Flask, Blueprint, render_template
from mongodb.mongo_manager import MongoManager
from pantry import pantry_bp
from constants import *

app = Flask(__name__)
mongo = MongoManager(DB)


@app.route("/")
def home():
    return render_template(
        'index.html'
    )

# @app.route('/pantry')
# def pantry():
#     items = mongo.queryCollection(ITEMS)
#     return render_template(
#             'pantry.html',
#             n=len(items),
#             items=items
#         )

app.register_blueprint(pantry_bp)

@app.route('/recipes/results')
def getRecipe():
    recipes = mongo.queryCollection(RECIPES)

if __name__ == '__main__':
    app.run(debug=True)
