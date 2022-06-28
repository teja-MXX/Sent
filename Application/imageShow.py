from flask import Blueprint, redirect, session
from Application.models import db, User, Images, Comments, CommentLike
from datetime import datetime
from .home import imageShowWindow

imageShowBP = Blueprint('imageShowBP',__name__,
						template_folder='templates', static_folder='static')

@imageShowBP.route("/imageShow/<string:imageFileName>/comment/<string:userComment>")
def comment(imageFileName, userComment):
	commentedUser, comment = userComment.split(" : ")
	commentUserId = User.query.filter_by(UserName = commentedUser).first().id
	commentTime = datetime.now()
	parent_Id = None
	imageId = int(imageFileName.split(".")[0])
	
	commentInsert = Comments(comment, commentUserId, commentTime, parent_Id, imageId)
	db.session.add(commentInsert)
	db.session.commit()
	return imageShowWindow(imageFileName)

@imageShowBP.route("/imageShow/<string:imageFileName>/reply/<int:parentCommentId>/<string:userComment>")
def reply(imageFileName, parentCommentId, userComment):
	commentQuery = Comments.query.filter_by(id = parentCommentId).first()
	if commentQuery.parent_Id:
		parent_Id = commentQuery.parent_Id
	else:
		parent_Id = parentCommentId
	commentedUser, comment = userComment.split(" : ")
	replyTo = commentQuery.commentedUser
	replyTo = User.query.filter_by(id = replyTo).first().UserName
	replyTo = "@"+replyTo+" "
	comment = replyTo + comment
	commentUserId = User.query.filter_by(UserName = commentedUser).first().id
	commentTime = datetime.now()
	imageId = int(imageFileName.split(".")[0])
	
	commentInsert = Comments(comment, commentUserId, commentTime, parent_Id, imageId)
	db.session.add(commentInsert)
	db.session.commit()
	return imageShowWindow(imageFileName)

@imageShowBP.route("/commentLike/<string:imageId>/<string:commentId>")
def commentLikeUpdate(imageId, commentId):
	# CHECKING IF USER ALREADY LIKED
	likedUserId = User.query.filter_by(UserName = session['uname']).first().id
	commentId = int(commentId)
	foundUser = CommentLike.query.filter_by(comment_id=commentId, user_id=likedUserId).first()
	if not foundUser:
		print("yo")
		commentLike = CommentLike(commentId, likedUserId)
		db.session.add(commentLike)
		db.session.commit()
	return redirect("/imageShow/"+imageId)
	


