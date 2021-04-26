# Import libraries
import firebase_admin
from firebase_admin import credentials, db
import random

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
        self.ref = db.reference("cities").child("0").child("containers").child("0").child("tracking_data")
    
    # INSERT DATA FUNCTION
    def insertFirebaseRow(self, uniqueInteger):
        # Select what row you want to insert
        insert_object = {
            u'id': uniqueInteger,
            u'day': str(datetime.today().strftime("%Y-%m-%d")),
            u'time': str(datetime.now().strftime("%H:%M:%S")),
            u'remaining_distance': random.randint(1, 99)
        }

        self.ref.child(str(uniqueInteger)).set(insert_object)
        
        print(f"Row is inserted...")
        print(f"Updated row is {uniqueInteger}")
        
        return str(uniqueInteger), "Row is inserted...", str(datetime.now())

    
    # Clears the database table
    def clearTable(self):
        print("Aborting data tracking and clearing database...")
        self.ref.delete()
        return "Cleaning your data", "Database is cleaned", str(datetime.now())

