from flask_socketio import emit

def notify(message):

    emit(
        'notification',
        {'message': message},
        broadcast=True
    )