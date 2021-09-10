import os
import json
import time
import datetime
import paho.mqtt.client
import pymongo
from  pymongo import MongoClient
from config import *

class ESP32(object):
    
    def on_connect(client, userdata, flags, rc):
        #print("rc: " + str(rc))
        print('USUARIO: (%s)' % client._client_id)
        #Subscribe to topic
        client.subscribe('indoor', 0) #client.subscribe('topic', qos)

    #Receive gateway and devices data
    def on_message(client, userdata, message):
        esp = message.payload
        esp_mac, near_mac , rssi = str(esp[45:62]), str(esp[71:88]), int(esp[97:100])
        esp_mac, near_mac= str(esp_mac[2:]), str(near_mac[2:])
        espAlias    = "B/F/Z" # ASIGNAR ALIAS EN DB
        print("\n", "esp_mac ",esp_mac[2:],"\n", "near_mac ",near_mac[2:], "\n", "RRSI ",rssi)
        collection.insert_one({"esp_mac": esp_mac.lower(), "near_mac": near_mac.lower(), "rssi": rssi})
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



