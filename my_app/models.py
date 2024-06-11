from . import db

class Products(db.Model):
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price= db.Column(db.Float(50))
       
    def __init__(self, name, price):
        self.name = name
        self.price = price