#!/usr/bin/env python
# coding: utf-8

# # In Part we are going to learn about
# 
# StringIO
# Pandas read_csv

# In[10]:


### Reading Different Data sources with the help of pandas
from io import StringIO
import pandas as pd


# In[24]:


df=pd.read_csv('mercedesbenz.csv')
type(df)
df.head(10)


# In[ ]:





# In[ ]:





# In[17]:


data = ('col1,col2,col3 \n'
        'x,y,e\n'
        'y,u,7\n'
        'l,7,8')


# In[18]:


type(data)


# In[19]:


##in memeory file format object
StringIO(data)


# In[20]:


pd.read_csv(StringIO(data))


# In[22]:


#use-cols function
pd.read_csv(StringIO(data) , usecols=['col1' ,'col2']) 


# In[32]:


df= pd.read_csv('mercedesbenz.csv' , usecols=['X0','X1','X2','X3','X4','X5','X6','X8'])
df.head(10)


# In[33]:


df.to_csv('test.csv')


# In[34]:


df.to_csv('test.csv' ,index= False)


# In[40]:


##datatypes in csv
data = ('a,b,c,d\n'
            '1,2,3,4\n'
            '5,6,7,8\n'
            '9,10,11')
df = pd.read_csv(StringIO(data))


# In[41]:


df.info()


# In[43]:


df = pd.read_csv(StringIO(data) , dtype = float)
df.info()


# In[48]:


df.isnull().sum() ==0


# In[57]:


df['a'][:]


# In[58]:


df[['a' , 'b']][2:]


# In[ ]:


##datatypes in csv
data = ('a,b,c,d\n'
            '1,2,3,4\n'
            '5,6,7,8\n'
            '9,10,11')


# In[66]:


df = pd.read_csv(StringIO(data) ,dtype={'a':float,'b':int  })
df.head()


# In[67]:


df.info()


# In[69]:


df.dtypes


# In[ ]:


data = ('index,a,b,c\n'
           '4,apple,bat,5.7\n'
            '8,orange,cow,10')


# In[72]:


pd.read_csv(StringIO(data),index_col=0)


# In[ ]:


# use index cols and usecols
data = ('a,b,c\n'
           '4,apple,bat\n'
            '8,orange,cow')


# In[73]:


pd.read_csv(StringIO(data),usecols=['a','b','c'],index_col=0)


# In[75]:


pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')           

