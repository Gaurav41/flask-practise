from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
    
class Student(db.model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=False,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)
    date_created = db.Column(db.DateTime, auto_now_add=True)

