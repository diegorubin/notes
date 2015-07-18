from repository import get_connection
import pdb

class Note():
    def __init__(self, attributes=dict()):
        self.title = attributes.get('title') or ''
        self.body = attributes.get('body') or ''
        self.path = attributes.get('path') or '/'

    def save(self):
        result = True

        try:
            db = get_connection()
            if "_id" in dir(self):
                db.notes.update({'_id' : ObjectId(self._id)},
                                    {"$set" :self.__dict__})
            else:

                self._id = db.notes.insert(self.__dict__)
        except:
            result = False

        return result

    def to_json(self):
        json = self.__dict__

        try:
            json['_id'] = str(json['_id'])
        except:
            json['_id'] = None

        return json

def find_note(uid):

    d = Note()

    try:
        db = get_connection()
        obj = db.notes.find({"_id" : ObjectId(uid)})

        d.__dict__ = obj[0]
        d.__dict__["_id"] = uid

        return d
    except:
        return None

def all_notes(**kwargs):
    notes = []

    try:
        db = get_connection()
        cursor = db.notes.find()

        for note in cursor:

            if kwargs.get('type') == 'dict':
                note['_id'] = str(note['_id'])
                notes.append(note)
            else:
                d = Note()
                d.__dict__ = note
                notes.append(d)

    except:
        pass

    return notes

