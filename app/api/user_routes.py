from flask import Blueprint, jsonify
from flask import request
from flask_login import login_required
from app.models import User, db, Answer

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


"""


----------------------------------- USER LIKES APIs -----------------------------------


"""


#getAllUserLikes
@user_routes.route('/<int:id>/likes')
def get_likes(id):

    user = User.query.get(id)
    likes = user.likes

    return {'user_likes': [like.to_dict() for like in likes]}

#getAllLikedBy
@user_routes.route('/<int:id>/liked')
def get_liked_by(id):

    user = User.query.get(id)
    likes = user.liked_by

    return {'likes_user': [like.to_dict() for like in likes]}

#createLike
@user_routes.route('/<int:id>/like', methods=['POST'])
def new_like(id):
    liked_instance = request.json
    liked_user_id = liked_instance['liked_id']

    liker = User.query.get(id)
    liked = User.query.get(liked_user_id)

    liked.liked_by.append(liker)
    db.session.commit()

    return {
            'liked_user': 'success'
           }


#removeLike
@user_routes.route('/<int:id>/like', methods=['DELETE'])
def delete_like(id):
    liked_instance = request.json
    liked_user_id = liked_instance['liked_id']

    liker = User.query.get(id)
    liked = User.query.get(liked_user_id)

    liked.liked_by.remove(liker)
    db.session.commit()

    return {
            'liked_user': 'success'
           }

"""


----------------------------------- USER ANSWERS APIs -----------------------------------


"""
@user_routes.route('/<int:id>/answers', methods=['POST'])
def post_answers():
    """
    Creates a new anwer and adds them in database
    """
    form = AnswerForm()
    if form.validate_on_submit():
        new_answer = Answer(
            user_id = form.data['user_id'],
            about = form.data['about'],
            weight_class = form.data['weight_class'],
            reach = form.data['reach'],
            professional_level = form.data['professional_level'],
            current_record = form.data['current_record'],
            previous_titles = form.data['previous_titles'],
            fav_rocky_fighter = form.data['fav_rocky_fighter'],
            walkout_song = form.data['walkout_song'],
            vaccinated = form.data['vaccinated'],
            nickname = form.data['nickname'],
            religion = form.data['religion'],
            offspring = form.data['offspring'],
            pets = form.data['pets'],
            availability = form.data['availability'],
            in_person = form.data['in_person'],
            rate = form.data['rate']
        )
        db.session.add(new_answer)
        db.session.commit()
