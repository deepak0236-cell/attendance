from app.extensions import db
from datetime import datetime

class Attendance(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey('student.id')
    )

    status = db.Column(db.String(20))
    time = db.Column(db.DateTime, default=datetime.utcnow)