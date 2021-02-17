import csv

import requests

from server import NotFound, ApiBaseException
from server.configuration import config


def send_to_chatbot(stock_code: str):
    response = requests.get(url=f'{config.CHAT_BOT}/search-stock/{stock_code}')
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        raise NotFound
    else:
        raise ApiBaseException
