from Application import init_app
from Application.models import db, User
from flask_socketio import SocketIO, emit
from flask import session
import datetime

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
	print(data)

	data["time"] = datetime.datetime.now()
	toUser = User.query.filter_by(UserName = data['to']).first()
	fromUser = User.query.filter_by(UserName = data['from']).first()
	msgg = Messages(toUser, fromUser, data['time'], data['msg'])
	db.session.add(msgg)
	db.session.commit()
	print(data)
	socket.emit('msgFromPythonJs', data)


if __name__ == "__main__":
	socket.run(app, debug=True, host='0.0.0.0', port=9000)
