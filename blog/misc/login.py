# -*- coding: utf-8 -*-


def login_required():
    @wraps(func):
    def deco(*args, **kwargs):
        if current_app.login_manager._login_disabled:
            return func(*args, **kwargs)
        elif not current_user.is_authenticated():
            