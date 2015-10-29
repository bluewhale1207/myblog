# -*_coding: utf-8 -*-

from flask.ext.login import UserMixin
from blog.database import db
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    create_time = db.Column(db.DateTime, default=datetime.now())
    last_login_time = db.Column(db.DateTime)

    def is_authenticated(self):
        # 如果用户已经登录，必须返回True，否则返回Fals
        return True

    def is_activity(self):
        # 如果允许用户登录，必须返回True，否则返回False。如果要禁用账户，可以返回False
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return 1
