#Firebase initialization
import pyrebase

class database():
	def __init__(self):

		firebaseConfig = {
			"apiKey": "AIzaSyAozr8Le3FYqMXmn5AMfhG2uolPsI5w8gE",
			"authDomain": "kodikon-cad93.firebaseapp.com",
			"databaseURL": "https://kodikon-cad93-default-rtdb.firebaseio.com",
			"projectId": "kodikon-cad93",
			"storageBucket": "kodikon-cad93.appspot.com",
			"messagingSenderId": "1044884536591",
			"appId": "1:1044884536591:web:97598f9270530f0c18127a",
		}

		self.firebase = pyrebase.initialize_app(firebaseConfig)
		self.auth = self.firebase.auth()
		self.db = self.firebase.database()
		self.storage = self.firebase.storage()
		