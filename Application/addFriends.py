from flask import Blueprint, render_template, session, request
from Application.models import db, User, Images

friendsBP = Blueprint('friendsBP', __name__)

@friendsBP.route("/addFriends", methods=["GET", "POST"])
def friends():
	print("YO MAN")
	user = User.query.filter_by(UserName = session['uname']).first()
	if user:
		
		friends = User.query.filter(User.UserName != session['uname']).all()
		print("FCK")
		print(friends)
		return render_template('friends.html', userDetails = user, friendAccounts = friends)

@friendsBP.route("/profile/<string:uname>")
def profileVisit(uname):
	user = User.query.filter_by(UserName = uname).first()
	dob = user.DOB.strftime('%d %B %Y')
	uploadedImages = Images.query.filter_by(user_id=user.id).all()
	imagePaths = []
	for images in uploadedImages:
		staticPath = images.path.split("\\")[7:]
		staticPath = "/".join(staticPath)
		imagePaths.append(staticPath)
	return render_template('home.html', userDetails = user, Birthday = dob, Identity = user.LastName, imagePaths=imagePaths)

