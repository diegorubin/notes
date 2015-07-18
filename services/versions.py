from flask import Blueprint, Response, jsonify, request
from repository.document import Document, all_documents

mod = Blueprint('verions', __name__)

@mod.route('/documents/<id>/versions', methods=['GET'])
def versions(document_id):
    pass

