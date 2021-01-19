#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[2]:


ckey = "dp1YcCFbuFisgyW08hQXw5FUZ"
csecret = "g6OoqIQafYDHIT5NX7nHXAuvMaYZ7w0mEMcXCnv0Tqv77lAEGB"
atoken = "4828088801-Jphcoww77hPxZnaWio6tYq9GiX3b4Iq4rjnseZi"
asecret = "mi1sp1HbemU8yirTFj4wGY7Q1TSc9YoSJGIBJUlSDCDY7"


# In[3]:


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())


# In[4]:


server = couchdb.Server('http://root:root@localhost:5984/')
try:
    db = server.create('twitter_couch')
except:
    db = server['twitter_couch']


# In[5]:


twitterStream.filter(track=['fifa'])


# In[ ]:




