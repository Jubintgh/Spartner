from flask import Blueprint, jsonify
from app.models import Like

user_routes = Blueprint('likes', __name__)

#error handling

@user_routes.route('/<int:id>/praisers')
def get_praisers(id):
    praisers = Like.query.filter_by(praised_id=id)
    return {'praisers': [praiser.praiser_id for praiser in praisers]}

@user_routes.route('/<int:id>/praised')
def get_praised(id):
    praised = Like.query.filter_by(praised_id=id)
    return {'praised': [praise.praised_id for praise in praised]}

@user_routes.route('/', method=['POST'])
def new_like(praiser_id, praised_id):
    like = Like(praiser_id= praiser_id, praised_id=praised_id)
    db.session.add(like)
    db.session.commit()

@user_routes.route('/<int:id>', method=['DELETE'])
def delete_like(id):
    Like.query.filter(Like.id == id).delete()