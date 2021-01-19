#!/usr/bin/env python
# coding: utf-8

# In[1]:


from facebook_scraper import get_posts
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import time


# In[2]:


CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


# In[3]:


i=1
for post in get_posts('fifa', pages=100, extra_info=True):
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        CLIENT.facebook_mongo.col_face_mongo.insert_one(doc)
        
    
        print("guardado")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[ ]:




