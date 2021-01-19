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


DBS=['facebook_mongo']


try:
    dbc=server.create('facebook_mongo_couch')
except:
    dbc=server['facebook_mongo_couch']

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))

                    documents["_id"]=str(documents["_id"]["$oid"])


                    print(documents)
                    doc=dbc.save(documents)

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e


# In[ ]:




