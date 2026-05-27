from flask import Flask
from app.extensions import db, login_manager, jwt
from app.auth.routes import auth_bp
from app.students.routes import student_bp
from app.teachers.routes import teacher_bp
from app.attendance.routes import attendance_bp

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(attendance_bp)

    with app.app_context():
        db.create_all()

    return app