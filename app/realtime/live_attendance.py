from flask_socketio import emit

def update_attendance(student):

    emit(
        'attendance_update',
        {'student': student},
        broadcast=True
    )