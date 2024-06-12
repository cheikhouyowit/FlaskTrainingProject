from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint
from my_app.product.models import PRODUCTS


web_blueprint = Blueprint('product', __name__)


@web_blueprint.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'], product['name'])
    return {'full_name': full_name}


@web_blueprint.route('/')
@web_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@web_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)