import pymongo
import json
import re

client = pymongo.MongoClient("")
db = client["MCU_CourseDB-dev"]
Courses = db.courses

collections =  Courses.find()
data = list(collections)
for i in range(len(data)):
    data[i]['_id'] = re.findall("'(.*)'", data[i].get('_id').__repr__())[0]
print(data[0])
with open('data.json','w') as f:
    json.dump(data, f)
client.close()