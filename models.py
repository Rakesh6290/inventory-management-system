from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Supplier(db.Model):
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city
        }


class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    supplier = db.relationship('Supplier', backref='items')

    def to_dict(self):
        return {
            "id": self.id,
            "supplier": self.supplier.name if self.supplier else None,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "price": self.price
        }