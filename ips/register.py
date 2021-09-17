import pymongo
from  pymongo import MongoClient
from config import *
from receiver import near_mac


antena_esp = ['4c:11:ae:8b:4c:94']
known_esp = ['fe:24:27:b8:d9:13', 'fd:04:ce:a4:90:e8']


esp_active = 'fe:24:27:b8:d9:13'



print(near_mac)
#def registerer(near_mac):
#    indoor_data = {"_id": esp_mac + ', ' + near_mac, "near_mac": near_mac, "rssi": rssi}
#    collection.insert_one(indoor_data)


#for antena in ESP_MACS:
#    if antena == esp_transmisor:
#        print(antena)
#        print('hola')
#        esp_transmisor = 'fd:04:ce:a4:90:e7'
#    elif antena != esp_transmisor:
#        print('NO')


known_esp.append(esp_active)

#print(known_esp)

