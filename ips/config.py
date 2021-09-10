import pymongo
from  pymongo import MongoClient


#MONGODB_URI = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false'
client = MongoClient('mongodb://localhost:27017/')

db = client.indoor_db
collection = db.indoor_collection

db = client['ESP32DB']
collection = db['BLEDATA']


# MQTT config info
# CLOUDMQTT_HOST = 'suigeneris.ml'
CLOUDMQTT_HOST = '15.188.22.5'
CLOUDMQTT_PORT = 1883
CLOUDMQTT_USER = 'indoor_client'
CLOUDMQTT_PASS = 'Realtime_1'