from sanic import Blueprint

from controller.测试大量请求同时访问数据库.测试并发访问数据库 import database_test



db_group_list = [
database_test
]

db_bp_group = Blueprint.group(*db_group_list, url_prefix="/db_group")