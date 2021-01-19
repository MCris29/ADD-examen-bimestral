#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from argparse import ArgumentParser
import requests
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import pandas as pd


# In[2]:


try:
    client = pymongo.MongoClient('mongodb+srv://root:root@cluster0.0gcep.mongodb.net/add?retryWrites=true')
    client.server_info()
    print('MongoDB Atlas connection: Success')
    
except pymongo.errors.ServerSelectionTimeoutError as error:
    print('MongoDB Atlas connection: failed', e)
    
except pymongo.errors.ConnectionFailure as error:
    print('MongoDB Atlas connection: failed', e)


# In[3]:


db = client.facebook_mongo_couch_atlas
col = db.add
    
data = col.find()

arr=[]
for i in data:
    arr.append(i)
    
pd.DataFrame([arr]).to_csv('facebook_mongo_couch_atlas_csv.csv', index=False)


# In[ ]:




