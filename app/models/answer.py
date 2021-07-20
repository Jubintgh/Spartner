from .db import db
from .user import User

class Answer(db.Model):
    __tablename__ = 'answers'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    about = db.Column(db.Text)
    weight_class = db.Column(db.VARCHAR(20), nullable=False)
    reach = db.Column(db.Integer, nullable=False)
    professional_level = db.Column(db.VARCHAR(15), nullable=False)
    current_record = db.Column(db.VARCHAR, default='0-0-0')
    previous_titles = db.Column(db.VARCHAR)
    fav_rocky_fighter = db.Column(db.VARCHAR)
    walkout_song = db.Column(db.VARCHAR)
    vaccinated = db.Column(db.Boolean)
    nickname = db.Column(db.VARCHAR)
    religion = db.Column(db.VARCHAR)
    offspring = db.Column(db.VARCHAR)
    pets = db.Column(db.VARCHAR)
    availability = db.Column(db.VARCHAR)
    rate = db.Column(db.Integer)


    user = db.relationship("User", back_populates="answer")
