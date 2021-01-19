#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb


# In[2]:


URL = 'http://root:root@localhost:5984'
print(URL)

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


# In[3]:


CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


# In[4]:


db = server['twitter_couch']

for docid in db.view('_all_docs'):
    try:
        id=docid['id']
        data=db[id]
        print(data)
        CLIENT.twitter_couch_mongo.col_twitter_couch_mongo.insert_one(data)
    
    except Exception as e:
        raise e


# In[ ]:




