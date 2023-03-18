#!/usr/bin/env python
# coding: utf-8

# # Creating DataFrames

# In[4]:


import pandas as pd
# From a dictionary
data = {'name': ['John', 'Alice', 'Bob'], 'age': [28, 24, 30]}
df = pd.DataFrame(data)

# From a list of dictionaries
data = [{'name': 'John', 'age': 28}, {'name': 'Alice', 'age': 24}, {'name': 'Bob', 'age': 30}]
df = pd.DataFrame(data)


# # Viewing DataFrames

# In[ ]:


# First few rows
df.head()

# Last few rows
df.tail()

# Summary statistics
df.describe()

# Data types of columns
df.dtypes

# Shape of the DataFrame
df.shape


# # Indexing and Slicing

# In[6]:


# By column name
df['name']

# By row index
df.loc[0]

# By row and column index
df.iloc[0, 1]

# Slicing rows
df[1:3]

# Slicing columns
df.loc[:, 'name':'age']


# 
# # Filtering Data

# In[7]:


# Single condition
df[df['age'] > 25]

# Multiple conditions
df[(df['age'] > 25) & (df['name'] != 'Bob')]

# Using isin()
df[df['name'].isin(['John', 'Alice'])]


# # Adding and Modifying Data

# In[8]:


# Adding a new column
df['height'] = [175, 163, 180]

# Modifying a column
df['age'] = df['age'] + 1


# # Grouping Data

# In[9]:


# Grouping by a column and aggregating
df.groupby('name').agg({'age': 'mean', 'height': 'max'})

# Grouping by multiple columns and aggregating
df.groupby(['name', 'age']).agg({'height': 'max'})


# # Sorting Data

# In[10]:


# By a single column
df.sort_values('age')

# By multiple columns
df.sort_values(['age', 'name'])

# In descending order
df.sort_values('age', ascending=False)


# # Pandas DataFrame
# 

# In[12]:



# Creating a DataFrame from a dictionary
data = {'name': ['John', 'Alice', 'Bob'], 'age': [28, 24, 30], 'city': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# Creating a DataFrame from a NumPy array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(arr, columns=['a', 'b', 'c'])

# Creating a DataFrame from a list of dictionaries
data = [{'name': 'John', 'age': 28, 'city': 'New York'}, 
        {'name': 'Alice', 'age': 24, 'city': 'Paris'}, 
        {'name': 'Bob', 'age': 30, 'city': 'London'}]
df = pd.DataFrame(data)

# Accessing columns and rows
df['name']
df.loc[0]
df.iloc[0, 1]

# Slicing
df.loc[1:2, 'age':'city']

# Filtering
df[df['age'] > 25]

# Grouping and aggregating
df.groupby('city').agg({'age': 'mean', 'name': 'count'})


# # Pandas Series

# In[13]:


# Creating a Series from a list
s = pd.Series([10, 20, 30, 40, 50], name='numbers')

# Accessing elements by index
s[0]
s.loc[1]
s.iloc[2]

# Slicing
s[:3]
s[1:4]

# Operations on a Series
s + 5
s * 2
s.mean()


# # Basic Operations

# In[14]:


# Renaming columns
df.rename(columns={'name': 'full_name'}, inplace=True)

# Dropping columns
df.drop('age', axis=1, inplace=True)

# Sorting by a column
df.sort_values('city')

# Adding a new column
df['salary'] = [50000, 60000, 70000]

# Filling missing values
df.fillna(0)

# Dropping missing values
df.dropna()


# In[ ]:


#StringIO

# Creating a DataFrame from a CSV string
import io
csv_string = 'name,age,city\nJohn,28,New York\nAlice,24,Paris\nBob,30,London\n'
df = pd.read_csv(io.StringIO(csv_string))

#read_csv

# Reading a CSV file
df = pd.read_csv('filename.csv') 
#read_json

# Reading a JSON file
df = pd.read_json('filename.json')
                                          #to_json

# Writing a DataFrame to a JSON file
df.to_json('filename.json')

                                        #json_normalize

# Normalizing JSON data
import json
json_data = '{"name": "John", "age": 28, "city": {"name": "New York", "country": "USA"}}'
data = json.loads(json_data)
df = pd.json_normalize(data)

