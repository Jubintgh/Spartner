from flask import Blueprint, jsonify
from flask import request
from flask_login import login_required
from app.forms import AnswerForm, SignUpForm, UpdateUserInfoForm
from app.models import Answer, User, db
import random

"""


----------------------------------- USER PROFILE APIs -----------------------------------


"""

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
    user_answer = user.to_dict()
    user_answer.update(user.answer.to_dict())
    users_answers.append(user_answer)
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
# @login_required
def user(id):
    user = User.query.get(id)
    user_answer = user.to_dict()
    user_answer.update(user.answer.to_dict())
    return user_answer



@user_routes.route('<int:id>/profile/update', methods=['PUT'])
# @login_required
def edit_info(id):
    """
    Updates Info
    """
    form = UpdateUserInfoForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ex_user_info = User.query.get(id)
        form.populate_obj(ex_user_info)
        ex_user_info.email = form.data["email"]
        ex_user_info.username = form.data["username"]
        ex_user_info.password = form.data["password"]
        ex_user_info.first_name = form.data["first_name"]
        ex_user_info.last_name = form.data["last_name"]
        ex_user_info.age = form.data["age"]
        ex_user_info.discipline = form.data["discipline"]
        ex_user_info.location = form.data["location"]
        ex_user_info.gender = form.data["gender"]
        ex_user_info.coach = form.data["coach"]
        ex_user_info.img_url = form.data["img_url"]
    
        db.session.commit()
        return ex_user_info.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

"""


----------------------------------- USER LIKES APIs -----------------------------------


"""


#getAllUserLikes
@user_routes.route('/<int:id>/likes')
# @login_required
def get_likes(id):

    user = User.query.get(id)
    likes = user.likes

    return {'user_likes': [like.to_dict() for like in likes]}

#getAllLikedBy
@user_routes.route('/<int:id>/liked')
# @login_required
def get_liked_by(id):

    user = User.query.get(id)
    liked_by = user.liked_by

    return {'likes_user': [like.to_dict() for like in liked_by]}

#createLike
@user_routes.route('/<int:id>/like', methods=['POST'])
# @login_required
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
# @login_required
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
# @login_required
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

    # users_answers = random.shuffle(users_answers)
    list = [ans for ans in users_answers]
    return {'users_answers': random.sample(list, len(list))}


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


"""


----------------------------------- USER ANSWERS APIs -----------------------------------


"""

@user_routes.route('/<int:id>/answers')
# @login_required
def get_answers(id):
    answer = Answer.query.filter_by(Answer.user_id == id)
    return {'answers': answer}

@user_routes.route('/<int:id>/answers', methods=['POST'])
# @login_required
def post_answers(id):
    """
    Creates a new answer and adds them in database
    """
    
    form = AnswerForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_answer = Answer(
            user_id = id,
            about = form.data["about"],
            reach = form.data["reach"],
            professional_level = form.data["professional_level"],
            current_record = form.data["current_record"],
            previous_titles = form.data["previous_titles"],
            fav_rocky_fighter = form.data["fav_rocky_fighter"],
            walkout_song = form.data["walkout_song"],
            vaccinated = form.data["vaccinated"],
            has_kids = form.data["has_kids"],
            in_person = form.data["in_person"],
            nickname = form.data["nickname"],
            religion = form.data["religion"],
            pets = form.data["pets"],
            availability = form.data["availability"],
            rate = request.json["rate"],
            weight_class = form.data["weight_class"]
        )

        db.session.add(new_answer)
        db.session.commit()
        return new_answer.to_dict()

    return {"errors": form.errors}

@user_routes.route('/<int:id>/answers/update', methods=['PUT'])
# @login_required
def update_answer(id):
    """
    Edits a existing answer and in our database based on the user's id
    """

    form = AnswerForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ex_user_answer=Answer.query.filter(Answer.user_id == id).first()
        form.populate_obj(ex_user_answer)
        ex_user_answer.about = form.data["about"]
        ex_user_answer.reach = form.data["reach"]
        ex_user_answer.professional_level = form.data["professional_level"]
        ex_user_answer.current_record = form.data["current_record"]
        ex_user_answer.previous_titles = form.data["previous_titles"]
        ex_user_answer.fav_rocky_fighter = form.data["fav_rocky_fighter"]
        ex_user_answer.walkout_song = form.data["walkout_song"]
        ex_user_answer.vaccinated = form.data["vaccinated"]
        ex_user_answer.nickname = form.data["nickname"]
        ex_user_answer.religion = form.data["religion"]
        ex_user_answer.has_kids = form.data["has_kids"]
        ex_user_answer.pets = form.data["pets"]
        ex_user_answer.availability = form.data["availability"]
        ex_user_answer.rate = request.json["rate"]
        ex_user_answer.in_person = form.data["in_person"]
        ex_user_answer.weight_class = form.data["weight_class"]

        db.session.commit()
        return ex_user_answer.to_dict()
    return {"errors": validation_errors_to_error_messages(form.errors)}, 401

"""


----------------------------------- Filters APIs -----------------------------------


"""

@user_routes.route('/<int:id>/filter/<filter_t>')
def filter_user(filter_t, id):

    curr_user = User.query.get(id)
    likes_users = curr_user.likes
    disliked_users = curr_user.dislikes

    no_show = [like.id for like in likes_users] #list of users that have been liked
    dislikes_ids = [dislike.id for dislike in disliked_users] #list of users that have been disliked

    no_show = no_show + dislikes_ids #combine above 2 lists
    no_show.append(id) #list of users not to show

    unseen_users = User.query.filter(User.id.not_in(no_show))

    if filter_t == "vaccination":
        user_vacc_stat = curr_user.answer.vaccinated
        similar_users = []
        for user in unseen_users:
            if user.answer.vaccinated == user_vacc_stat:
                similar_users.append(user)
                
        # return { "vacc_stat": [ user.to_dict() for user in similar_users]}

    if filter_t == "weight-class":
        user_wc_stat = curr_user.answer.weight_class
        similar_users = []

        for user in unseen_users:
            if user.answer.weight_class == user_wc_stat:
                similar_users.append(user)
    
        # return { "wc_stat": [ user.to_dict() for user in similar_users]}

    if filter_t == "professional-level":
        user_pro_stat = curr_user.answer.professional_level
        similar_users = []

        for user in unseen_users:
            if user.answer.professional_level == user_pro_stat:
                similar_users.append(user)
    
        # return { "pro_stat": [ user.to_dict() for user in similar_users]}

    if filter_t == "coach":
        similar_users = []

        for user in unseen_users:
            if user.coach == True:
                similar_users.append(user)
    
    return { "users_answers": [ user.to_dict() for user in similar_users]}
