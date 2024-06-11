from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    my_app = Flask(__name__)
    my_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.sqlite3'
    my_app.config['SECRET_KEY'] = 'random string'

    db.init_app(my_app)

    with my_app.app_context():
        from . import product
        db.create_all()

    return my_app
