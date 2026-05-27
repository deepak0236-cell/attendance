from app.database.models.attendance import Attendance

def total_attendance():

    return Attendance.query.count()

def absent_students():

    return Attendance.query.filter_by(
        status='Absent'
    ).count()