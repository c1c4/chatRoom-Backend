from flask import request, Blueprint

from server.service.user_service import create_user

user_blueprint = Blueprint('user_urls', __name__)


@user_blueprint.route('/users', methods=['POST'])
def post_user():
    user_json = request.json

    return create_user(user_json)
