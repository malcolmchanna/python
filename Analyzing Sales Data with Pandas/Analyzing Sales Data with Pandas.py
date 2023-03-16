#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/datagy/mediumdata/master/sales_data_sample.csv")


# In[ ]:


# Clean the data
df = df.drop(columns=['Unnamed: 0'])  # Remove unnecessary column
df = df.dropna()  # Remove any rows with missing values
df = df.rename(columns={'Order Date': 'order_date', 'Product': 'product', 'Sales': 'sales'})  
# Rename columns


# In[ ]:


# Perform basic analysis
total_sales = df['sales'].sum()
average_sales = df['sales'].mean()
orders_per_customer = df.groupby('Customer Email')['order_date'].count().mean()


# In[ ]:


# Visualize the data
monthly_sales = df.groupby(pd.to_datetime(df['order_date']).dt.to_period('M'))['sales'].sum()
monthly_sales.plot(kind='bar', xlabel='Month', ylabel='Sales', title='Monthly Sales')

product_sales = df.groupby('product')['sales'].sum()
product_sales.plot(kind='pie', autopct='%1.1f%%', title='Product Sales')

plt.show()


# In[ ]:


# Export the cleaned data
df.to_csv('cleaned_sales_data.csv', index=False)


# In[ ]:





# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




