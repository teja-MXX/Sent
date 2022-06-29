from Application import init_app
from Application.models import db, User, Messages
from flask_socketio import SocketIO, emit
from flask import session
from datetime import datetime

app = init_app()
socket = SocketIO(app)


@socket.on('socketidFromJsPython')
def updateUserSocketID(sockData):
	print(sockData)
	user = User.query.filter_by(UserName = session['uname']).first()
	user.socketId = sockData['sockID']
	db.session.add(user)
	db.session.commit()
	user1 = User.query.filter_by(UserName = session['uname']).first()
	print(user1.socketId)

@socket.on('msgFromJsPython')
def msg(data):
	fromId = User.query.filter_by(UserName = data['from']).first()
	toId = User.query.filter_by(UserName = data['to']).first()
	mesasge = data['msg']
	time = datetime.now()
	
	socket.emit('msgFromPythonJs', data)


if __name__ == "__main__":
	socket.run(app, debug=True, host='0.0.0.0', port=9000)
