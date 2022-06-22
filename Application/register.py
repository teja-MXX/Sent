from flask import Blueprint, request, render_template, flash
from werkzeug.utils import secure_filename
import datetime
import os
from flask import current_app as app
from Application.models import db, User, Images
from PIL import Image, ImageOps

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
		os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], uname))
		path = os.path.join(app.config['UPLOAD_FOLDER'], uname, uname+".jpg")
		DP.save(path)
		i = Image.open(path)
		width, height = i.size
		if(height > 150):
			perc = 150 / height
		else:
			perc = 235 / width

		height = int(height * perc)
		width = int(width * perc)
		resizedImage = i.resize((width, height))
		# Adding Black Border padding . . .
		if(height <= 150):
			# width padding	
			# print("Line 84")
			requiredPadding = int((235 - width) / 2)
			paddedImage = ImageOps.expand(resizedImage, (requiredPadding, 0))

		else:
			# height padding
			requiredPadding = int((150 - height) / 2)
			paddedImage = ImageOps.expand(resizedImage, (0, requiredPadding))
			# ADJUST HEIGHT ACCORDINGLY
		
		paddedImage.save(path)
		checkUname = User.query.filter_by(UserName = uname).first()
		print(checkUname)
		if checkUname:
			flash('Username Already Exists')
		elif pwd1 != pwd2:
			flash('Passwords don\'t match')
		else:
			newUser = User(fname, lname, uname, dob, pwd1)
			db.session.add(newUser)
			# f = open('./Application/static/profiles/Users','a')
			# f.write(newUser.FirstName + " " + newUser.LastName +"\n")
			# f.close()

			# f = open('./Application/static/profiles/UserNames','a')
			# f.write(newUser.UserName +"\n")
			# f.close()

			db.session.commit()
			flash('Account Created Successfully')
	return render_template('register.html')