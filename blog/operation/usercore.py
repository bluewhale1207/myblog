# -*_coding: utf-8 -*-

from flask_login import login_user

from blog.models.model_user import User
from blog.database import db


def register(email, password, name=None):
    if '@' not in email:
        return 1, '邮箱格式不正确！'
    if len(password) < 6:
        return 2, '密码不能小于6位！'

    user = User.get_user_by_email(email)
    if user:
        return 3, '该邮箱已经注册过了!'
    if name is None:
        name = email.split('@')[0]

    password = User.set_password(password)
    user = User(email=email, password=password, name=name)
    db.session.add(user)
    db.session.commit()
    return 0, '创建成功!'


# def login(email, password):
#     user = User.query.filter_by(email=email).first()
#     if user.email == email and \
#             hashlib.md5(password).hexdigest() == user.password_hash:
#         login_user(user)