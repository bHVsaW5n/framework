from base.数据库连接.数据库连接db import db
from sanic import response

def async_json_response():
    def response_deractor(func):
        def wrapper(*args, **keywards):
            # with db.atomic as t:
            try:
                result = func()
                if isinstance(result, str) or isinstance(result, list) or isinstance(result, dict):
                    return response.json({
                        'meta': {
                            'code': 2000,
                            'internal_message': [],
                            'user_message': "sdf",
                            'notice': "Sdfsd"
                        },
                        'dataset': result
                    })

                if isinstance(result, tuple):
                    return response.json({
                        'meta': {
                            'code': 2000,
                            'internal_message': [],
                            'user_message': "sdf",
                            'notice': "Sdfsd"
                        },
                        'dataset': {"datalist":result[0], "count":result[1]}
                    })
            except Exception as e:
                print(e)
                    # t.rollback()
        return wrapper
    return response_deractor
