from flask import Blueprint
from app.models import Discipline

discipline_routes = Blueprint('discipline', __name__)

#error handling

@discipline_routes.route('/:userid')
def get_disciplines():
    pass

@discipline_routes.route('/:userid', method=['POST'])
def post_disciplines():
    pass


@discipline_routes.route('/:userid', method=['DELETE'])
def delete_disciplines():
    pass