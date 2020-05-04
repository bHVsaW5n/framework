import datetime

from peewee import Model, IntegerField, AutoField, CharField, DateTimeField

from base.数据库连接.数据库连接db import db


class Chat(Model):
    class Meta:
        database = db
        table_name = 'chat'

    id = AutoField()
    customer_service_id = IntegerField()
    customer_id = IntegerField()
    direction = IntegerField()
    content = CharField(null=True)
    gen_time = DateTimeField(default=datetime.datetime.now())



