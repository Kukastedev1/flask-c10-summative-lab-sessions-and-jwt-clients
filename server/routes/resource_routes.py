from flask import Blueprint, request
from models import Note
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

resource_bp = Blueprint('resource_bp', __name__)


# GET NOTES 
@resource_bp.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    user_id = int(get_jwt_identity())

    page = request.args.get('page', 1, type=int)
    per_page = 5

    pagination = Note.query.filter_by(user_id=user_id)\
        .paginate(page=page, per_page=per_page)

    # Return ARRAY 
    return [
        {"id": n.id, "title": n.title, "content": n.content}
        for n in pagination.items
    ], 200


# CREATE NOTE
@resource_bp.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    # safety check
    if not data or not data.get('title') or not data.get('content'):
        return {"error": "Title and content required"}, 400

    note = Note(
        title=data['title'],
        content=data['content'],
        user_id=user_id
    )

    db.session.add(note)
    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }, 201


# UPDATE NOTE
@resource_bp.route('/notes/<int:id>', methods=['PATCH'])
@jwt_required()
def update_note(id):
    user_id = get_jwt_identity()
    note = Note.query.get(id)

    if not note or note.user_id != user_id:
        return {"error": "Unauthorized"}, 403

    data = request.get_json()

    if not data:
        return {"error": "No data provided"}, 400

    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)

    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }, 200


# DELETE NOTE
@resource_bp.route('/notes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_note(id):
    user_id = get_jwt_identity()
    note = Note.query.get(id)

    if not note or note.user_id != user_id:
        return {"error": "Unauthorized"}, 403

    db.session.delete(note)
    db.session.commit()

    return {"message": "Deleted"}, 200