from flask_socketio import SocketIO

from server import init_api
from server.controllers.login_controller import login_blueprint
from server.controllers.user_controller import user_blueprint
from server.service.message_service import save_message

app = init_api()
app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)
socketio = SocketIO(app, cors_allowed_origins="*")


# TODO - Discover how to move to a separeted file
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('message')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    message_saved, is_command = save_message(json)

    if not is_command:
        socketio.emit('my response', message_saved, callback=messageReceived)


def main():
    socketio.run(app, debug=True, host='localhost', port='8080')


if __name__ == '__main__':
    main()
