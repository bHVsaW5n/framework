import asyncio_redis

from sanic import Sanic
from sanic.response import text
from sanic_session import RedisSessionInterface

app = Sanic()


# Token from https://github.com/subyraman/sanic_session

class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host='172.12.78.218', port=6379, poolsize=10, password="Password123", db=10
            )

        return self._pool


redis = Redis()

# pass the getter method for the connection pool into the session
session_interface = RedisSessionInterface(redis.get_redis_pool, expiry=604800)


@app.middleware('request')
async def add_session_to_request(request):
    # before each request initialize a session
    # using the client's request
    await session_interface.open(request)


@app.middleware('response')
async def save_session(request, response):
    # after each request save the session,
    # pass the response to set client cookies
    await session_interface.save(request, response)


@app.route("/")
async def test(request):
    # interact with the session like a normal dict
    if not request['session'].get('foo'):
        request['session']['foo'] = 0
        request.cookie = 1

    request['session']['foo'] += 1

    response = text(request['session']['foo'])

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)