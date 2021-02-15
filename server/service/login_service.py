from flask import jsonify

from server import Unauthorized
from server.model.user import User
from server.repository.user_repository import check_user_exist


def validate_login(user_name: str, password: str):
    user = check_user_exist(user_name, password)
    if user:
        user_json = User.convert_model_to_dto(user)
        return jsonify(user_json), 200
    else:
        raise Unauthorized()
