from .db import db

class Discipline(db.Model):
    __tablename__ = 'disciplines'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    discipline_name = db.Column(db.VARCHAR(20), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    users_discipline = db.relationship('User_Discipline', back_populates='disciplines')