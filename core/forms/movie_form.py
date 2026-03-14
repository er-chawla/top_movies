from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
class MovieForm(FlaskForm):
    rating = SelectField('Rating', choices=[("7.5", "7.5"), ("8.0", "8.0"), ("8.5", "8.5"), ("9.0", "9.0"), ("9.5", "9.5"), ("10.0", "10.0")], validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')