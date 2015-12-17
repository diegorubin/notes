from flask import Blueprint, redirect, session, request, url_for
from oauth.labluna import lunagate

mod = Blueprint('auth', __name__)

@mod.route('/live', methods=['GET'])
def live():
    pass

@mod.route('/login', methods=['POST'])
def login():
    return luna_gate.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

@mod.route('/logout', methods=['DELETE'])
def logout():
    pass

@mod.route('/authorized')
@lunagate.authorized_handler
def authorized(resp):
    next_url = request.args.get('next') or url_for('index')

    session['luna_gate_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['luna_gate_user'] = resp['screen_name']

    print 'You were signed in as %s' % resp['screen_name']
    return redirect(next_url)

