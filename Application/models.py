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
	commentLikedUsers = db.relationship('CommentLike', backref='User')

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

class Comments(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer,primary_key=True)
	comment = db.Column(db.String(1000))
	commentedUser = db.Column(db.Integer)
	commentTime = db.Column(db.DateTime)
	parent_Id = db.Column(db.Integer)
	image_Id = db.Column(db.Integer)
	likedComment = db.relationship('CommentLike', backref='Comments')


	def __init__(self, comment, commentedUser, 	commentTime, parentId, imageId, userId=None):
		self.comment = comment
		self.commentedUser = commentedUser
		self.commentTime = commentTime
		self.parent_Id = parentId
		self.image_Id = imageId

class CommentLike(db.Model):
	__tablename__ = 'commentLike'
	id = db.Column(db.Integer, primary_key=True)
	comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, commentId, userId):
		self.comment_id = commentId
		self.user_id = userId

class Messages(db.Model):
	__tablename__ = 'messages'
	id = db.Column(db.Integer, primary_key=True)
	from_id = db.Column(db.Integer)
	to_id = db.Column(db.Integer)
	message = db.Column(db.String(1000))
	time = db.Column(db.DateTime)

	def __init__(self, fromId, toId, msg, time):
		self.from_id = fromId
		self.to_id = toId
		self.message = msg
		self.time = time

class friendRequests(db.Model):
	__tablename__ = 'friendRequests'
	id = db.Column(db.Integer, primary_key=True)
	from_id = db.Column(db.Integer)
	to_id = db.Column(db.Integer)

	def __init__(self, fromId, toId):
		self.from_id = fromId
		self.to_id = toId

class Friends(db.Model):
	__tablename__ = 'friends'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	friend_id = db.Column(db.Integer)

	def __init__(self, userId, friendId):
		self.user_id = userId
		self.friend_id = friendId












