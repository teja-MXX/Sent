from flask import current_app as app, session, jsonify
from flask import render_template, request, flash, redirect, flash
from flask import Blueprint
import os
from os.path import exists
import random
from Application.models import db, User
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
		return render_template('home.html', userDetails = user, Birthday = dob)
	else:

		return render_template('login.html')

@homeBP.route("/imageUpload", methods=["GET", "POST"])
def imageUPLOAD():
	if request.method == "POST":
		image = request.files['imag']
		fileName = str(random.randint(1,1000000000)) + ".jpg"
		while(exists(os.path.join(app.config['UPLOAD_FOLDER'], session['uname'], fileName))):
			fileName = str(random.randint(1,1000000000)) + ".jpg"
		image.save(os.path.join(app.config['UPLOAD_FOLDER'], session['uname'], fileName))
		return redirect("/")

@homeBP.route("/dpChange", methods=["POST"])
def dpChange():
	if request.method == "POST":
		DP = request.files['dp']
		DP.save(os.path.join(app.config['UPLOAD_FOLDER'], session['uname'],session['uname']+".jpg"))
		return redirect("/")


@homeBP.route("/dpRemove")
def dpRemove():
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], session['uname'],session['uname']+".jpg"))
	return redirect("/")

@app.route("/logout")
def logout():
	session.pop('uname', None)
	session.pop('_flashes', None)
	return redirect('/')