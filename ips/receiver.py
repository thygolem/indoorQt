import os
import json
import time
import datetime
import paho.mqtt.client
import pymongo
from  pymongo import MongoClient
from config import *


    
def on_connect(client, userdata, flags, rc):
    #print("rc: " + str(rc))
    print('USUARIO: (%s)' % client._client_id)
    #Subscribe to topic
    client.subscribe('indoor', 0) #client.subscribe('topic', qos)
#Receive gateway and devices data

def on_message(client, userdata, message):
    esp = message.payload
    esp_mac, near_mac , rssi = str(esp[45:62]).lower(), str(esp[71:88]).lower(), int(esp[97:100])
    esp_mac, near_mac= str(esp_mac[2:-1]), str(near_mac[2:-1])
    espAlias    = "B/F/Z" # ASIGNAR ALIAS EN DB
    #_id = ObjectId()
    #print("\n", "esp_mac ",esp_mac,"\n", "near_mac ",near_mac, "\n", "RRSI ",rssi)
    
    objectIdentifier = esp_mac + ', ' + 'fe:24:27:b8:d9:13'
    #indoor_data = {"_id": objectIdentifier}, {"rssi": rssi}
    collection_count = collection.count_documents({})
    print(collection_count)
    if collection_count == 0:
        collection.insert_one({"_id": objectIdentifier}, {"rssi": rssi})
        print('nueva colección')
    else:
        collection.update_one({"_id": objectIdentifier}, {'$set':{"rssi": rssi}})
        print("\n", "esp_mac ",esp_mac,"\n", "near_mac ",near_mac, "\n", "RRSI ",rssi)
    
    #indoor_data = {"_id": esp_mac + ', ' + near_mac, "near_mac": near_mac, "rssi": rssi}
    #collection.insert_one(indoor_data)
    print("guardado en DB")


def main():
    #Mqtt connection
    mqttc = paho.mqtt.client.Client(client_id = 'mqttSimo')
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.username_pw_set(CLOUDMQTT_USER, CLOUDMQTT_PASS)
    mqttc.connect(CLOUDMQTT_HOST, CLOUDMQTT_PORT, keepalive=60)
    #Broker loop
    mqttc.loop_forever()


    
if __name__ == '__main__':
    main()



