from flask import jsonify

from server.model.user import User
from server.repository.default_repository import save


def create_user(json_user):
    user = User.convert_dto_to_model(json_user)
    save(user, is_insert=True)

    user_dto = User.convert_model_to_dto(user)

    return jsonify(user_dto), 200
