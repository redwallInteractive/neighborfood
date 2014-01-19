from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from app import app, db
from forms import PostFood
from app.buy.forms import Order
from app.sell.models import Food
from datetime import datetime

mod = Blueprint('sellModule', __name__)

@mod.route('/post/', methods=('GET', 'POST'))
def post_view():
    if(session.get('logged_in')):
        form = PostFood(request.form)
        if form.validate_on_submit():
            post = Food(session.get('id'),form.title.data,form.cuisine.data,form.description.data,form.price.data,form.plates.data,form.location.data,0,datetime.utcnow())
            #form.populate_obj(post)
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        return render_template('sell/add.html', form=form)
    else:
        return redirect('/login')

@mod.route('/')
def showFood():
    posts = Food.query.order_by(Food.id)
    return render_template('search.html', posts=posts)

@mod.route('/food/<int:food_id>/', methods=('GET', 'POST'))
def singleFood(food_id):
    post = Food.query.filter_by(id=food_id).first()
    if(post.orders is None):
        post.orders = 0
    count = (int(post.plates) - int(post.orders)) + 1
    form = Order(request.form)
    form.plates.choices = [(x, x) for x in range(1, int(count))]
    return render_template('single.html', post=post, form=form)