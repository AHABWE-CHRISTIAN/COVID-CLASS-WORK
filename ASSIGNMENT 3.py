#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import lxml.html as lh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


Covid = 'https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases'
page = requests.get(Covid)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
[len(T) for T in tr_elements[:12]]


# In[3]:


doc = lh.fromstring(page.content)


# Check the table headers

# In[4]:


tr_elements = doc.xpath('//tr')
col = [] #
i = 0
for t in tr_elements[0]: 
    i+=1
    name=t.text_content()
    print("%d:%s" % (i,name))
    col.append((name,[]))


# In[5]:


for j in range(1,len(tr_elements)): # Because header is the first row, data would be store in the subsequent rows.
    T = tr_elements[j] #T is j'th row
    
    if len(T)!=6: #if row is not size 3, //tr data is not from the table.
        break
        
    i = 0 #i is the index of the first column
    
    for t in T.iterchildren(): #iterate through each element of the row
        data=t.text_content()
            
        col[i][1].append(data) #append the data to the empty list of the i'th column
            
        i+=1 #increment i for the next column


# In[15]:


[len(C) for (title,C) in col]


# Displays the data frame with three columns.

# In[6]:


Dict = {title:column for (title,column) in col}
df = pd.DataFrame(Dict)


# In[7]:


df.head()


# In[18]:


df.tail()


# In[19]:


df.describe()


# In[20]:


df.shape


# Clean the Data
# Remove row 0 from the head
# 

# In[21]:


dfc =df.drop([df.index[0]])
dfc.head()


# 

# 

# data types

# In[27]:


dfc.dtypes


# In[ ]:




