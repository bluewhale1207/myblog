# -*_coding: utf-8 -*-
import hashlib

from flask import (Blueprint, request, url_for, render_template, redirect,
                   jsonify)
from flask_login import login_required, logout_user, login_required

from blog.operation import usercore

mod = Blueprint('/user', __name__)


@mod.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    code, msg = usercore.register(email, password, name=name)
    print '--------------------------', code, msg
    return jsonify(code=code, msg=msg)


# @mod.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         next = request.args.get('next')
#         name = request.args.get('name')
#         password = request.args.get('password')

#         # # permission to access the `next` url
#         # if not next_is_valid(next):
#         #     return flask.abort(400)

#         return redirect(next or url_for('.index'))
#     else:
#         return render_template('login.html')


@mod.route('/login-required')
def user_login_required():
    return render_template('/login.html')


@mod.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('/index.html')

# @mod.route('/login', methods=['POST'])
# def login():
#     email = request.form['email']
#     password = request.form['password']
#     user = AdminUser.get_by_email(email)
#     if user and user.get_encrypt_password(password) == user.password \
#             and user.status == 0:
#         resp = make_response(redirect(url_for('.index')))
#         cookie_name = custom_login.LOGIN_COOKIE_NAME
#         custom_login.set_cookie(resp, cookie_name, user.email, user.password)
#         return resp
#     return 'login failture'


@mod.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
