from app import db
from app.common import CRUD

class Orders(CRUD, db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    food_id = db.Column(db.Integer)
    plates = db.Column(db.Integer)
    date_added = db.Column(db.DateTime)

    def __init__(self, user_id, food_id, plates, date_added):
        self.user_id = user_id
        self.food_id = food_id
        self.plates = plates
        self.date_added = date_added

    def __repr__(self):
        return '<Orders %r>' % (self.title)