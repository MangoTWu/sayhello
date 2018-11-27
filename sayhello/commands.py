# -*- coding: utf-8 -*-
"""
    :author: Mango Wu (吴谢)
    :url: https://mangowu.me
    :copyright: © 2018 Mango Wu <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import click
from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker('zh_CN')  # 创建生成虚拟数据的实例
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)
