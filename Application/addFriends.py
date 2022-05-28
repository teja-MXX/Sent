from flask import Blueprint, render_template, session
from Application.models import db, User

friendsBP = Blueprint('friendsBP', __name__)

@friendsBP.route("/addFriends")
def friends():
	user = User.query.filter_by(UserName = session['uname']).first()
	if user:
		return render_template('friends.html', userDetails = user)