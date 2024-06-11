from flask import request, flash, url_for, redirect, render_template
from . import db
from .models import Products
from flask import current_app as my_app

@my_app.route('/')
def show():
    return render_template('home.html', products=Products.query.all())

@my_app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['price']:
            flash('Please enter all the fields', 'error')
        else:
            product = Products(request.form['name'], request.form['price'])

            db.session.add(product)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show'))
    return render_template('product.html')
