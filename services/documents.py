import json

from flask import Blueprint, Response, jsonify, request
from repository.document import Document, all_documents

mod = Blueprint('documents', __name__)

@mod.route('/documents', methods=['GET', 'POST'])
def documents():
    if request.method == 'POST':
        return create_document()
    else:
        return get_documents()

def create_document():
    document = Document(request.get_json())
    document.save()
    result = json.dumps(document.to_json())
    return Response(result, mimetype='application/json', status=201)

def get_documents():
    result = json.dumps(all_documents(type='dict'))
    return Response(result, mimetype='application/json')

