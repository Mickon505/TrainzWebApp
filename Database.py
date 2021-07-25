import pyrebase


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
