from .db import db
from .user import User


class Answer(db.Model):
    __tablename__ = 'answers'

    # id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    about = db.Column(db.Text)
    reach = db.Column(db.Integer, nullable=False)
    professional_level = db.Column(db.Integer, nullable=False)
    current_record = db.Column(db.VARCHAR, default='0-0-0')
    previous_titles = db.Column(db.VARCHAR)
    fav_rocky_fighter = db.Column(db.VARCHAR)
    walkout_song = db.Column(db.VARCHAR)
    vaccinated = db.Column(db.Boolean)
    nickname = db.Column(db.VARCHAR)
    religion = db.Column(db.VARCHAR)
    has_kids = db.Column(db.Boolean)
    pets = db.Column(db.VARCHAR)
    availability = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    in_person = db.Column(db.Boolean)
    weight_class = db.Column(db.Integer, nullable=False)

    user = db.relationship(
        "User",
        back_populates="answer"
    )

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'about': self.about,
            'weight_class': self.weight_class,
            'reach': self.reach,
            'professional_level': self.professional_level,
            'current_record': self.current_record,
            'previous_titles': self.previous_titles,
            'fav_rocky_fighter': self.fav_rocky_fighter,
            'walkout_song': self.walkout_song,
            'vaccinated': self.vaccinated,
            'nickname': self.nickname,
            'religion': self.religion,
            'has_kids': self.has_kids,
            'pets': self.pets,
            'availability': self.availability,
            'rate': self.rate
        }
