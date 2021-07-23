from flask import Blueprint, jsonify
from flask import request
from flask_login import login_required
from app.forms import AnswerForm
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
            nickname = form.data["nickname"],
            religion = form.data["religion"],
            has_kids = form.data["has_kids"],
            pets = form.data["pets"],
            availability = form.data["availability"],
            rate = request.json["rate"],
            in_person = form.data["in_person"],
            weight_class = form.data["weight_class"]
        )

        db.session.add(new_answer)
        db.session.commit()
        return new_answer.to_dict()

    return {"errors": form.errors}

@user_routes.route('/<int:id>/answers', methods=['PUT'])
def update_answer():
    pass

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
    
        return { "vacc_stat": [ user.to_dict() for user in similar_users]}

    if filter_t == "weight-class":
        user_wc_stat = curr_user.answer.weight_class
        similar_users = []

        for user in unseen_users:
            if user.answer.weight_class == user_wc_stat:
                similar_users.append(user)
    
        return { "wc_stat": [ user.to_dict() for user in similar_users]}

    if filter_t == "professional-level":
        user_pro_stat = curr_user.answer.professional_level
        similar_users = []

        for user in unseen_users:
            if user.answer.professional_level == user_pro_stat:
                similar_users.append(user)
    
        return { "pro_stat": [ user.to_dict() for user in similar_users]}
        
    if filter_t == "coach":
        similar_users = []

        for user in unseen_users:
            if user.coach == True:
                similar_users.append(user)
    
        return { "coach_stat": [ user.to_dict() for user in similar_users]}