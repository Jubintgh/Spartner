from .db import db

class User_Discipline(db.Model):
    __tablename__ = 'user_discipline'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    discipline = db.Column(db.Integer, db.ForeignKey('discipline.id'), nullable=False)