from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class Selectteacher(FlaskForm):
    teacher = SelectField('Select Teacher',choices=[])
    submit = SubmitField('Show')
    
class Selectclass(FlaskForm):
    department = SelectField('Select Department',choices=[])
    semester = SelectField('Select Semester',choices=[])
    submit = SubmitField('Show')