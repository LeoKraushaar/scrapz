from flask import Flask, render_template, request, redirect, url_for
from mongodb.mongo_manager import MongoManager
from constants import *
from datetime import datetime

app = Flask(__name__)
mongo = MongoManager(DB)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/pantry', methods=['GET', 'POST'])
def pantry():
    if request.method == 'POST':
        name = request.form['name']
        expiration_date = request.form['expiration_date']
        mongo.insertOne(ITEMS, {'name': name, 'expiration_date': expiration_date})
        return redirect(url_for('pantry'))
    
    items = mongo.queryCollection(ITEMS)
    for item in items:
        try:
            item['expiration_date'] = datetime.strptime(item['expiration_date'], '%Y-%m-%d').strftime('%B %d, %Y')
        except ValueError:
            item['expiration_date'] = 'Invalid date'
    return render_template('pantry.html', n=len(items), items=items)

@app.route('/recipes/results')
def getRecipe():
    recipes = mongo.queryCollection(RECIPES)
    return render_template('recipes_results.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)