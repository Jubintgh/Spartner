from flask import Blueprint, jsonify
from flask import request
from flask_login import login_required
from app.forms import AnswerForm, SignUpForm
from app.models import User, db, Answer

user_routes = Blueprint('users', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

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

@user_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_info(id):
    """
    Updates Info
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        editted_user = User.query.get(id)
        form.populate_obj(editted_user)
        # editted_user = User(
        #     username=form.data['username'],
        #     email=form.data['email'],
        #     password=form.data['password'],
        #     first_name=form.data['first_name'],
        #     last_name=form.data['last_name'],
        #     age=form.data['age'],
        #     location=form.data['location'],
        #     gender=form.data['gender'],
        #     coach=form.data['coach'],
        #     discipline=form.data['discipline'],
        #     img_url=form.data['img_url']
        # )
        # db.session.add(editted_user)
        db.session.commit()
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

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

@user_routes.route('/<int:id>/answers')
def get_answers(id):
    answer = Answer.query.filter_by(Answer.user_id == id)
    return {'answers': answer}

@user_routes.route('/<int:id>/answers', methods=['POST'])
def post_answers(id):
    """
    Creates a new anwer and adds them in database
    """
    form = AnswerForm()
    if form.validate_on_submit():
        new_answer = Answer(
            user_id = id,
            about = form.data['about'],
            weight_class = form.data['weightClass'],
            reach = form.data['reach'],
            professional_level = form.data['professionalLevel'],
            current_record = form.data['currentRecord'],
            previous_titles = form.data['previousTitles'],
            fav_rocky_fighter = form.data['favRockyFighter'],
            walkout_song = form.data['walkoutSong'],
            vaccinated = form.data['vaccinated'],
            nickname = form.data['nickname'],
            religion = form.data['religion'],
            has_kids = form.data['hasKids'],
            pets = form.data['pets'],
            availability = form.data['availability'],
            in_person = form.data['inPerson'],
            rate = form.data['rate']
        )
        db.session.add(new_answer)
        db.session.commit()
    return {"errors": form.errors}

@user_routes.route('/<int:id>/answers', methods=['PUT'])
def update_answer():
    pass
