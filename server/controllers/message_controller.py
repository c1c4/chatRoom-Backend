from flask import Blueprint

from server.service.message_service import retrieve_last_fifty

messages_blueprint = Blueprint('messages_urls', __name__)


@messages_blueprint.route('/messages/last_fifty', methods=['GET'])
def get_last_fifty_messages():
    return retrieve_last_fifty()
