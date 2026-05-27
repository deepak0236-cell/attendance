from app.extensions import db

class Timetable(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    subject = db.Column(db.String(100))

    teacher = db.Column(db.String(100))

    time = db.Column(db.String(50))

    room = db.Column(db.String(50))