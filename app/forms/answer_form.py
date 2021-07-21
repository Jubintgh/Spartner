from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    about = StringField('about', validators=[DataRequired()])
    weight_class = IntegerField('weight class', validators=[DataRequired()])
    reach = IntegerField('reach', validators=[DataRequired()])
    professional_level = IntegerField('professional level', validators=[DataRequired()])
    current_record = StringField('current record', validators=[DataRequired()])
    previous_titles = StringField('previous titles', validators=[DataRequired()])
    fav_rocky_fighter = StringField('fav rocky fighter', validators=[DataRequired()])
    walkout_song = StringField('walkout song', validators=[DataRequired()])
    vaccinated = BooleanField('vaccinated', validators=[DataRequired()])
    nickname = StringField('nick name', validators=[DataRequired()])
    religion = StringField('religion', validators=[DataRequired()])
    offspring = StringField('offspring', validators=[DataRequired()])
    pets = StringField('pets', validators=[DataRequired()])
    availability = IntegerField('availability', validators=[DataRequired()])
    rate = IntegerField('rate', validators=[DataRequired()])
