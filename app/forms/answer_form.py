from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange


class AnswerForm(FlaskForm):
    about = StringField('about', validators=[DataRequired()])
    reach = IntegerField('reach', validators=[DataRequired()])
    professional_level = IntegerField('professional level', validators=[NumberRange(min=0, max=5, message=None)])
    current_record = StringField('current record')
    previous_titles = StringField('previous titles')
    fav_rocky_fighter = StringField('fav rocky fighter')
    walkout_song = StringField('walkout song')
    vaccinated = BooleanField('vaccinated')
    nickname = StringField('nick name')
    religion = StringField('religion')
    has_kids = BooleanField('has_kids')
    pets = StringField('pets')
    availability = IntegerField('availability')
    rate = IntegerField('rate', validators=[DataRequired()]),
    in_person = BooleanField('in person')
    weight_class = IntegerField('weight class', validators=[DataRequired()])