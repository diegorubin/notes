from repository import get_connection
import pdb

class Document():
    def __init__(self, attributes=dict()):
        self.title = attributes.get('title') or ''
        self.body = attributes.get('body') or ''
        self.path = attributes.get('path') or '/'

    def save(self):
        result = True

        try:
            db = get_connection()
            if "_id" in dir(self):
                db.documents.update({'_id' : ObjectId(self._id)},
                                    {"$set" :self.__dict__})
            else:

                self._id = db.documents.insert(self.__dict__)
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

def find_document(uid):

    d = Document()

    try:
        db = get_connection()
        obj = db.documents.find({"_id" : ObjectId(uid)})

        d.__dict__ = obj[0]
        d.__dict__["_id"] = uid

        return d
    except:
        return None

def all_documents(**kwargs):
    documents = []

    try:
        db = get_connection()
        cursor = db.documents.find()

        for document in cursor:

            if kwargs.get('type') == 'dict':
                document['_id'] = str(document['_id'])
                documents.append(document)
            else:
                d = Document()
                d.__dict__ = document
                documents.append(d)

    except:
        pass

    return documents

