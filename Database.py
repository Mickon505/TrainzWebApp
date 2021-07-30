import pyrebase
from pymongo import MongoClient


class Firebase:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyCZwyinf9QGZpZZlknyFinqFttBX4Rq6uQ",
            "authDomain": "trainzcontroller.firebaseapp.com",
            "databaseURL": "https://trainzcontroller-default-rtdb.europe-west1.firebasedatabase.app/",
            "projectId": "trainzcontroller",
            "storageBucket": "trainzcontroller.appspot.com",
            "messagingSenderId": "465970089518",
            "appId": "1:465970089518:web:859d33cbeb9c44532c99bf",
            "measurementId": "G-RNTY4R1H3X"
        }

        self.app = pyrebase.initialize_app(self.config)
        self.firebaseDB = self.app.database()

    def push_data(self, data, child=None):
        if child:
            self.firebaseDB.child(child).set(data)

        else:
            self.firebaseDB.push(data)

    def get_data(self, data, child=None):
        if child:
            try:
                return self.firebaseDB.child(child).get().val()[data]

            except KeyError:
                return None

        else:
            try:
                return self.firebaseDB.get().val()[data]

            except KeyError:
                return None

    def update_data(self, data, child=None):
        if child:
            self.firebaseDB.child(child).update(data)

        else:
            self.firebaseDB.update(data)


class Mongo:
    def __init__(self, client, database=None, collection=None):
        self.cluster = MongoClient(client)
        self.db = None
        self.col = None
        if database and collection:
            self.set_database(database, collection)

    def set_database(self, db, col):
        self.db = self.cluster[str(db)]
        self.col = self.db[str(col)]

    def add(self, post):
        self.col.insert_one(post)

    def get(self, post):
        return self.col.find_one(post)

    def update(self, post, _id):
        self.col.replace_one({"_id": _id}, post)