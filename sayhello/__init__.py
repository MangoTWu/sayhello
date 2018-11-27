# -*- coding: utf-8 -*-
"""
    :author: Mango Wu
    :url: https://mangowu.me
    :copyright: © 2018 Mango Wu <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask("sayhello")
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from sayhello import views, errors, commands


