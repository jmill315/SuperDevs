from database import db

class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(200))
    date = db.Column("date", db.String(50))
    tasks = db.relationship("Task", backref="project", cascade="all, delete-orphan", lazy=True)
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date


class Task(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    date = db.Column("date", db.String(50))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    def __init__(self, title, project_id):
        self.title = title
        self.project_id = project_id

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    def __init__(self, name, email):
        self.name = name
        self.email = email
