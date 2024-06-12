from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from my_app import app
from my_app import manager



a

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app) #//
manager.run()

app.run(debug=True)