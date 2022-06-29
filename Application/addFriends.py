from flask import Blueprint, render_template, session, request, redirect
from Application.models import db, User, Images, friendRequests, Friends

friendsBP = Blueprint('friendsBP', __name__)

@friendsBP.route("/addFriends", methods=["GET", "POST"])
def friends():
	print("YO MAN")
	# CHECKING IF USER GOT ANY FRIEND REQUESTS
	getUserId = User.query.filter_by(UserName = session['uname']).first().id
	getRequests = friendRequests.query.filter_by(to_id = getUserId).all()
	requestsFrom = []
	if getRequests:
		for requests in getRequests:
			getUser = User.query.filter_by(id = requests.from_id).first()
			requestsFrom.append(getUser.UserName)
		print(requestsFrom)
	user = User.query.filter_by(UserName = session['uname']).first()
	if user:
		usersList = User.query.filter(User.UserName != session['uname']).all()
		friends = []
		friendsDpPaths = {}
		for friend in usersList:
			alreadyFriend = Friends.query.filter_by(user_id = getUserId, friend_id = friend.id).first()
			if not alreadyFriend:
				friends.append(friend)
				pathh = "profiles/{}/{}.jpg".format(friend.UserName, friend.UserName)
				friendsDpPaths[friend.UserName] = pathh
		return render_template('friends.html', userDetails = user, friendAccounts = friends, path = friendsDpPaths, requests=requestsFrom)

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

@friendsBP.route("/addFriend/<string:fromm>/<string:too>")
def friendRequest(fromm, too):
	fromId = User.query.filter_by(UserName = fromm).first().id
	toId = User.query.filter_by(UserName = too).first().id
	requestSent = friendRequests.query.filter_by(from_id=fromId, to_id=toId).first()
	if not requestSent:
		print("Not sent")
		request = friendRequests(fromId, toId)
		db.session.add(request)
		db.session.commit()
	print("Successful")
	return redirect("/addFriends")

@friendsBP.route("/friendRequest/<string:fromm>/<string:too>/<string:response>")
def requestResponse(fromm, too, response):
	fromId = User.query.filter_by(UserName = fromm).first().id
	toId = User.query.filter_by(UserName = too).first().id
	if response == "Accept":
		fromFriend = Friends(fromId, toId)
		toFriend = Friends(toId, fromId)
		db.session.add(fromFriend)
		db.session.add(toFriend)
		db.session.commit()
		print("Request Accepted")
		print(fromId, toId)
	requestDeleteDB = friendRequests.query.filter_by(from_id=fromId, to_id=toId).first()
	db.session.delete(requestDeleteDB)
	db.session.commit()
	print("Succesfully 63")
	return redirect("/addFriends") 



