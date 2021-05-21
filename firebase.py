# Import libraries
import firebase_admin
from firebase_admin import credentials, db

from distance import calc_distance
from datetime import datetime
import time

import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

class Firebase:
    # CONSTRUCTOR WITH CONNECTION
    def __init__(self, city_id, street_id):
        cred = credentials.Certificate(path + '/FirebaseKey.json')
        
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://smartcity-75e0e-default-rtdb.firebaseio.com/'
        })
        self.row = "cities"
        self.ref = db.reference("cities").child(str(city_id)).child("containers").child(str(street_id)).child("tracking_data")

    # INSERT DATA FUNCTION
    def insertFirebaseRow(self, uniqueInteger):
        index = len(self.ref.get())

        # Select what row you want to insert
        # insert_object = {
        #     u'id': index,
        #     u'day': str(datetime.today().strftime("%Y-%m-%d")),
        #     u'time': str(datetime.now().strftime("%H:%M:%S")),
        #     u'remaining_distance': calc_distance()
        # }

        # self.ref.child(str(index)).set(insert_object)
        return str(index), "Row is inserted...", str(datetime.now())

    
    # Clears the database table
    def clearTable(self):
        print("Aborting data tracking and clearing database...")
        self.ref.delete()
        return "Cleaning your data", "Database is cleaned", str(datetime.now())

