#!/usr/bin/env python
# coding: utf-8

# # numpy

# In[12]:


import numpy as np
                                                                       #diminsion
a = np.array(42)                                                       #0
b = np.array([1,4,5,6])                                                #1
c = np.array([[1,4,5,6], [2,6,7,8]])                                   #2
d = np.array([[[12,45,67], [45,67,889]], [[23,45,45] , [34,567,45]]])  #03
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[103]:


a = np.array([[1,2,3,4] , [6,7,8,9]])
b = np.array([[[1,2,3,4], [5,6,7,8]] , [[1,2,3,4], [5,6,7,8]]])
print("2nd row",a[1,2])
print("3nd row",b[1,1,-2])

# SCLING 
k= np.array([1,2,3,4,5,6,8,9,10])

print("\n output1:  ", k[0:1]) # 0:1 , 0,8 , ::1, ::2 ::3 , :3, 3: 

#2D array with 3array
f = np.array([[23,26,27] , [28,29,30], [8,9,0]])
print("\n output2:  ",f[0:3,1])    #1 ke bd 2 chro kar 

#2D array with 2array
f = np.array([[23,26,27] , [28,29,30]])
print("\n output3:  ",f[0:2,1])    #1 ke bd 2 chro kar 

d = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print("\n output4: ",d[0:2,0:3,0:4])



# In[104]:


#copy vs view

copy = np.array([1,2,3,4,5]) 
x = copy.copy()
copy[0] = 8

print("\n output5:",x)
print("output5:",copy)

view= np.array([1,2,3,4,5]) 
x =view.view()
copy[0] = 8

print("\n output5:",x)
print("output5:",view)


# In[124]:


#shape
arr = np.array([[[1,2,3],
                 [4,5,6],[4,5,6]],
                [[7,8,9],
                [10,11,12],[4,5,6]]])
print(arr.shape)
    


# In[134]:


3reshape
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,1,3,14,15,16,17])
arr3 = arr2.reshape(3,3,2)
print(arr3)



# In[177]:


#iteration
#Iterating 3-D Arrays
aa = np.array([[[1,2],
              [3,4],
               [5,6],[7,8]]])
for x in aa:
  for y in x:
    for z in y:
     print(z)
#shorthand    
ab = np.array([1,2,3,4,5,6,7])
for x in np.nditer(ab):
 print(x)    


# In[193]:


aaa = np.array([[[1,2],
              [3,4],
               [5,6],[7,8]]])

for x in np.nditer(aaa): #  , flags = ['buffered'], op_dtypes="S" dnumberate
    #for x in np.ndenumerate(aaa):
  print(x)


# In[23]:


import numpy as np
arr = np.array([[1,2], [3,4]])
arr1 = np.array([[7,8], [10,11]])
con = np.concatenate((arr,arr1),axis=1)
print(con)
    
    
    


# In[32]:


#stack
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])
con = np.stack((arr,arr1))
print(con)
    


# In[ ]:





# In[ ]:





# In[33]:


#hstack | rows
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])
con = np.hstack((arr,arr1))
print(con)
    


# In[ ]:





# In[34]:


#vstack \coloumm
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])
con = np.vstack((arr,arr1))
print(con)


# In[ ]:





# In[35]:


#dstack \height
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])
con = np.dstack((arr,arr1))
print(con)


# In[42]:


arr = np.array([1,2,3,4,5,6,7,8,9,10])
splits = np.array_split(arr,2)
print(splits)


# In[56]:


arr = np.array([[1,2,3],[4,5,6] ,[7,8,9],[10,11,12], [13,18,19],[110,111,112]] )
splits = np.array_split(arr,2,axis=1)
print(splits)


# In[64]:


arr = np.array([[1,2,3],[4,5,6] ,[7,8,9],[10,11,12], [13,18,19],[110,111,112]] )
splits = np.vsplit(arr,2)
print(splits)


# In[87]:


#search
arr = np.array([1,2,3,4,5,6,7,8])
search = np.searchsorted(arr ,6 ,side = "left" )  #even /odd
print(search)


# In[89]:



arr = np.array([1,2,3,4,5,6,7,8])
search = np.searchsorted(arr ,[2,6,7] )  #even /odd
print(search)


# In[17]:


import numpy as np
arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])
con = np.concatenate((arr3,arr4) ,axis = 1)
print(con,"\n")

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
con = np.stack((arr3,arr4) ,axis = 1)
print(con)



# In[22]:


#arrayfilter
arrset = np.array([1,2,3,4,5,6,7,8,9,10])
x = np.array([True,False,True,False,True,False,True,False,False,False])
newarr = arrset[x]
print(newarr)


# In[30]:


arrset = np.array([1,2,3,4,5,6,7,8,9,10])
filter_arr = []

for element in arrset:
    if element%2 == 0 :
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arrset[filter_arr]
print(filter_arr)
print(newarr)


# In[32]:


arrset = np.array([1,2,3,4,5,6])

filter_arr= arrset > 2
newarr = arrset[filter_arr]
print(newarr)
print(filter_arr)

