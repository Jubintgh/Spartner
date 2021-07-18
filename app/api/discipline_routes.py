from flask import Blueprint
from app.models import Discipline

user_routes = Blueprint('discipline', __name__)

#error handling

@user_routes.route('/:userid')
def get_disciplines():
    pass

@user_routes.route('/:userid', method=['POST'])
def post_disciplines():
    pass


@user_routes.route('/:userid', method=['DELETE'])
def delete_disciplines():
    pass