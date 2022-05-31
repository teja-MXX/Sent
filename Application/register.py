from flask import Blueprint, request, render_template, flash
from werkzeug.utils import secure_filename
import datetime
import os
from flask import current_app as app
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
		DP = request.files['file']
		DP.save(os.path.join(app.config['UPLOAD_FOLDER'], uname))
		checkUname = User.query.filter_by(UserName = uname).first()
		print(checkUname)
		if checkUname:
			flash('Username Already Exists')
		elif pwd1 != pwd2:
			flash('Passwords don\'t match')
		else:
			newUser = User(fname, lname, uname, dob, pwd1)
			db.session.add(newUser)
			f = open('./Application/static/profiles/Users','a')
			f.write(newUser.FirstName + " " + newUser.LastName +"\n")
			f.close()

			f = open('./Application/static/profiles/UserNames','a')
			f.write(newUser.UserName +"\n")
			f.close()

			db.session.commit()
			flash('Account Created Successfully')
	return render_template('register.html')