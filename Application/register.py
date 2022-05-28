from flask import Blueprint, request, render_template, flash
import datetime
from Application.models import db,User

registerBP = Blueprint('registerBP', __name__)

@registerBP.route("/register", methods=['GET','POST'])
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