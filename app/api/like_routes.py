from flask import Blueprint, jsonify
from app.models import Like

like_routes = Blueprint('likes', __name__)

#error handling

@like_routes.route('/likes-you/:userid')
def get_admirers():
    pass

@like_routes.route('/you-like/:userid')
def get_likes():
    pass

@like_routes.route('/', method=['POST'])
def make_like():
    pass

@like_routes.route('/:userid', method=['DELETE'])
def delete_like():
    pass