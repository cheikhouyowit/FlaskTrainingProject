# Forms

Branch: forms

Summary: This branch covers handling forms in Flask, allowing you to collect and process user inputs. You'll learn to manage form submissions via GET and POST methods.

Key Concepts:

    Creating HTML forms to collect user data.
    Processing form data in Flask views using the request object.
    Using GET and POST methods.

Example : app.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

if __name__ == "__main__":
    app.run(debug=True)
