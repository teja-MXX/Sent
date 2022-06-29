from flask import current_app as app
from flask import Blueprint, render_template, session
from Application.models import db, User
import datetime
import json

chatBP = Blueprint('chatBP', __name__)

@chatBP.route("/chat")
def chat():
	details = User.query.filter_by(UserName = session['uname']).first()
	if details:
		return render_template('chat.html', userDetails = details)

@chatBP.route("/chat/<string:searchInput>")
def searchResults(searchInput):
	details = User.query.filter_by(UserName = session['uname']).first()
	searchInput = searchInput.split(" ")
	if len(searchInput) == 2:
		userSearch = User.query.filter(User.FirstName == searchInput[0],User.LastName == searchInput[1]).all()
		if not userSearch:
			userSearch = User.query.filter((User.FirstName.like(searchInput[0])) | (User.LastName.like(searchInput[1])) | (User.FirstName.like(searchInput[1])) | (User.LastName.like(searchInput[0])))
		users = {}
		for user in userSearch:
			if user.UserName == session['uname']:
				continue
			users[user.UserName] = {"FirstName": user.FirstName ,
									"LastName" : user.LastName ,
									"UserName" : user.UserName	    }
		jsonData = json.dumps(users)
		return jsonData
		
	else:
		value = "%{}%".format(searchInput[0])
		userSearch = User.query.filter(User.UserName.like(value) | User.FirstName.like(value) | User.LastName.like(value) ).all()
		if userSearch:
			users = {}
			for user in userSearch:
				if user.UserName == session['uname']:
					continue
				users[user.UserName] = {"FirstName": user.FirstName ,
										"LastName" : user.LastName ,
										"UserName" : user.UserName }
			jsonData = json.dumps(users)
			return jsonData

			