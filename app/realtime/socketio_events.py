from flask_socketio import emit

def register_events(socketio):

    @socketio.on('message')
    def handle_message(data):

        emit(
            'response',
            {'data': data},
            broadcast=True
        )