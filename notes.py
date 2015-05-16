# -*- coding: utf-8 -*-
"""
    Notes
    ~~~~~

    Part of labluna project.

    :copyright: (c) 2015 by Diego Rubin.
    :license: BSD, see LICENSE for more details.
"""

import os
from flask import Flask


app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from services import documents
app.register_blueprint(documents.mod)

if __name__ == '__main__':
    app.run()

