from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(30), nullable=False)
    last_name = db.Column(db.VARCHAR(30), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.VARCHAR, nullable=False) #Fix VARCHAR length based on format
    gender = db.Column(db.Integer, nullable=False) #1=Female 2=Male 3=Other
    coach = db.Column(db.Boolean, default=False)
    img_url = db.Column(db.VARCHAR)
    discipline = db.Column(db.VARCHAR(50), nullable=False)

    answer = db.relationship(
        "Answer",  uselist=False,
        back_populates="user"
    )

    likes = db.Table(
    "likes",
    db.Column("liker_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("liked_id", db.Integer, db.ForeignKey("users.id"))
    )

    liked_users = db.relationship(
        "User",
        secondary=likes,
        primaryjoin=(likes.c.liker_id == id),
        secondaryjoin=(likes.c.liked_id == id),
        backref=db.backref("likes", lazy="dynamic"),
        lazy="dynamic"
    )

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


