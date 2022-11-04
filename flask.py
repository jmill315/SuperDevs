# imports
import os
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/projects')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')
