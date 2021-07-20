from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    username = StringField(
    'username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), Email(), user_exists])
    password = StringField('password', validators=[DataRequired()])
    first_name = StringField('first name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])
    discipline = SelectMultipleField('disciplines', choices=[('Southpaw'), ('Kickboxing'), ('Orthodox'), ('Judo'),  ('Muay Thai'), ('Grappling'), ('Counter Striker'), ('Karate'), ('Switch'), ('Brazilian Jiu-Jitsu')], validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    coach = BooleanField('trainer')
    image_url = StringField('Profile picture URL')
