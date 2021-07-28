import pyrebase
import mysql.connector
from mysql.connector import Error


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


class MySQL:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='thejacob.eu',
                                                 database='trainz',
                                                 user='trainz',
                                                 password='Ymwfl@15chsk')

            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

    def create_table(self, table_name, content):
        self.cursor.execute(f"CREATE TABLE {table_name} ({content})")