from flask import Blueprint, jsonify
from flask import request
from flask_login import login_required
from app.forms import AnswerForm, SignUpForm, UpdateForm
from app.models import Answer, User, db

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
# @login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
# @login_required
def user(id):
    user = User.query.get(id)
    user_answer = user.to_dict()
    user_answer.update(user.answer.to_dict())
    print(user_answer)
    return user_answer



#!!!!!!! still fixing this put route for user information!!!!!!!!!!!!!!!!!!!!!!!
# @user_routes.route('/<int:id>', methods=['PUT'])
# def edit_info(id):
#     """
#     Updates Info
#     """
#     form = UpdateForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         editted_user = User.query.get(id)
#         # form.populate_obj(editted_user)
#         editted_user = User(
#             username=form.data['username'],
#             email=form.data['email'],
#             first_name=form.data['first_name'],
#             last_name=form.data['last_name'],
#             age=form.data['age'],
#             location=form.data['location'],
#             gender=form.data['gender'],
#             coach=form.data['coach'],
#             discipline=form.data['discipline'],
#             img_url=form.data['img_url']
#         )
#         db.session.add(editted_user)
#         db.session.commit()
#         return user.to_dict()
#     return {'errors': validation_errors_to_error_messages(form.errors)}, 401

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
    liked_by = user.liked_by

    return {'likes_user': [like.to_dict() for like in liked_by]}

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

#createDisLike
@user_routes.route('/<int:id>/dislike', methods=['POST'])
def new_dislike(id):
    disliked_instance = request.json
    disliked_user_id = disliked_instance['disliked_id']

    disliker = User.query.get(id)
    disliked = User.query.get(disliked_user_id)

    disliked.disliked_by.append(disliker)
    db.session.commit()

    return {
            'disliked_user': 'success'
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
    Creates a new answer and adds them in database
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
    """
    Edits a existing answer and in our database based on the user's id
    """

    form = AnswerForm()
    if form.validate_on_submit():
        edit_answer=Answer.query.filter(Answer.user_id == id)
        form.populate_obj(edit_answer)
        db.session.commit()
    return {"errors": form.errors}

"""


----------------------------------- Discover routes APIs -----------------------------------


"""
#DicoverPage
@user_routes.route('<int:id>/discover')
def get_user_list(id):
    user = User.query.get(id)
    likes_users = user.likes
    disliked_users = user.dislikes

    no_show = [like.id for like in likes_users] #list of users that have been liked
    dislikes_ids = [dislike.id for dislike in disliked_users] #list of users that have been disliked

    no_show = no_show + dislikes_ids #combine above 2 lists
    no_show.append(id) # add self

    unseen_user = User.query.filter(User.id.not_in(no_show))

    users_answers = []
    for user in unseen_user:
        user_answer = user.to_dict()
        user_answer.update(user.answer.to_dict())
        users_answers.append(user_answer)
    return {'users_answers': [ans for ans in users_answers]}

#Matches render
@user_routes.route('<int:id>/matches')
def get_matches_list(id):
    user = User.query.get(id)
    likes = user.likes
    liked_by = user.liked_by
    matches = []

    for like in likes:
        for like_b in liked_by:
            if like.id == like_b.id:
                matches.append(like)

    return { 'matches': [match.to_dict() for match in matches]}
