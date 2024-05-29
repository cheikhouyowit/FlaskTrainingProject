from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}')"

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form['data']
        return f"Received: {data}"
    return '''
    <form method="POST">
        <input type="text" name="data">
        <input type="submit">
    </form>
    '''

@app.route('/add_user')
def add_user():
    new_user = User(username="NewUser")
    db.session.add(new_user)
    db.session.commit()
    return "User added!"

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
