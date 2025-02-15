from flask import Flask, Blueprint, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to SmartCart!</p>"

@app.route('/pantry')
def pantry():
    return "<p>This is your pantry.</p"

