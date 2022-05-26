from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)

	with app.app_context():
		from . import routes
		db.create_all()
		return app