from app.extensions import db

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    course = db.Column(db.String(100))
    attendance = db.relationship('Attendance', backref='student')