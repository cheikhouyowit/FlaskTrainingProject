

from flask import request, flash, url_for, redirect, render_template, session
from . import db
from .models import Product
from flask import current_app as app






@app.route('/product')
def show_all():
    product = Product.query.all()
    return render_template('home.html', product=product)


# Rota de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar o nome de usuário e senha (isso é um exemplo simples, você deve fazer verificações adequadas)
        if username == 'odc' and password == 'odc':
            # Autenticação bem-sucedida, redirecionar para a página principal
            session['logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('show_all'))
        else:
            # Autenticação falhou, redirecionar de volta para a página de login com uma mensagem de erro
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('login'))
    
    # Se o método for GET (ou qualquer outro), renderizar o formulário de login
    return render_template('index.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        product = Product(name=request.form['name'],
                          category=request.form['category'],
                          price=request.form['price'],
                          )
        db.session.add(product)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('add_product.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.category = request.form['category']
        product.price = request.form['price']
        
        db.session.commit()
        flash('Record was successfully updated')
        return redirect(url_for('show_all'))
    return render_template('edit.html', product=product)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    flash('Record was successfully deleted')
    return redirect(url_for('show_all'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        product = Product.query.filter(Product.name.like(f"%{search_term}%")).all()
        return render_template('search_results.html', product=product)
    return render_template('base.html')