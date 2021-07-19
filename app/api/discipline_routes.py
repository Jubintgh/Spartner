from flask import Blueprint
from app.models import Discipline

discipline_routes = Blueprint('discipline', __name__)

#error handling

@discipline_routes.route('/:userid')
def get_disciplines():
    pass

@discipline_routes.route('/:userid', methods=['POST'])
def post_disciplines():
    pass


@discipline_routes.route('/:userid', methods=['DELETE'])
def delete_disciplines():
    pass