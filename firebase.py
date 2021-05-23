# IMPORT MODULES
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import pathlib

# IMPORT CLASSES
from distance import calc_distance

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
        self.status_set = db.reference("cities").child(str(city_id)).child("containers").child(str(street_id)).child("status")
        self.city_id = city_id
        self.street_id = street_id

    # INSERT DATA FUNCTION
    def insert_Firebase_Row(self):
        index = len(self.ref.get())
        # CREATE INSERT OBJECT
        insert_object = {
            u'id': index,
            u'day': str(datetime.today().strftime("%Y-%m-%d")),
            u'time': str(datetime.now().strftime("%H:%M:%S")),
            u'remaining_distance': calc_distance()
        }
        
        self.ref.child(str(index)).set(insert_object)

        distance = calc_distance()
        print(distance)
        if distance < 8:
            self.status_set.set("False")
        else:
            self.status_set.set("True")

    # GET CONTAINER INFORMATION 
    def get_container_info(self, key):
        return db.reference("cities").child(str(self.city_id)).child("containers").child(str(self.street_id)).get().get(key)

    # GET CITY INFORMATION
    def get_city_info(self):
        return db.reference("cities").child(str(self.city_id)).get().get("city_name")

    # CLEARS TRACKING_DATA INFORMATION 
    def clearTable(self):
        print("Aborting data tracking and clearing database...")
        self.ref.delete()
        return "Cleaning your data", "Database is cleaned", str(datetime.now())

