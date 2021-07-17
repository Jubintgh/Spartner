from flask import Blueprint, jsonify
from app.models import Like

user_routes = Blueprint('likes', __name__)

#error handling

@user_routes.route('/likes-you/:userid')
def get_admirers():
    pass

@user_routes.route('/you-like/:userid')
def get_likes():
    pass

@user_routes.route('/:userid', method=['POST'])
def make_like():
    pass

@user_routes.route('/:userid', method=['DELETE'])
def delete_like():
    pass