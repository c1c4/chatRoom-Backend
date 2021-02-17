from flask import jsonify

from server.model.message import Message
from server.repository.default_repository import save
from server.repository.message_repository import get_last_fifty_messages
from server.request.chatBot_requests import send_to_chatbot


def save_message(json_message):
    message = Message.convert_dto_to_model(json_message)
    save(message, is_insert=True)

    message_dto = Message.convert_model_to_dto(message)
    response = jsonify(message_dto)

    if is_command_message(message):
        stock_code = message.message.split('=')
        send_to_chatbot(stock_code[1])

    return response.json


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
