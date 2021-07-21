from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/likes')
def get_likes(id):

    # likes = User.query.all()
    likes = User.query.get(id)

    print('asdjnasfidjndsafnsdfkjnsdjkfsdkjnfkjSSSSSSSSSSSSAAASSS', likes.likeds.like_id)
    return {'likes':[ like.to_dict() for like in likes]}

@user_routes.route('/<int:id>/praised')
def get_praised(id):
    praised = Like.query.filter_by(praised_id=id)
    return {'praised': [praise.praised_id for praise in praised]}

@user_routes.route('/', methods=['POST'])
def post_like(praiser_id, praised_id):
    new_like = Like(praiser_id= praiser_id, praised_id=praised_id)
    db.session.add(new_like)
    db.session.commit()

@user_routes.route('/<int:id>', methods=['DELETE'])
def delete_like(id):
    Like.query.filter(Like.id == id).delete()
