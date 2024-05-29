# SQLAlchemy & Database

Branch: sqlalchemy

Summary: This branch introduces SQLAlchemy, an ORM for interacting with databases. You'll learn to set up a database, define database models, and perform CRUD operations.

Key Concepts:

    Setting up SQLAlchemy with Flask.
    Defining database models.
    Performing CRUD operations (Create, Read, Update, Delete).

Example : 
```sh
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}')"

@app.route('/add_user')
def add_user():
    new_user = User(username="NewUser")
    db.session.add(new_user)
    db.session.commit()
    return "User added!"

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
```

# Steps
1. install Flask-SQLAlchemy.
2. Define the User model and perform a simple add_user operation.

