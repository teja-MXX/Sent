from flask import Blueprint, redirect
from Application.models import db, User, Images, Comments
from datetime import datetime
from .home import imageShowWindow

imageShowBP = Blueprint('imageShowBP',__name__,
						template_folder='templates', static_folder='static')

@imageShowBP.route("/imageShow/<string:imageFileName>/comment/<string:userComment>")
def comment(imageFileName, userComment):
	commentedUser, comment = userComment.split(" : ")
	print(commentedUser, comment)
	commentUserId = User.query.filter_by(UserName = commentedUser).first().id
	commentTime = datetime.now()
	parent_Id = None
	imageId = int(imageFileName.split(".")[0])
	print("ImageID - "+str(imageId))
	
	commentInsert = Comments(comment, commentUserId, commentTime, parent_Id, imageId)
	db.session.add(commentInsert)
	db.session.commit()
	print("Haha")
	return imageShowWindow(imageFileName)