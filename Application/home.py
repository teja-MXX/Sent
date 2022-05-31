from flask import current_app as app, session, jsonify
from flask import render_template, request, flash, redirect, flash
from flask import Blueprint
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




@app.route("/logout")
def logout():
	session.pop('uname', None)
	session.pop('_flashes', None)
	return redirect('/')