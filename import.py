import pymongo
import json
import re
from bson import ObjectId
import os

client = pymongo.MongoClient("mongodb://localhost:27017")
dblsit = client.list_database_names()
db = client.MCU_CourseDB
Courses = db.test

str = open('Data'+os.sep+'data.json', encoding="utf-8").read()
data = []
data.extend(json.loads(str))
for i in range(len(data)):
    data[i]['_id'] = ObjectId(re.findall("'(.*)'", data[i].get('_id').__repr__())[0])
    data[i]['createdAt'] = ObjectId(re.findall("'(.*)'", data[i].get('createdAt').__repr__())[0]).generation_time
    data[i]['modifiedAt'] = ObjectId(re.findall("'(.*)'", data[i].get('modifiedAt').__repr__())[0]).generation_time
Courses.insert_many(data)
print(data[0])
client.close()