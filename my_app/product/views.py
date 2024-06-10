from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint
from my_app.product.models import PRODUCTS
from flask import request, jsonify, Blueprint #dd
from my_app import app, db #dd
from my_app.product.models import Product #dd

product_blueprint = Blueprint('product', __name__)

#ESTE METODO VAI NOS REDIRECIONAR A NOSSA PAGINA HOME
product = Blueprint('product', __name__) #dd

@product.route('/') #dd
@product.route('/home') #dd
def home(): #dd
    return "Welcome to the Catalog Home" #dd

#ESTE METODO VAI NOS mostrar QUAL USUARIO VIU PRODUTO
@product.route('/product/<id>') #dd
def product(id): #dd
    product = Product.query.get_or_404(id) #dd
    return 'Product - %, $%s' % (product.name, product.price) #dd

#ESTE METODO CONTRALA A SAIDA DE PRODUTOS
@product.route('/products') #dd
def products(): #dd
    products = Product.query.all()#dd 
    rest = {} #dd
    for product in products: #dd
        rest[product.id] = {
            'name': product.name,
            'price': str(product.price)
        }
        return jsonify(rest) #dd
    
    #RETORNAR PRODUTOS NO FORMATO JSON
    @product.route('/product-create', methods = ['POST',]) #dd
    def create_product(): #dd
        name = request.form.get('name') #dd
        price = request.form.get('price') #dd
        product = Product (name, price) #dd
        db.session.commit() #dd
        return 'Product created.' #dd

@product_blueprint.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'], product['name'])
    return {'full_name': full_name}


@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)
