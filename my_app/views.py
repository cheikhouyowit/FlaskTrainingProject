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
            product = Products(request.form['name'], 
                               request.form['price'])

            db.session.add(product)
            db.session.commit()
            flash('Product was successfully added')
            return redirect(url_for('show'))
    return render_template('new.html')

#metodo para deletar
@my_app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    product = Products.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Product deletado com sucesso!', 'success')
    else:
        flash('Products não encontrado!', 'error')
    return redirect(url_for('show'))

#metodo para editar
@my_app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = Products.query.get(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        db.session.commit()
        flash('Product atualizado com sucesso!', 'success')
        return redirect(url_for('show'))
    return render_template('edit.html', product=product)


@my_app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    products = Products.query.filter(Products.name.ilike(f'%{query}%')).all()
    return render_template('index.html', products=products)



