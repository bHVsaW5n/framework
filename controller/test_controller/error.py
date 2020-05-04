
from sanic import Blueprint
from sanic import response
from sanic.exceptions import ServerError
from sanic.exceptions import abort
from sanic.response import text

error_bp = Blueprint('error_bp', url_prefix='/error')

@error_bp.route("/", methods=["GET"])
async def halt_request(request):
    raise ServerError("Something bad happened", status_code=400)



@error_bp.route('/abort')
async def no_no(request):
    abort(400)
    # this won't happen
    return text("OK")

