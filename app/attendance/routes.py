from flask import Blueprint, request, jsonify
from app.extensions import db
from app.database.models.attendance import Attendance

attendance_bp = Blueprint(
    'attendance',
    __name__
)

@attendance_bp.route('/mark', methods=['POST'])
def mark_attendance():

    data = request.json

    attendance = Attendance(
        student_id=data['student_id'],
        status=data['status']
    )

    db.session.add(attendance)
    db.session.commit()

    return jsonify({
        "message": "Attendance Marked"
    })