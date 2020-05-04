from peewee import *
from base.redis_helper.redis_helper import RedisHelper


redis_helper = RedisHelper("redis_pool")
r = redis_helper.r

db = PostgresqlDatabase('ll', user='postgres', password='Password123', host='127.0.0.1', port=5432)

