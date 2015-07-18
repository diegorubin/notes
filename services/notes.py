import json

from flask import Blueprint, Response, jsonify, request
from repository.note import Note, all_notes

mod = Blueprint('notes', __name__)

@mod.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        return create_note()
    else:
        return get_notes()

def create_note():
    note = Note(request.get_json())
    note.save()
    result = json.dumps(note.to_json())
    return Response(result, mimetype='application/json', status=201)

def get_notes():
    result = json.dumps(all_notes(type='dict'))
    return Response(result, mimetype='application/json')

