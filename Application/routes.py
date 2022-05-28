from flask import current_app as app, session
from flask import render_template, request, flash, redirect
from .models import db, User
import datetime

@app.route("/", methods=['GET', 'POST'])
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


@app.route("/register", methods=['GET','POST'])
def register():
	if request.method == "POST":
		fname = request.form['fname']
		lname = request.form['lname']
		uname = request.form['uname']
		dob = request.form['dob'].split("-")
		#dob 1212-12-12
		dob = datetime.datetime(int(dob[0]), int(dob[1]), int(dob[2]))
		pwd1 = request.form['pwd1']
		pwd2 = request.form['pwd2']

		checkUname = User.query.filter_by(UserName = uname).first()
		print(checkUname)
		if checkUname:
			flash('Username Already Exists')
		elif pwd1 != pwd2:
			flash('Passwords don\'t match')
		else:
			newUser = User(fname, lname, uname, dob, pwd1)
			db.session.add(newUser)
			db.session.commit()
			flash('Account Created Successfully')
	return render_template('register.html')

@app.route("/logout")
def logout():
	session.pop('uname', None)
	session.pop('_flashes', None)
	return redirect('/')