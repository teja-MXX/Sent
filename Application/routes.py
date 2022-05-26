from flask import current_app as app
from flask import render_template, request, flash
from .models import db, User

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		uname = request.form['username']
		pwd = request.form['password']
		User = User.query.filter_by(UserName = uname).first()
		if User:
			if pwd != User.Password:
				flash('Wrong Password')
			else:
				return render_template('home.html')
		else:
			flash('Username doesn\'t Exists')
	return render_template('login.html')


@app.route("/register", methods=['GET','POST'])
def register():
	if request.method == "POST":
		fname = request.form['fname']
		lname = request.form['lname']
		uname = request.form['uname']
		pwd1 = request.form['pwd1']
		pwd2 = request.form['pwd2']

		checkUname = User.query.filter_by(UserName = uname).first()
		print(checkUname)
		if checkUname:
			flash('Username Already Exists')
		elif pwd1 != pwd2:
			flash('Passwords don\'t match')
		else:
			newUser = User(fname, lname, uname, pwd1)
			db.session.add(newUser)
			db.session.commit()
			flash('Account Created Successfully')
	return render_template('register.html')
