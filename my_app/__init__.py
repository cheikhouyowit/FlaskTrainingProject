import ccy
from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy #//


from flask_migrate import Migrate, MigrateCommand
from redis import Redis
from flask_mongoengine import MongoEngine


redis = Redis()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app) #//
migrate = Migrate(app, db)




import my_app.product.views

db.create_all()

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'my_catalog'}
app.debug = True
db = MongoEngine(app)
redis = Redis()
from my_app.product.views import catalog
app.register_blueprint(catalog)

#//
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from my_app.product.views import catalog
app.register_blueprint(catalog)

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
#//



@app.template_filter('format_currency')
def format_currency_filter(amount):
	currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or 'USD'
	return '{0} {1}'.format(currency_code, amount)

