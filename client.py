from flask import Blueprint, Flask, request, send_from_directory

mod = Blueprint('static', __name__)

@mod.route('/<path:path>', methods=['GET'])
def send_static_file(path):
    return send_from_directory('static', path)

@mod.route('/', methods=['GET'])
def render_root():
    return send_from_directory('static', 'index.html')

