from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.database.models.student import Student
from app.database.models.teacher import Teacher

admin_bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)

@admin_bp.route('/')
def dashboard():

    students = Student.query.all()
    teachers = Teacher.query.all()

    return render_template(
        'admin/dashboard.html',
        students=students,
        teachers=teachers
    )

@admin_bp.route('/add_student', methods=['POST'])
def add_student():

    student = Student(
        name=request.form['name'],
        email=request.form['email'],
        course=request.form['course']
    )

    db.session.add(student)
    db.session.commit()

    return redirect('/admin')

@admin_bp.route('/add_teacher', methods=['POST'])
def add_teacher():

    teacher = Teacher(
        name=request.form['name'],
        email=request.form['email'],
        subject=request.form['subject']
    )

    db.session.add(teacher)
    db.session.commit()

    return redirect('/admin')