from base.redis_helper import RedisHelper
import threading

def get_news():
    print("订阅者1建立")
    redis_helper = RedisHelper("redis_pool")
    r = redis_helper.r
    sub = r.pubsub()
    sub.psubscribe(["mes"])  # 订阅一个频道
    while True:
        item = sub.get_message()
        if item:
            print("有消息发布，为：", item)


t = threading.Thread(target=get_news)
t.start()