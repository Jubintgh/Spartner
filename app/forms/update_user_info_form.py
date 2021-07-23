from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email
from .signup_form import user_exists, username_exists

class UpdateUserInfoForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), Email(), user_exists])
    password = StringField('password', validators=[DataRequired()])
    first_name = StringField('first name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])
    discipline = IntegerField('disciplines', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    coach = BooleanField('trainer')
    img_url = StringField('Profile picture URL')