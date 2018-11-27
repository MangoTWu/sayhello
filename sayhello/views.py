# -*- coding: utf-8 -*-
"""
    :author: Mango Wu (吴谢)
    :url: https://mangowu.me
    :copyright: © 2018 Mango Wu <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    GET请求返回HTML页面，POST请求处理表单内容
    :return: index.html
    """
    messages = Message.query.order_by(Message.timestamp.desc()).all()  # 查询所有留言
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
