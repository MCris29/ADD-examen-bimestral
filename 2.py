#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


# In[2]:


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))   

response = requests.get("https://spanish.alibaba.com/apparel/men-s-clothing/p3_p127726318?spm=a27aq.13924097.7644240160.18.51875db0TA5BZ7")
soup = BeautifulSoup(response.content, "lxml")

Product=[]
Value=[]
Price=[]


# In[3]:


post_product=soup.find_all("div", class_="offer-row product-subject")
post_value=soup.find_all("span", class_="moq-value")
post_price=soup.find_all("span", class_="price")


# In[4]:


for element in post_product:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Product.append(limpio.strip())

for element in post_value:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Value.append(limpio.strip())

for element in post_price:
    element=str(element)
    element=element.replace('<!-- -->','')
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Price.append(limpio.strip())


# In[5]:


CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


# In[6]:


data={}
i=0
for element in Product:
    try: 
        data={
            'Producto':Product[i],
            'Valor':Value[i], 
            'Precio':Price[i]
        }
        i=i+1
        
        CLIENT.webscraping_mongo.col_webs_mongo.insert_one(data)
        print("Guardado")
    
    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[ ]:




