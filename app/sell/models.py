from app import db
from app.common import CRUD

class Food(CRUD, db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(50))
    cuisine = db.Column(db.String(120))
    description = db.Column(db.String(240))
    price = db.Column(db.Integer)
    plates = db.Column(db.Integer)
    location = db.Column(db.String(240))
    date_available = db.Column(db.DateTime)
    orders = db.Column(db.Integer)
    date_added = db.Column(db.DateTime)

    def __init__(self, user_id, title, cuisine, description, price, plates, location, orders, date_added):
        self.user_id = user_id
        self.title = title
        self.cuisine = cuisine
        self.description = description
        self.price = price
        self.plates = plates
        self.location = location
        self.orders = orders
        self.date_added = date_added

    def __repr__(self):
        return '<Food %r>' % (self.title)