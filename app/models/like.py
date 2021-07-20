from .db import db


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    praiser_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    praised_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    display = db.Column(db.Boolean, default=True)

    praiser_user = db.relationship('User', back_populates="praiser_likes")
    praised_user = db.relationship('User', back_populates="praised_likes")

    def to_dict(self):
        return {
            'id': self.id,
            'praiser_id': self.praiser_id,
            'praised_id': self.praised_id
        }

    follows = db.Table(
        "follows", 
        db.Column("follower_id", db.Integer, db.ForeignKey("users.id")),
        db.Column("followed_id", db.Integer, db.ForeignKey("users.id"))
    )