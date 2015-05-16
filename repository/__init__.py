from pymongo.connection import Connection
from bson.objectid import ObjectId
import os

db = None

def get_connection():
    global db

    if db == None:
        print "Conectando ao Mongo"
        connection = Connection('localhost')

        try:
            env = os.environ["NOTES_ENV"]
        except:
            env = "test"

        if env == "production":
            db = connection['notes_prod']
        else:
            db = connection['notes_test']

    return db


