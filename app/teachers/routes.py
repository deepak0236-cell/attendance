from flask import Blueprint, render_template

teacher_bp = Blueprint(
    'teacher',
    __name__
)

@teacher_bp.route('/teacher')
def teacher_dashboard():

    return render_template(
        'teacher/dashboard.html'
    )