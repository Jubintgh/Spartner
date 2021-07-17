from flask.blueprints import Blueprint
from flaskblueprints, 
from app.models import Answer

user_routes = Blueprint('answers', __name__)

#error handling

@user_routes.route('/:userid')
def get_answers():
    pass

@user_routes.route('/:userid')
def post_answers():
    pass

@user_routes.route('/:userid')
def update_answer():
    pass