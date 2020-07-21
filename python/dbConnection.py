import pyrebase
import urllib.request
import urllib.error
import json




config = {
  "apiKey": "AIzaSyBMPg_FoALZ_n5_hRnkjdZ0fDQ7AjvRRnM",
  "authDomain": "dbtestproject-462f7.firebaseapp.com",
  "databaseURL": "https://dbtestproject-462f7.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

data = {"name": "Hashini Lakshika Kumanayake"}

db.child("Users").push(data)

print("Data Added to the Real Time Database")