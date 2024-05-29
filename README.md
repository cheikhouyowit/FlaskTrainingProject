Branch: basic-routing

Summary: This branch introduces the basic concepts of routing in Flask. Routing is the mechanism by which Flask maps URL endpoints to Python functions. Each route corresponds to a specific function that is called whenever the URL is accessed.

Key Concepts:

    Defining routes using the @app.route decorator.
    Creating multiple routes with different URLs.
    Handling different HTTP methods (GET, POST).

Example Code:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the about page."

if __name__ == "__main__":
    app.run(debug=True)
