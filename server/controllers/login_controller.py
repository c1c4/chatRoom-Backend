from flask import request, Blueprint

from server.service.login_service import validate_login

login_blueprint = Blueprint('login_urls', __name__)


@login_blueprint.route('/login', methods=['GET'])
def get_login():
    user_name = request.args.get('userName')
    password = request.args.get('password')
    return validate_login(user_name, password)
