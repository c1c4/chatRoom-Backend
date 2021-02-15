from server.model.message import Message


def get_last_fifty_messages():
    return Message.query.order_by(Message.date_time.asc()).limit(50).all()
