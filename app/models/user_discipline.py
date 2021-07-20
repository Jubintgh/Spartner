from .db import db

class User_Discipline(db.Model):
    __tablename__ = 'user_discipline'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), primary_key=True, nullable=False)

    disciplines = db.relationship('Discipline', back_populates='users_discipline')
    users_id = db.relationship('User', back_populates='users_id')

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'discipline_id': self.discipline_id
        }
