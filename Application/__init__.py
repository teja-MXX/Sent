from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()

def init_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)
	with app.app_context():
		from .home import homeBP
		from .chat import chatBP
		from .register import registerBP
		from .addFriends import friendsBP
		app.register_blueprint(chatBP)
		app.register_blueprint(homeBP)
		app.register_blueprint(registerBP)
		app.register_blueprint(friendsBP)
		db.create_all()
		return app