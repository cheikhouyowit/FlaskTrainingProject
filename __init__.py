
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
    app.config['SECRET_KEY'] = "random string"
    app.secret_key = 'any random string'

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app

