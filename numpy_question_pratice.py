#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Question : Create a 1D array of numbers from 0 to 9
# Output : #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


import numpy as np
x = np.arange((10),True, dtype = bool)
x


# In[41]:


# Question : Create a 3×3 numpy array of all True’s

arr = np.full((3,3),True, dtype = bool )
arr1 = np.full((9),True, dtype = bool ).reshape(3,3)
arr2 = np.ones((3,3), dtype=bool)
print("\n",arr)
print("\n",arr1)
print("\n",arr2)


# In[43]:


# Question : Extract all odd numbers from array
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([1, 3, 5, 7, 9])

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
filters = arr[arr%2 == 1]
filters


# In[75]:


# Question: Replace all odd numbers in arr with -1
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

arr = np.arange(0,10)
arr[arr%2 == 1] = -1
arr


# In[79]:


# Question: Replace all odd numbers in arr with -1 without changing arr
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: out
# array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
# arr
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr = np.arange(0,10)
copy = np.copy(arr)
copy[copy%2 == 1] = -1
print("print orginal\n",arr)
print("print modify\n",copy)


# In[80]:


# Question: Convert a 1D array to a 2D array with 2 rows
# input: np.arange(10)
# output array([[0, 1, 2, 3, 4],
#               [5, 6, 7, 8, 9]])
arr = np.arange(10).reshape(2,5)
arr


# In[96]:


# Question: Stack arrays a and b vertically
# input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)

# output: array([[0, 1, 2, 3, 4],
#                [5, 6, 7, 8, 9],
#                [1, 1, 1, 1, 1],
#                [1, 1, 1, 1, 1]])

#solution

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print("orginal a array:\n",a)
print("orginal b array:\n",b)

join = np.vstack((a,b))  #concatenate 
join


# In[2]:


# Input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)
# Output: array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#                [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
join = np.hstack((a,b))
join


# In[12]:


# Question: Get the common items between a and b
# Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#        b = np.array([7,2,10,2,7,4,9,4,9,8])
# Output: array([2, 4])

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# In[13]:


# Input: a = np.array([1,2,3,4,5])
#        b = np.array([5,6,7,8,9])
# Output: array([1,2,3,4])
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
np.setdiff1d(a,b)


# In[14]:


# Question: Get the positions where elements of a and b match
# Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#        b = np.array([7,2,10,2,7,4,9,4,9,8])
# Output: (array([1, 3, 5, 7]),)

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a ==b)


# In[23]:


#Question: Get all items between 5 and 10 from a.
# Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
# Output: (array([6, 9, 10]),)

a = np.array([2, 6, 1, 9, 10, 3, 27])
a[(a >= 5) & (a <= 10)]


# In[6]:


# Question: Swap columns 1 and 2 in the array arr.

# Input:
import numpy as np
arr = np.arange(9).reshape(3,3)
print("orginal\n: " ,arr)

print("orginal\n: " ,arr[:, [1,0,2]] )


# In[9]:


# Question: Swap rows 1 and 2 in the array arr:
# Input: 
arr = np.arange(9).reshape(3,3)
print('Original array')
print(arr)
print('modified')
arr[[1,0,2],:]


# In[12]:


# Question: Reverse the rows of a 2D array arr.
# Input:
arr = np.arange(9).reshape(3,3)

print('Original array')
print(arr)
print('Modified array')
print(arr[::-1,:])


# In[15]:


# Question: Reverse the columns of a 2D array arr.
arr = np.arange(9).reshape(3,3)
print('Original array')
print(arr)
print('Modified array')
print(arr[:,::-1])

