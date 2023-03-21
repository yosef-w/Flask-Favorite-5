from app import app
from flask import render_template

@app.route('/')
def hello():
    return('Welcome to my favorites')

@app.route('/favorites')
def favorites():
    return render_template('index.html')