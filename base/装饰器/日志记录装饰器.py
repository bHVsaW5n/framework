from base.数据库连接.数据库连接db import db
from sanic import response

from base.日志.file_logger import file_logger


def log_record(func):
    def wrapper(*args, **keywards):
        try:

            request = locals().get("args")[0]
            log_format = "{url} 的参数为:从request.args获取{args}, 从request.json获取{json}".format(**{
                "url": request.url,
                "args": request.args if request.args else "无",
                "json": request.json if request.json else "无",
            })
            file_logger.info(log_format)


            result = func(*args, **keywards)
            return result
        except Exception as e:
            print(e)
    return wrapper
