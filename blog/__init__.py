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
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


db = SQLAlchemy()


@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).fitst()


from blog.views import general
from blog.views import user
app.register_blueprint(general.mod)
app.register_blueprint(user.mod)
