from flask import current_app as app, session, jsonify
from flask import render_template, request, flash, redirect, flash
from flask import Blueprint
import os
from PIL import Image
from os.path import exists
import random
from Application.models import db, User, Images
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
				return render_template('home.html', userDetails = user, Birthday = dob)
		else:
			print('Hahaha')
			flash('Username doesn\'t Exists')
	if 'uname' in session:
		user = User.query.filter_by(UserName = session['uname']).first()
		dob = user.DOB.strftime('%d %B %Y')
		dpPath = "profiles/{}/{}.jpg'".format(user.UserName, user.UserName)
		return render_template('home.html', userDetails = user, Birthday = dob, DP = dpPath)
	else:

		return render_template('login.html')

@homeBP.route("/imageUpload", methods=["GET", "POST"])
def imageUPLOAD():
	if request.method == "POST":
		image = request.files['imag']
		totalImages = len(Images.query.all())
		fileName = str(totalImages + 1) + ".jpg"
		imagePath = os.path.join(app.config['UPLOAD_FOLDER'], session['uname'], fileName)
		image.save(imagePath)

		i = Image.open(imagePath)
		width, height = i.size
		if(height > width or height == width):
			perc = 550 / height
		else:
			perc = 900 / width

		height = int(height * perc)
		width = int(width * perc)
		resizedImage = i.resize((width, height))
		resizedImage.save(imagePath)
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
		i = Image.open(path)
		width, height = i.size
		if(height > width or height == width):
			perc = 540 / height
		else:
			perc = 850 / width

		height = int(height * perc)
		width = int(width * perc)
		resizedImage = i.resize((width, height))
		resizedImage.save(path)
		return redirect("/")


@homeBP.route("/dpRemove")
def dpRemove():
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], session['uname'],session['uname']+".jpg"))
	return redirect("/")


# FUNCTION FOR VIEWING YOUR OWN PROFILE PHOTOS IN NEW WINDOW
@homeBP.route("/imageShow/<string:imageFileName>")
def imageShowWindow(imageFileName):
	print("Image File Name - "+imageFileName)
	imageId = int(imageFileName.split(".")[0])
	imgSrc = Images.query.filter_by(id = imageId).first().path.split("\\")
	imgSrc = "/".join(imgSrc[7:])
	return render_template("imageShow.html", path=imgSrc)
	# return redirect("/dpRemove")


@app.route("/logout")
def logout():
	session.pop('uname', None)
	session.pop('_flashes', None)
	return redirect('/')