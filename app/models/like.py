from .db import db


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    display = db.Column(db.Boolean, default=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())