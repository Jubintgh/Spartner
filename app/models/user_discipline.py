from .db import db

class User_Discipline(db.Model):
    __tablename__ = 'user_discipline'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    discipline = db.Column(db.Integer, db.ForeignKey('discipline.id'), primary_key=True, nullable=False)