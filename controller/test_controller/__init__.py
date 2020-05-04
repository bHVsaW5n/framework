from sanic import Blueprint

from controller.test_controller.error import error_bp
from controller.test_controller.user import user_bp

bps = [
    user_bp,
    error_bp
]

group = Blueprint.group(*bps, url_prefix='/group')