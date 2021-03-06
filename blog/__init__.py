# -*- coding: utf-8 -*-
import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from blog.models.model_user import User

app = Flask(__name__)
app.config.from_object(os.environ['BLOG_SETTINGS'])


# 登录
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '.user_login_required'
login_manager.login_message = u'请登录'

db = SQLAlchemy()
db.init_app(app)


@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(name=username).first()


from blog.views import general
from blog.views import user
app.register_blueprint(general.mod)
app.register_blueprint(user.mod)
