import ccy
from flask import Flask, request
from my_app.product.views import product_blueprint
from flask_sqlalchemy import SQLAlchemy #dd
from 

#flask applicatin context
from my_app import create_app #dd

app = create_app() #dd
app.test_request_context().push() #dd
#Do whatever needs to be done
app.test_request_context().pop() #dd
app = Flask(__name__)
app.register_blueprint(product_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' #dd
db = SQLAlchemy(app) #dd

from my_app.product.views import product #dd
app.register_blueprint(product) #dd

db.create_all() #dd criar a tabela quando app for executado

#Vamos registrar a aplicação
db = SQLAlchemy() #dd
def create_app(): #dd 
    app = Flask(__name__) #dd
    db.init_app(app) #dd
    return app #dd
#Vamos usar contexto de gerenciamento
  


@app.template_filter('format_currency')
def format_currency_filter(amount):
	currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or 'USD'
	return '{0} {1}'.format(currency_code, amount)
