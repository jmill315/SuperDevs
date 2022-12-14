from database import db
import datetime

class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(200))
    date = db.Column("date", db.String(50))
    counter = db.Column("counter", db.Integer)
    image = db.Column("image", db.String(200, nullable=True))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    tasks = db.relationship("Task", backref="project", cascade="all, delete-orphan", lazy=True)

    def __init__(self, title, text, image, date, counter, user_id):
        self.title = title
        self.text = text
        self.image = image
        self.date = date
        self.counter = counter
        self.user_id = user_id


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, title, project_id, user_id):
        self.title = title

        self.project_id = project_id
        self.user_id = user_id

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    projects = db.relationship("Project", backref="user", lazy=True)
    tasks = db.relationship("Task", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()
