from flask import current_app as app, session, jsonify
from flask import render_template, request, flash, redirect, flash
from flask import Blueprint
import os
from PIL import Image, ImageOps
from os.path import exists
import random
from Application.models import db, User, Images, LikedUsers
import datetime

homeBP = Blueprint('homeBP',__name__, 
			template_folder='templates', static_folder='static')

@homeBP.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		uname = request.form['username']
		pwd = request.form['password']
		user = User.query.filter_by(UserName = uname).first()

		if user:
			if pwd != user.Password:
				flash('Wrong Password')
			else:
				session['uname'] = uname
				dob = user.DOB.strftime('%d %B %Y')
				uploadedImages = Images.query.filter_by(user_id=user.id).all()
				imagePaths = []
				for images in uploadedImages:
					staticPath = images.path.split("\\")[7:]
					staticPath = "/".join(staticPath)
					imagePaths.append(staticPath)
				
				return render_template('home.html', userDetails = user, Birthday = dob, imagePaths=imagePaths, imageIds = '5')
		else:
			print('Hahaha')
			flash('Username doesn\'t Exists')
	if 'uname' in session:
		user = User.query.filter_by(UserName = session['uname']).first()
		dob = user.DOB.strftime('%d %B %Y')
		dpPath = "profiles/{}/{}.jpg'".format(user.UserName, user.UserName)
		uploadedImages = Images.query.filter_by(user_id=user.id).all()
		imagePaths = []
		for images in uploadedImages:
			staticPath = images.path.split("\\")[7:]
			staticPath = "/".join(staticPath)
			imagePaths.append(staticPath)

		return render_template('home.html', userDetails = user, Birthday = dob, DP = dpPath, imagePaths = imagePaths)
	else:

		return render_template('login.html')

@homeBP.route("/imageUpload", methods=["GET", "POST"])
def imageUPLOAD():
	if request.method == "POST":
		image = request.files['imag']
		f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'dbInfo.txt'))
		lastImageId = int(f.read())
		f.close()
		fileName = str(lastImageId + 1) + ".jpg"
		imagePath = os.path.join(app.config['UPLOAD_FOLDER'], session['uname'], fileName)
		image.save(imagePath)
		f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'dbInfo.txt'),'w')
		f.write(str(lastImageId + 1))
		f.close()
		addPadding(imagePath, "GALLERY")
		imageUser = User.query.filter_by(UserName = session['uname']).first()
		imageUpload = Images(imagePath, imageUser, 0)
		db.session.add(imageUpload)
		db.session.commit()

		return redirect("/")

@homeBP.route("/dpChange", methods=["POST"])
def dpChange():
	if request.method == "POST":
		DP = request.files['dp']
		path = os.path.join(app.config['UPLOAD_FOLDER'], session['uname'],session['uname']+".jpg")
		DP.save(path)
		# Resizing in Image
		addPadding(path, "DP")
		return redirect("/")


@homeBP.route("/dpRemove")
def dpRemove():
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], session['uname'],session['uname']+".jpg"))
	return redirect("/")


# FUNCTION FOR VIEWING YOUR OWN PROFILE PHOTOS IN NEW WINDOW
@homeBP.route("/imageShow/<string:imageFileName>")
def imageShowWindow(imageFileName):
	print("Image File Name - "+imageFileName)
	# GETTING IMAGE DETAILS BY ITS ID
	imageId = int(imageFileName.split(".")[0])
	imageQuery = Images.query.filter_by(id = imageId).first()
	imageUserQuery = User.query.filter_by(id = imageQuery.user_id).first()
	imageUser = imageUserQuery.FirstName + " " + imageUserQuery.LastName
	imgSrc = imageQuery.path.split("\\")
	imgSrc = "/".join(imgSrc[7:])
	imgLikes = imageQuery.likeCount

	# DISPLAYING FIRST USER WHO LIKED THE PHOTO -> w3eknd and 16 other 
	allLikedUsers = LikedUsers.query.filter_by(image_id = imageId).all()
	# CHECKING IF USER HAS LIKED SO THAT LIKE BUTTON IS FILLED
	likedPhoto = False
	userDetails = []
	if allLikedUsers:
		for likedUser in allLikedUsers:
			userFind = User.query.filter_by(id = likedUser.user_id).first()
			userDetails.append(userFind.UserName)
			if userFind.UserName == session['uname']:
				likedPhoto = True
				break
			
	if userDetails:
		return render_template("imageShow.html", path=imgSrc, user=imageUser, likes=imgLikes, details=userDetails[0], likedPhoto=likedPhoto)
	return render_template("imageShow.html", path=imgSrc, user=imageUser, likes=imgLikes, likedPhoto=likedPhoto)
	

# IMAGE EDIT
@homeBP.route("/imageShow/<string:imageFileName>/edit")
def editPhoto(imageFileName):
	print("Cool")
	imageId = int(imageFileName.split(".")[0])
	imageQuery = Images.query.filter_by(id = imageId).first()
	imageUserQuery = User.query.filter_by(id = imageQuery.user_id).first()
	imageUser = imageUserQuery.FirstName + " " + imageUserQuery.LastName
	imgSrc = imageQuery.path.split("\\")
	imgSrc = "/".join(imgSrc[7:])
	return render_template("imageShowEdit.html", path=imgSrc, user=imageUser)



# DELETING USER PHOTOS WHEN OPENED IN NEW WINDOW
@homeBP.route("/imageShow/<string:imageFileName>/delete")
def deletePhoto(imageFileName):
	imageId = int(imageFileName.split(".")[0])
	imageQuery = Images.query.filter_by(id = imageId).first()
	imagePath = imageQuery.path
	users = LikedUsers.query.filter_by(image_id = imageId).delete()
	db.session.delete(imageQuery)
	db.session.commit()
	os.remove(imagePath)
	return redirect("/")

# UPDATING LIKES
@homeBP.route("/imageShow/<string:imageFileName>/updateLikes")
def updateLikes(imageFileName):
	imageId = int(imageFileName.split(".")[0])
	imageQuery = Images.query.filter_by(id = imageId).first()
	user = User.query.filter_by(UserName = session['uname']).first()
	PhotoLiked = LikedUsers.query.filter_by(user_id = user.id , image_id = imageQuery.id).first()
	if(not PhotoLiked):
		imageQuery.likeCount += 1
		print(session['uname'])
		
		likedUser = LikedUsers(user.id, imageQuery.id)
		db.session.add(likedUser)
		db.session.add(imageQuery)
		db.session.commit()
	return redirect("/imageShow/" + imageFileName)



@app.route("/logout")
def logout():
	session.pop('uname', None)
	session.pop('_flashes', None)
	return redirect('/')

def addPadding(path, imageType):
	i = Image.open(path)
	width, height = i.size
	if imageType == "DP":
		if(height > 150):
			perc = 150 / height
		else:
			perc = 235 / width
		maxHeight = 150
		maxWidth = 235
	else:
		if(height > width or height == width):
			perc = 550 / height
		else:
			perc = 900 / width
		maxHeight = 550
		maxWidth = 900

	height = int(height * perc)
	width = int(width * perc)
	resizedImage = i.resize((width, height))
	# Adding Black Border padding . . .
	if(height <= maxHeight):
		# width padding	
		# print("Line 84")
		requiredPadding = int((maxWidth - width) / 2)
		paddedImage = ImageOps.expand(resizedImage, (requiredPadding, 0))

	else:
		# height padding
		requiredPadding = int((maxHeight - height) / 2)
		paddedImage = ImageOps.expand(resizedImage, (0, requiredPadding))
		# ADJUST HEIGHT ACCORDINGLY
	paddedImage.save(path)