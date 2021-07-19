from flask import Blueprint
from app.models import Discipline, User_Discipline

discipline_routes = Blueprint('discipline', __name__)

#error handling

@discipline_routes.route('/<int:id>')
def get_disciplines(id):
    disciplines = User_Discipline.query.filter_by(User_Discipline.user_id == id)
    return {'disciplines': [discipline.discipline_name for discipline in disciplines]}
    

@discipline_routes.route('/<int:id>', methods=['POST'])
def post_disciplines(disciplines ,id):
    new_discipline = Discipline(
        discipline_name = form.data['discipline']
    )


@discipline_routes.route('/<int:id>', methods=['DELETE'])
def delete_disciplines():
    pass