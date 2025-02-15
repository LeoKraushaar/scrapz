from flask import Flask, Blueprint, render_template
from mongo.mongo_manager import MongoManager
from constants import *

app = Flask(__name__)
mongo = MongoManager()

@app.route("/")
def home():
    return "<p>Welcome to SmartCart!</p>"

@app.route('/pantry')
def pantry():
    items = mongo.queryCollection(ITEMS)
    return render_template(
        'templates/pantry.html',
        n=len(items),
        
    )

