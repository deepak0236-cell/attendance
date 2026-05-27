from app.extensions import db

class Teacher(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)