from flask_oauth import OAuth
import os

oauth = OAuth()
lunagate = oauth.remote_app('luna_gate',
    base_url=os.environ['LUNA_GATE_BASE_URL'],
    request_token_url='',
    access_token_url='',
    authorize_url=os.environ['LUNA_GATE_AUTHORIZE_URL'],
    consumer_key=os.environ['LUNA_GATE_CONSUMER_ID'],
    consumer_secret=os.environ['LUNA_GATE_CONSUMER_SECRET']
)

