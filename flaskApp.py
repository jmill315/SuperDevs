# imports
import os
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_project_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# Bind SQLAlchemy db object to this Flask app
db.init-app(app)
# setup models
with app.app_context():
    db.create_all()

#test dictionaries and user
projects = {1: {'title': 'Create web page', 'text': 'Create a web page for client', 'date': '10-1-2020'},
               2: {},
               3: {}
               }
tasks = {1: {'title': 'Create Index HTML file', 'text': 'Create and code in HTML file called index', 'date': '10-1-2020'},
         2: {},
         3: {}
         }
a_user = {'name':'Bob', 'email':'mogli@uncc.edu'}


@app.route('/index')
def index():
    return render_template('index.html', user=a_user)

@app.route('/projects')
def get_projects():
    return render_template('projects.html', projects=projects, user=a_user)

@app.route('/projects/<project_id>')
def get_tasks():
    return render_template('tasks.html', user=a_user)

@app.route('/projects/newProject', methods=['Get', 'POST'])
def new_project():

    # check method used for request
    print('request method is', request.method)
    if request.method == 'POST':
        # get title data
        title = request.form['title']
        # get note data
        text = request.form['projectText']
        # create date stamp
        from datetime import date
        today = date.today()
        # format date mm/dd/yyyy
        today = today.strftime("%m-%d-%Y")
        # get the last ID used and increment by 1
        id = len(projects)+1
        # create new note entry
        projects[id] = {'title' : title, 'text' : text, 'date' : today}
        # ready to render response - redirect to projects listing
        return redirect(url_for('get_projects'))
    else:
        return render_template('newProject.html', user=a_user)

app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
#   http://127.0.0.1:5000/index
