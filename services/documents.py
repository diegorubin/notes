from flask import Blueprint, jsonify

from repository.document import Document

mod = Blueprint('documents', __name__)

@mod.route('/documents')
def documents():
    return jsonify(dict(teste='1'))

