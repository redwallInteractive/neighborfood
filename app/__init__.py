from flask import Flask, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# create application
app = Flask(__name__)
app.config.from_object('config.DebugConfiguration')

#db
db = SQLAlchemy(app)

#register the sell module blueprint
from app.sell.views import mod as sellModule
app.register_blueprint(sellModule)

#register the buy module blueprint
from app.buy.views import modd as buyModule
app.register_blueprint(buyModule)

#register user Model
from app.user.views import mod as userModule
app.register_blueprint(userModule)

