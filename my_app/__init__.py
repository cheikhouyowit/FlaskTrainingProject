import ccy
from flask import Flask, request
from my_app.product.views import product_blueprint
from my_app.catalog.views import catalog

from flask import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(product_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.register_blueprint(catalog)

db.create_all()




@app.template_filter('format_currency')
def format_currency_filter(amount):
	currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or 'USD'
	return '{0} {1}'.format(currency_code, amount)
