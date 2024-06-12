PRODUCTS = {
    'iphone': {
        'name': 'iPhone 5S',
        'category': 'Phones',
        'price': 699,
    }, 
    'galaxy': {
        'name': 'Samsung Galaxy 5',
        'category': 'Phones',
        'price': 649,
    },
    'ipad-air': {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649,
    },
    'ipad-mini': {
        'name': 'iPad Mini',
        'category': 'Tablets',
        'price': 549
    }
}

#acrescentado
from my_app import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	#name = db.Column(db.String(255), unique=True, nullable=False)
	price = db.Column(db.Float)
	category_id = db.Column(db.Integer,
	db.ForeignKey('category.id'))
	category = db.relationship(
 'Category', backref=db.backref('products', lazy='dynamic')
 )



	def __init__(self, name, price, categoria):
		self.name = name
		self.price = price
		self.categoria = categoria
	#self.price = price
     
def __repr__(self):
 	return '<Product %d>' % self.id




