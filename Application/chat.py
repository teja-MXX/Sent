from flask import current_app as app
from flask import Blueprint, render_template, session
from Application.models import db, User
import datetime

chatBP = Blueprint('chatBP', __name__)

@chatBP.route("/chat")
def chat():
	details = User.query.filter_by(UserName = session['uname']).first()
	if details:
		return render_template('chat.html', userDetails = details)