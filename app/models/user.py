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


    answer = db.relationship(
        "Answer",  uselist=False,
        back_populates="user"
    )

    praiser_likes = db.relationship('Like', back_populates='praiser_user')
    praised_likes = db.relationship('Like', back_populates='praised_user')
    disciplines = db.relationship('user_discipline', back_populates='users_id')

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
