#!/usr/bin/env python
# coding: utf-8

# # Topic Cover
# Pandas Dataframe
# Pandas Series
# Pandas Basic Operations

# In[2]:



import pandas as pd
import numpy as np


# In[3]:


np.arange(0,20).reshape(5,4)


# In[14]:


## Create Dataframe
df=pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1",
                                                      "Row2","Row3",
                                                      "Row4","Row5"],columns=["Column1",
                                                                             "Column2",
                                                                             "Column3",
                                                                             "Column4"])
print(df.head()      , "\n\n")
print(df.tail()      , "\n\n")
print(type(df)       , "\n\n")
print(df.info()      , "\n\n")
print(df.describe()  , "\n\n")
print(df.info()      , "\n\n")


# In[15]:


##Indexing
## columnname,rowindex[loc],rowindex columnindex number[.iloc]
df.head()


# In[ ]:





# In[11]:


##columnname
type(df['Column1'])


# In[12]:


df[['Column1','Column2','Column3']]


# In[13]:


##using row index name loc
df.loc[['Row3','Row4']]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:





# In[16]:


df.iloc[2:4,0:2]


# In[17]:


df.iloc[2:,1:]


# In[18]:


##convert dataframe into arrays
df.iloc[:,1:].values


# In[19]:


## Basic operations
df.isnull().sum()


# In[20]:


df=pd.DataFrame(data=[[1,np.nan,2],[1,3,4]],index=["Row1",
                                                      "Row2"],columns=["Column1",
                                                                             "Column2",
                                                                             "Column3",
                                                                             ])
df


# In[21]:


df.isnull().sum()


# In[24]:


df.isnull().sum()==0


# In[25]:


df['Column3'].value_counts()


# In[26]:


df['Column2'].unique()


# In[27]:


df[df['Column2']>2]

