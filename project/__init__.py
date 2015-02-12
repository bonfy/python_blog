#################
#### imports ####
#################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_weixin import Weixin

import os

################
#### config ####
################

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
weixin = Weixin(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint


app.add_url_rule('/weixin', view_func=weixin.view_func)

from weixin import *

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
