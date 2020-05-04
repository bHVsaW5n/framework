"""
测试 redis做缓存， redis中不存在则去数据库查，并计入缓存
"""
import json
import time

from base.redis_helper.redis_helper import RedisHelper
from model.chat import Chat

redis_helper = RedisHelper("redis_pool")
r = redis_helper.r


def decorate(func):
    def wrapper(*args, **keywargs):
        start = time.time()
        source, content = func(*args, **keywargs)
        end = time.time()
        print("%s运行时间" % source, end - start)
        print("内容", content)
        return source, content

    return wrapper


@decorate
def get_chat_content(customer_id, direction):
    key = "{customer_id}-{direction}".format(**{"customer_id": customer_id, "direction": direction})

    content = r.get(key)
    print("content", content)
    if content:
        return "redis", content
    else:
        chat_objs = Chat.select().where(Chat.customer_id == customer_id, Chat.direction == direction).order_by(
            Chat.gen_time.desc())
        datalist = [{"id": obj.id, "customer_id": obj.customer_id, "direction": obj.direction, "content": obj.content,
                     "gen_time": str(obj.gen_time)[:19]} for obj in chat_objs]
        r.set(key, json.dumps(datalist), ex=5)
        return "数据库", datalist


if __name__ == '__main__':
    get_chat_content(1, 0)
    time.sleep(1)
    get_chat_content(1, 0)
