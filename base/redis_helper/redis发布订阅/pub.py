from base.redis_helper import RedisHelper

redis_helper = RedisHelper("redis_pool")
r = redis_helper.r

r.publish("mes", "水电费东方闪电")