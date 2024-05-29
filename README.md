##Branch: templates

Summary: This branch covers the use of Jinja2 templates in Flask, which allows you to dynamically generate HTML on the server side. Template inheritance helps reduce redundancy, as you can create a base template that other templates extend.

Key Concepts:

    Creating and rendering templates using Flask's render_template function.
    Template inheritance to reuse common HTML structures.
    Passing variables from Flask views to templates.
    
#base.html
```sh
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Blog{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

#home.html
{% extends "base.html" %}

{% block title %}Home - My Blog{% endblock %}

{% block content %}
<h1>Welcome to my blog!</h1>
{% endblock %}

#app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

```
