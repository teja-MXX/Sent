from flask import Blueprint, render_template, session, request
from Application.models import db, User

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