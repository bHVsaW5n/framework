from sanic import blueprints
from sanic import response
# from base.装饰器.返回装饰器 import response_deractor
from base.装饰器.返回装饰器 import async_json_response
from service.测试大量请求并发访问数据库.database_service import database_test_service

database_test = blueprints.Blueprint("database_test_bp", url_prefix="/db_test")


@database_test.route("/get_data_from_database", methods=["GET"])
# @async_json_response()
async def get_data_from_database(request):
    return response.json(database_test_service.get_data_from_db())



