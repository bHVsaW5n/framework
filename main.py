from sanic import Sanic, Blueprint
from sanic.response import *
from sanic import response
import datetime

from controller.test_controller import group
from controller.test_controller.user import user_bp
from sanic_cors import CORS

from controller.测试大量请求同时访问数据库 import db_bp_group

app = Sanic()
CORS(app, resources={r"*": {"origins": "*"}})
# CORS(app, resources={r"*": {"origins": ['.*']}})
bp = Blueprint('bp', url_prefix='/bp')
bp.static('/img', './static/img_224.zip', stream_large_files=True)
# bp.static('/img', '/img_224.zip', name='img_224.zip')

app.blueprint(bp)
app.blueprint(group)
app.blueprint(db_bp_group)
print(app.router.__dict__)


if __name__ == "__main__":
    app.run(host="172.16.77.223", port=8000, debug=True, auto_reload=False)

