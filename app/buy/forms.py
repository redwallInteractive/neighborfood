from flask_wtf import Form
from wtforms import SelectField

class Order(Form):
    plates = SelectField('plates',coerce=int)