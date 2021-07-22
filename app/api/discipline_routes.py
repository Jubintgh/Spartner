# from flask import Blueprint
# from app.models import Discipline, User_Discipline

# discipline_routes = Blueprint('discipline', __name__)

# #error handling

# @discipline_routes.route('/<int:id>')
# def get_disciplines(id):
#     disciplines = User_Discipline.query.filter_by(User_Discipline.user_id == id)
#     return {'disciplines': [discipline.discipline_name for discipline in disciplines]}
    

# @discipline_routes.route('/<int:id>', methods=['POST'])
# def post_disciplines(disciplines_id ,id):
#     for discipline_id in disciplines_id:
#         new_discipline = User_Discipline(
#             user_id = id,
#             discipline_id = discipline_id
#         )
#         db.session.add(new_discipline)
#         db.session.commit()


# @discipline_routes.route('/<int:id>', methods=['DELETE'])
# def delete_disciplines(discipline_id):
#     User_Discipline.query.filter(User_Discipline.discipline_id == discipline_id).delete()