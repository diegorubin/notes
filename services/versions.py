from flask import Blueprint, Response, jsonify, request
from repository.note import Note, all_notes

mod = Blueprint('verions', __name__)

@mod.route('/notes/<id>/versions', methods=['GET'])
def versions(note_id):
    pass

