from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
   

    def __repr__(self):
        return f"Product('{self.name}', '{self.category}', '{self.price}')"


    def __iter__(self):
        # Definindo um iterador sobre os atributos do objeto
        return iter((self.name, self.category, self.price))