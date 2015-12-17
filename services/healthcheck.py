from flask import Blueprint

mod = Blueprint('healthcheck', __name__)

@mod.route('/healthcheck', methods=['GET'])
def healthcheck():
    pass

