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
    return render_template('projects.html')

@app.route('/projects/<project_id>')
def index():
    return render_template('tasks.html')



app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
