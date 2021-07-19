from flask.blueprints import Blueprint
from app.models import Answer

answer_routes = Blueprint('answers', __name__)

#error handling

@answer_routes.route('/')
def get_answers():
    pass

@answer_routes.route('/', method=['POST'])
def post_answers():
    pass

@answer_routes.route('/', method=['PUT'])
def update_answer():
    pass