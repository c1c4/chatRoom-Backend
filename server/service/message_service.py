from flask import jsonify

from server.message_broker.send import send_stock_message
from server.model.message import Message
from server.repository.default_repository import save
from server.repository.message_repository import get_last_fifty_messages


def save_message(json_message):
    message = Message.convert_dto_to_model(json_message)
    save(message, is_insert=True)

    if not is_command_message(message):
        message_dto = Message.convert_model_to_dto(message)
        response = jsonify(message_dto)
        return response.json, False
    else:
        send_stock_message(message.message)
        return None, True


def retrieve_last_fifty():
    messages_list = get_last_fifty_messages()
    messages_list_dto = []
    for message in messages_list:
        message_dto = Message.convert_model_to_dto(message)
        messages_list_dto.append(message_dto)

    return jsonify(messages_list_dto), 200


def is_command_message(message):
    if message.message.startswith('/stock='):
        return True
    else:
        return False
