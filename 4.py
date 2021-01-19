#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import sqlite3
import json
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


# In[15]:


con=sqlite3.connect("database.db")
dfsqlite=pd.read_sql_query("SELECT * FROM compras", con)
dfsqlite


# In[16]:


result=dfsqlite.to_json(orient="records")
parsed = json.loads(result)
json.dumps(parsed)


# In[17]:


CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


# In[18]:


for data in parsed:
    try:
        db = CLIENT.sqlite_mongo
        db.data.insert_one(data)
        print("Guardado")
    except Exception as e:
        print("No se pudo guardar")


# In[ ]:




