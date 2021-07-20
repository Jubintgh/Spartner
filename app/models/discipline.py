from .db import db

class Discipline(db.Model):
    __tablename__ = 'disciplines'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    discipline_name = db.Column(db.VARCHAR(20), nullable=False)

    users_discipline = db.relationship('User_Discipline', back_populates='discipline_id')
