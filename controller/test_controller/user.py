from sanic import Blueprint
from sanic import response
from aiofiles import os as async_os
from sanic.response import file_stream

from base.装饰器.日志记录装饰器 import log_record

user_bp = Blueprint('user_bp', url_prefix='/user')

def add(a=2, b=4):
    return a+b

@user_bp.middleware
async def print_on_request(request):
    print("I am a spy")


@user_bp.route("/", methods=["GET"])
@log_record
async def halt_request(request):
    return response.json(add(a=3, b=4))



@user_bp.route("/a", methods=["GET"])
@log_record
async def handle_request(request):
    return response.json("hahaha")



@user_bp.route("/img")
async def index(request):
    file_path = "static/img_224.zip"

    file_stat = await async_os.stat(file_path)
    headers = {"Content-Length": str(file_stat.st_size)}

    return await file_stream(
        file_path,
        headers=headers,

    )
