from .db import db


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    praiser_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    praised_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    display = db.Column(db.Boolean, default=True)
    
    praiser_user = db.relationship('User', back_populates="praiser_likes")
    praised_user = db.relationship('User', back_populates="praised_likes")
