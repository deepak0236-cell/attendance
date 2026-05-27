from app.extensions import db

class Marks(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer)

    subject = db.Column(db.String(100))

    marks = db.Column(db.Integer)