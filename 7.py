#!/usr/bin/env python
# coding: utf-8

# In[8]:


from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

CLIENT = couchdb.Server('http://root:root@localhost:5984/')

try:
    print('cocuh connection: Success')
except ConnectionFailure as e:
    print('Couch connection: failed', e)
    
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.0gcep.mongodb.net/add?retryWrites=true")
DBm = client.get_database('facebook_mongo_couch_atlas')
DBma =DBm.add

try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    
DBc=CLIENT['facebook_mongo_couch']

for db in DBc:
    try:
        DBma.insert_one(DBc[db])
        print('Data saved mongoDB Atlas')
    except TypeError as et:
        print('current document raised error: {}'.format(et))
        SKIPPED.append(db)
        continue
    except Exception as e:
        raise e


# In[ ]:





# In[ ]:




