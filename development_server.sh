#!/bin/bash

export LUNA_GATE_BASE_URL=http://localhost:5000/
export LUNA_GATE_AUTHORIZE_URL=http://localhost:5000/o/authorize
export LUNA_GATE_CONSUMER_ID=http://localhost:5000/o/authorize
export LUNA_GATE_CONSUMER_SECRET=http://localhost:5000/o/authorize

python notes_app.py

