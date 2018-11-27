# -*- coding: utf-8 -*-
"""
    :author: Mango Wu (吴谢)
    :url: https://mangowu.me
    :copyright: © 2018 Mango Wu <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime

from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
