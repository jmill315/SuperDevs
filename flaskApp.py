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
from forms import RegisterForm
from forms import LoginForm
from forms import TaskForm
from flask import session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_project_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SE3155'
# Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# setup models
with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/index')
def index():
    # check if a user is saved in the session
    if session.get('user'):
        return  render_template('index.html', user=session['user'])
    return render_template('index.html')


@app.route('/projects')
def get_projects():
    # check if a user is saved in the session
    if session.get('user'):
        # get projects from database
        projects = db.session.query(Project).all()
        return render_template('projects.html', projects=projects, user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/projects/<project_id>')
def get_tasks(project_id):
    # check if a user is saved in the session
    if session.get('user'):
        # get project from database
        projects = db.session.query(Project).filter_by(id=project_id).one()
        # set up a taskform
        tasks = TaskForm()
        return render_template('tasks.html', projects=projects, user=session['user'], form=tasks)
    else:
        return redirect(url_for('login'))

@app.route('/projects/newProject', methods=['GET', 'POST'])
def new_project():
    # check if a user is saved in the session
    if session.get('user'):
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
            new_record = Project(title, text, today, session['user_id'])
            db.session.add(new_record)
            db.session.commit()
            return redirect(url_for('get_projects'))
        else:
            return render_template("newProject.html", user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/projects/newTask/<project_id>', methods=['POST'])
def new_task(project_id):
    # check if a user is saved in the session
    if session.get('user'):
        task_form = TaskForm()
        if task_form.validate_on_submit():
            task_title = request.form['task']
            new_record = Task(task_title, project_id, session['user'])
            db.session.add(new_record)
            db.session.commit()
        return redirect(url_for('get_tasks', project_id=project_id))
    else:
        return redirect(url_for('login'))


@app.route('/projects/edit/<project_id>', methods=['GET', 'POST'])
def update_project(project_id):
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['projectText']
        project = db.session.query(Project).filter_by(id=project_id).one()
        project.title = title
        project.text = text
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('get_projects'))
    else:
        a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
        my_project = db.session.query(Project).filter_by(id=project_id).one()
        return render_template('newProject.html', project=my_project, user=a_user)


@app.route('/projects/delete/<project_id>', methods=['POST'])
def delete_project(project_id):
    my_project = db.session.query(Project).filter_by(id=project_id).one()
    db.session.delete(my_project)
    db.session.commit()
    return render_template('projects.html')


# does not work and we can't figure out why
@app.route('/projects/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    #task = db.session.query(Task).filter_by(id=task_id).one()
    
    task = Task.query.filter(Task.id == task_id).first()
    db.session.delete(task)
    db.session.commit()
    return render_template('tasks.html', task=task_id)




app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
#   http://127.0.0.1:5000/index
