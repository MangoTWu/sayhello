# -*- coding: utf-8 -*-
"""
    :author: Mango Wu (吴谢)
    :url: https://mangowu.me
    :copyright: © 2018 Mango Wu <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired, Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired, Length(1, 200)])
    submit = SubmitField('Submit')
