from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	FirstName = db.Column(db.String(15))
	LastName = db.Column(db.String(15))
	UserName = db.Column(db.String(10))
	Password = db.Column(db.String(50))

	def __init__(self, fname, lname, uname, pwd):
		self.FirstName = fname
		self.LastName = lname
		self.UserName = uname
		self.Password = pwd


