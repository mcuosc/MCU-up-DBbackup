import pymongo
import json
import re
import os
import time
import log
from dotenv import load_dotenv
load_dotenv()

MONGO_SRV = os.getenv('MONGO_SRV')
DB_NAME = os.getenv('DB_NAME')
COLLECTION = os.getenv('COLLECTION')
Log = log.Logger()

def backup():
    try:
        client = pymongo.MongoClient(MONGO_SRV)
        db = client[DB_NAME]
        collection = db[COLLECTION].find()
        data = list(collection)
        for i in range(len(data)):
            data[i]['_id'] = re.findall("'(.*)'", data[i].get('_id').__repr__())[0]
            data[i]['createdAt'] = re.findall("'(.*)'", data[i].get('_id').__repr__())[0]
            data[i]['modifiedAt'] = re.findall("'(.*)'", data[i].get('_id').__repr__())[0]
        filename = COLLECTION+time.strftime("_%Y%m%d_%H%M.json")
        with open("Data/"+filename,'w') as f:
            json.dump(data, f)
        client.close()
        Log.Info("Data is already save on "+time.strftime("%Y/%m/%d %H:%M:%S"))
        return True
    except:
        Log.Error("")
        return False