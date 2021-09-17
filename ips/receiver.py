import os
import json
import time
import datetime
import paho.mqtt.client
import pymongo
from  pymongo import MongoClient
from config import *
from bson import json_util
import time

    
def on_connect(client, userdata, flags, rc):
    #print("rc: " + str(rc))
    print('USUARIO: (%s)' % client._client_id)
    #Subscribe to topic
    client.subscribe('indoor', 0) #client.subscribe('topic', qos)
#Receive gateway and devices data

def on_message(client, userdata, message):
    indoor = True
    esp = message.payload
    esp_mac, near_mac , rssi = str(esp[45:62]).lower(), str(esp[71:88]).lower(), int(esp[97:100])
    esp_mac, near_mac= str(esp_mac[2:-1]), str(near_mac[2:-1])
    timestamp = str(esp[17:34])
    espAlias    = "B/F/Z" # ASIGNAR ALIAS EN DB
    near_mac_list = []
    esp_mac_list = []

    antena_esp = ['4c:11:ae:8b:4c:94']
    known_esp = []
    #'fe:24:27:b8:d9:13', 'fd:04:ce:a4:90:e8'

    objectIdentifier = esp_mac + ', ' + near_mac
    collection_count = collection.count_documents({})

    print('\n\nLIVE DATA: \ntime: {} \n near_mac recibido: {} \n RSSI {}\n############'.format(timestamp, near_mac, rssi))

    if collection_count == 0:
        print('NUEVO OBJETO NEAR MAC: {}, RSSI {} \n'.format(near_mac, rssi))
        collection.insert_one({"_id": 'objectIdentifier', "SISTEMA INICIADO": True})
        #collection.insert_one({"_id": objectIdentifier}, {"near_mac ": near_mac, "rssi": rssi, "timestamp": timestamp})
        time.sleep(1)
    else:
        
        collection.update_one({"_id": objectIdentifier}, {'$set':{"rssi": rssi}})
        print('DB DATA: \n esp_mac: {} \n near_mac: {} \n RRSI{} rssi \n- - - - - - -\nguardado en DB\n- - - - - - -\n\n'.format(esp_mac, near_mac, rssi))

        #registerer()
        #indoor_data = {"_id": esp_mac + ', ' + near_mac, "near_mac": near_mac, "rssi": rssi}
        #collection.insert_one(indoor_data)


        time.sleep(1)

'''
El sistema funciona a medias:
 - Hay que crear un def o un class al que se le pueda llamar para 
    registrar una near_mac que no sea conocida


'''

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



