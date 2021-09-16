import os
import json
import time
import datetime
import pymongo
from  pymongo import MongoClient
from config import *


# Mostrar todos los resultados
'''
results_all_data = collection.find()
for r in results_all_data:
    data = r['data']
    print(data)
'''
# Mostrar todos los resultados con el filtro usado
'''
results_rssi = collection.find({'rssi':-91})
for r in results_rssi:
    #rssi_data = r['data']
    print(r)
'''

# Mostrar todos los resultados con el filtro usado
'''
results_esp_mac = collection.find({'esp_mac': '4c:11:ae:8b:4c:94'})
for r in results_esp_mac:
    #rssi_data = r['data']
    print(r)
'''


# Mostrar el primer dato con el filtro usado
#result_esp_mac = collection.find_one({'esp_mac': '4c:11:ae:8b:4c:94'})
#print(result_esp_mac)


number_of_rows = collection.count_documents({})
print(number_of_rows)