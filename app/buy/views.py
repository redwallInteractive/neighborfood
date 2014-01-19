from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from app import app, db
from forms import Order
from app.buy.models import Orders
from app.sell.models import Food
from datetime import datetime

modd = Blueprint('buyModule', __name__)

@modd.route('/cart/<int:food_id>/', methods=('GET', 'POST'))
def order(food_id):
    if(session.get('logged_in')):
        form = Order(request.form)
        order = Orders(session.get('id'),food_id,int(form.plates.data),datetime.utcnow())
        db.session.add(order)
        db.session.commit()

        food = Food.query.filter_by(id=food_id).first()
        food.orders = int(food.orders) + int(form.plates.data)
        db.session.add(food)
        db.session.commit()

        return redirect('/payment')
    else:
        return redirect('/login')