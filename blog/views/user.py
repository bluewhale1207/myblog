# -*_coding: utf-8 -*-

from blog import app
from flask import Blueprint, request, url_for, render_template
from flask_login import login_required, logout_user, login_user

from flask import redirect

from blog.models.model_user import User

mod = Blueprint('auth', __name__)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login_user(user, remember=True)
#     user.update_last_login_time()


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        next = request.args.get('next')
        name = request.args.get('name')
        password = request.args.get('password')
        # user = User.query.filter_by(name=name)
        # hashlib.md5(password).hexdigest()

        user = User.query.filter_by(name=name)
        login_user(user)
        # # permission to access the `next` url
        # if not next_is_valid(next):
        #     return flask.abort(400)

        # return flask.redirect(next or flask.url_for('index'))
    else:
        return render_template('login.html')


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


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
