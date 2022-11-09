from database import db

class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    date = db.Column("date", db.String(50))
    def __abs__(self, title, date):
        self.title = title
        self.date = date
        self.task = self.Task()

class Task(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    date = db.Column("date", db.String(50))
    def __init__(self, title, date):
        self.title = title
        self.date = date

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    def __init__(self, name, email):
        self.name = name
        self.email = email
