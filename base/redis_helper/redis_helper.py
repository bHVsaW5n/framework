import redis
import time

## 测试redis是否安装成功
class RedisHelper:
    def __init__(self, type="redis"):
        if type == "redis":
            r = redis.Redis(host="172.12.78.218", db=8, password="Password123", decode_responses=True)
        else:
            pool = redis.ConnectionPool(host="172.12.78.218", db=8, password="Password123", max_connections=10, decode_responses=True)
            r = redis.Redis(host="172.12.78.218", db=8, password="Password123", decode_responses=True, connection_pool=pool)
        self.r = r


    def redis_connection_pool(self):
        pass

redis_helper = RedisHelper("redis_pool")
r = redis_helper.r

def without_pipe(r):
    start = time.time()
    for i in range(100):
        r.set("without_pipe_%s" % i, i)
    end = time.time()
    print("没有pipe", end-start)

def with_pipe(r):
    start = time.time()
    pipe = r.pipeline()
    for i in range(100):
        pipe.set("with_pipe_%s" % i, i)
    end = time.time()
    print("有管道", end - start)


without_pipe(r)
with_pipe(r)
print(r.client_list())