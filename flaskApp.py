# imports
import os
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Project as Project
from models import Task as Task
from models import User as User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_project_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# setup models
with app.app_context():
    db.create_all()


@app.route('/index')
def index():
    # get user from database
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
    return render_template('index.html', user=a_user)


@app.route('/projects')
def get_projects():
    # get user from database
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
    # get projects from database
    projects = db.session.query(Project).all()
    return render_template('projects.html', projects=projects, user=a_user)


@app.route('/projects/<project_id>')
def get_tasks(project_id):
    # get user from database
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
    # get project from database
    projects = db.session.query(Project).filter_by(id=project_id).one()
    # get tasks from database
    tasks = db.session.query(Project.tasks).filter_by(id=project_id).all()
    return render_template('tasks.html', projects=projects, tasks=tasks, user=a_user)


@app.route('/projects/newProject', methods=['GET', 'POST'])
def new_project():
    # check method used for request
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
        new_record = Project(title, text, today)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('get_projects'))
    else:
        # get user from database
        a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
        return render_template("newProject.html", user=a_user)


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
#   http://127.0.0.1:5000/index
