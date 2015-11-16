# -*_coding: utf-8 -*-
import uuid
import hashlib

from werkzeug import security


from blog.database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer)
    location = db.Column(db.String(25))
    salt = db.Column(db.String(32))
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

    @classmethod
    def get_user_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        return user

    @classmethod
    def get_user_by_name(cls, name):
        user = cls.query.get(name=name).first()
        return user

    def check_password(self, password):
        # password = hashlib.md5(self.salt + password).hexdigest()
        # if self.password != password:
        #     return 1
        # return 0
        return security.check_password_hash(self.password, password)

    def change_password(self, password):
        pass

    @classmethod
    def set_password(cls, password):
        # salt = uuid.uuid4().hex
        # password = hashlib.md5(salt + password).hexdigest()
        # return password
        security.generate_password_hash(password)
