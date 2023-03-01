#!/usr/bin/env python
# coding: utf-8

# In[2]:


# multiply tow array
import numpy as np
nums1 = np.array([[2, 5, 2],
              [1, 5, 5]])
nums2 = np.array([[5, 3, 4],
              [3, 2, 5]])

newarr = np.multiply(nums1,nums2)
print(newarr)


# In[7]:


#Write a NumPy program to swap rows and columns of a given array in reverse order.
nums = np.array([[[1, 2, 3, 4],
               [0, 1, 3, 4],
               [90, 91, 93, 94],
               [5, 0, 3, 2]]])

print(nums[::-1, ::-1])
nums = np.array([1, 2, 3, 4])
print(nums[-1])


# In[19]:


#Write a NumPy program to create a 4x4 array, now create a new array from the said array swapping first and last, second and third columns.
#Create the array using numpy.arange which returns evenly spaced values within a given interval.
import numpy as np

nums = np.arange(16 , dtype= 'int').reshape(-1,4) 
print("orginal array \n",nums)
print("first to last\n", nums[:,::-1])


# In[32]:


#Write a NumPy program to replace all numbers in a given array which is equal, less and greater to a given number.

nums = np.array([[4,5,9],
                 [5,9,6],
                 [2,5,7]])
print("orginal dataset\n", nums)
greater = 3
lesser = 8
print("replace where nums equal to " , greater, "with" , lesser)
print(np.where(nums == greater,lesser, nums))
print("replace where nums lesser to " , greater, "with" , lesser)
print(np.where(nums < greater,lesser, nums))
print("replace where nums lesser to " , greater, "with" , lesser)
print(np.where(nums > greater,lesser, nums))


# In[ ]:


#Write a NumPy program to extract all numbers from a given array which are less and greater than a specified numbe


# In[2]:


nums = np.array([[4,5,9],
                 [5,9,6],
                 [2,5,7]])

print("orginal data set\n" , nums  )
g = 3
l = 6

x = np.where(nums > g,l,nums)
print()


# In[ ]:





# In[21]:


import numpy as np
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
arr1 = np.array(list)
arr2 = arr1.reshape(5,5)
print(arr2)
#np.zeros((4,5))
#np.arange(1,20,2).reshape(5,2,1)
arr2[arr2%2 == 0] #EDA
arr2[arr2%2 == 1] #EDA
arr2[arr2  >3] #EDA
arr2 >2 


# In[1]:


#difference axis 1
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0 ) #default
print(arr)

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2), axis=0 ) #default
print(arr)


# In[39]:


arr1 = np.array([[3,2,7] , [3,4,5]])
arr2 = np.array([6,7,8,11,9,10])

search = np.searchsorted(arr,[7,9,10])
print(search)


# In[40]:



arr1 = np.array([[3,2,7] , [3,4,5]])
arr2 = np.array([6,7,8,11,9,10])

search = np.where(arr2%2 == 0)
print(search)


# In[41]:


arr2 = np.array([6,7,8,11,9,10])
sort = np.sort(arr2)
print(sort)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




