from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)

	with app.app_context():
		from .HOME.home import homeBP
		from .REGISTER.register import registerBP
		app.register_blueprint(homeBP)
		app.register_blueprint(registerBP)
		db.create_all()
		return app