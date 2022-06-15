from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	FirstName = db.Column(db.String(15))
	LastName = db.Column(db.String(15))
	UserName = db.Column(db.String(10))
	DOB = db.Column(db.Date)
	Password = db.Column(db.String(50))
	socketId = db.Column(db.String(100))
	images = db.relationship('Images', backref='User')
	likedUsers = db.relationship('LikedUsers', backref='User')
	

	def __init__(self, fname, lname, uname, dob, pwd, sockID = None):
		self.FirstName = fname
		self.LastName = lname
		self.UserName = uname
		self.DOB = dob
		self.Password = pwd
		self.socketId = sockID

class Images(db.Model):
	__tablename__ = 'images'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	path = db.Column(db.String(500))
	likeCount = db.Column(db.Integer)
	likedUsers = db.relationship('LikedUsers', backref='Images')

	def __init__(self, path, user = None, likeCount = 0):
		self.User = user
		self.path = path
		self.likeCount = likeCount

class LikedUsers(db.Model):
	__tablename__ = 'likedUsers'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	image_id = db.Column(db.Integer, db.ForeignKey('images.id'))

	def __init__(self, user_id, image_id):
		self.user_id = user_id
		self.image_id = image_id







