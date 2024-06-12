from werkzeug.exceptions import abort
from flask import render_template, jsonify, request
from flask import Blueprint
from my_app import app, db
from my_app.product.models import Product, Category
#importar intanciaS adiconar

catalog = Blueprint('catalog', __name__)
@catalog.route('/')
@catalog.route('/home')
def home():
 return "Welcome to the Catalog Home."

product_blueprint = Blueprint('product', __name__)

@catalog.route('/product/<id>')
def product(id):
 product = Product.query.get_or_404(id)
 return 'Product - %s, $%s' % (product.name, product.price)

@catalog.route('/products')
def products():
 products = Product.query.all()
 res = {}
 for product in products:
    res[product.id] = {
 'name': product.name,
 'price': str(product.price)
 }
    
    return jsonify(res) 
 @catalog.route('/product-create', methods=['POST',])
 def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    product = Product(name, price)
    db.session.add(product)
    db.session.commit()
 return 'Product created.'


@product_blueprint.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'], product['name'])
    return {'full_name': full_name}


@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=Product)

@product_blueprint.route('/product/<key>')
def product(key):
    product = Product.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)


@catalog.route('/products')
def products():
 products = Product.query.all()
 res = {}
 for product in products:
    res[product.id] = {
 'name': product.name,
 'price': product.price,
 'category': product.category.name
 }
 return jsonify(res)

@catalog.route('/product-create', methods=['POST',])
def create_product():
 name = request.form.get('name')
 price = request.form.get('price')
 categ_name = request.form.get('category')
 category = Category.query.filter_by(name=categ_name).first()
 if not category:
    category = Category(categ_name)
 product = Product(name, price, category)
 db.session.add(product)
 db.session.commit()
 return 'Product created.'

@catalog.route('/category-create', methods=['POST',])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return 'Category created.'


@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    res = {}
    for category in categories:
     res[category.id] = {
        'name': category.name
    }
    for product in category.products:
        res[category.id]['products'] = {
            'id': product.id,
            'name': product.name,
             'price': product.price
     }
    return jsonify(res)

from my_app import redis
@catalog.route('/product/<id>')
def product(id):
 product = Product.query.get_or_404(id)
 product_key = 'product-%s' % product.id
 redis.set(product_key, product.name)
 redis.expire(product_key, 600)
 return 'Product - %s, $%s' % (product.name, product.price)

from decimal import Decimal
from flask import request, Blueprint, jsonify
from my_app.product.models import Product

catalog = Blueprint('catalog', __name__)
@catalog.route('/')
@catalog.route('/home')
def home():
 return "Welcome to the Catalog Home."
@catalog.route('/product/<key>')
def product(key):
 product = Product.objects.get_or_404(key=key)
 return 'Product - %s, $%s' % (product.name, product.price)
@catalog.route('/products')
def products():
 products = Product.objects.all()

 res = {}
 for product in products:
    res[product.key] = {
 'name': product.name,
 'price': str(product.price),
 }
 return jsonify(res)
@catalog.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    key = request.form.get('key')
    price = request.form.get('price')
    product = Product(
         name=name,
         key=key,
         price=Decimal(price)
 )
    product.save()
    return 'Product created.'
