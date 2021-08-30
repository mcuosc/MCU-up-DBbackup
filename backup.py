import pymongo
import json
import re
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_SRV = os.getenv('MONGO_SRV')
DB_NAME = os.getenv('DB_NAME')
COLLECTION = os.getenv('COLLECTION')

client = pymongo.MongoClient(MONGO_SRV)
db = client[DB_NAME]
collection = db[COLLECTION].find()

data = list(collection)
for i in range(len(data)):
    data[i]['_id'] = re.findall("'(.*)'", data[i].get('_id').__repr__())[0]
with open('data.json','w') as f:
    json.dump(data, f)
print("Success")
client.close()