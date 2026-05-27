from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):

    name = StringField(
        'Name',
        validators=[DataRequired()]
    )

    email = StringField(
        'Email',
        validators=[DataRequired()]
    )

    course = StringField(
        'Course',
        validators=[DataRequired()]
    )

    submit = SubmitField('Add Student')
