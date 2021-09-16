import os
import json
import time
import datetime
import pymongo
from  pymongo import MongoClient
from config import *


def main():
    results_all_data = collection.find()
    for r in results_all_data:
        print(r)


    
if __name__ == '__main__':
    main()


