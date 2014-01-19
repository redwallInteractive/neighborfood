from flask_wtf import Form
from wtforms import TextField, TextAreaField, DateField
from wtforms.validators import Required


class PostFood(Form):
    title = TextField('title', validators = [Required()])
    cuisine = TextField('cuisine', validators = [Required()])
    description = TextAreaField('description', validators = [Required()])
    price = TextField('price', validators = [Required()])
    plates = TextField('plates', validators = [Required()])
    location = TextField('location', validators = [Required()])
    date = DateField('date')