# -*_coding: utf-8 -*-

from flask import Blueprint
import datetime

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    return 'Hello World!' + datetime.datetime.now().strftime('%Y-%m-%d')


@mod.route('/tags')
def tags():
    return 'tags'
