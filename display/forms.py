from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class Selectteachers(FlaskForm):
    teacher = SelectField('Select Teacher',choices=[])
    submit = SubmitField('Show')