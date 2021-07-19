from flask.blueprints import Blueprint
from app.models import Answer
from app.forms import AnswerForm

answer_routes = Blueprint('answers', __name__)

#error handling

@answer_routes.route('/')
def get_answers(id):
    answer = Answer.query.filter_by(Answer.user_id == id)
    return {'answers': answer}

@answer_routes.route('/', methods=['POST'])
def post_answers():
    """
    Creates a new anwer and adds them in database
    """
    form = AnswerForm()
    new_answer = Answer(
        user_id = form.data['user_id'],
        about = form.data['about'],
        weight_class = form.data['weight_class'],
        reach = form.data['reach'],
        professional_level = form.data['professional_level'],
        current_record = form.data['current_record'],
        previous_titles = form.data['previous_titles'],
        fav_rocky_fighter = form.data['fav_rocky_fighter'],
        walkout_song = form.data['walkout_song'],
        vaccinated = form.data['vaccinated'],
        nickname = form.data['nickname'],
        religion = form.data['religion'],
        offspring = form.data['offspring'],
        pets = form.data['pets'],
        availability = form.data['availability'],
        in_person = form.data['in_person'],
        rate = form.data['rate']
    )
    db.session.add(new_answer)
    db.session.commit(new_answer)

@answer_routes.route('/', methods=['PUT'])
def update_answer():
    pass