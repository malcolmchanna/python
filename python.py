#!/usr/bin/env python
# coding: utf-8

# # slicing ( return a range of characters)  

# In[1]:


a = " muzamil   .channa"
print(a[3:6])
print(a[3:])
print(a[:3])
print(a[-3:])
print(a[:-3])
print(a[-5:-2])


# In[ ]:





# # modify

# In[24]:


print(a.upper())
print(a.lower())
print(a.replace("M", "c")) #capital word not work
print(a.replace("c", "m"))
print(a.strip()) #remove whitespace
print(a.split("c"))


# # String Concatenation

# In[34]:


a = "muzamil"
c = "channa"
print(a+c)
print(a +"   "+ c)


# # String Format

# In[54]:


a= "36"
print("this is muzamil" + a)
a="muzamil "
b="channa"
txt = "firsName {0} and LastName {1})"
print( txt.format(b,a) )

a = "this is \"muzamil\"channa  "
print(a)


# # Python Lists
# Lists are used to store multiple items in a single variable

# In[105]:


list= ["muzamil", "channa", "imran" , "channa"]
thislist= ["muzmail" , 6]  
print(list)
print(len(list))
print(type(thislist))

#Access Items


listaccess = ["muzamil ", "channa" , "kamran" , "jamil" ,"farhan", "shoaib"]
print(listaccess[2])
print(listaccess[-4])
print(listaccess[2:5])

listaccess[1:3] = ["ali", "yousaf"]
print(listaccess)

listaccess[1] = ["ali", "yousaf", "daniyal"]
print(listaccess)

listaccess.insert(2,"lala")
print(listaccess)

listaccess.append("ali")      #append
print(listaccess)        


listaccess.remove("shoaib")
print(listaccess)

listaccess.pop(1)

del list[0]
print(list)



# #sort list
# 
# m

# In[11]:


turple = ("apple" , "orange" ," banana")
print(len(turple))
print(type(turple))
print(turple[1:3])
print(turple[:2])
print(turple[:-2])


# In[21]:


y = list(turple)
y[1]= "kiwi"
turple = tuple(y)
print(turple)

y = list(turple)
y.append("muzamil")
turple = tuple(y)
print(turple)


# In[28]:


thisturple = ("apple" , "orange" ," banana")
y= ("graphes",)
thisturple += y
print(thisturple)

y = list(thisturple)
y.remove("orange")
x = tuple(y)
print(x)


# In[34]:


turple = ("muzamil", "karmarna" ," zubAUR", "muzamil", "karmarna" ," zubAUR")
(green, white, *blue) = turple
print(green)
print(white)
print(blue)


# In[39]:


turple = ("muzamil", "karmarna" ," zubAUR", "muzamil", "karmarna" ," zubAUR")
for i in range(len(turple)):
      print(turple[i])


# In[10]:


car = {
    "model" : "kiwi",
    "color" : "yellow",
    "year"   : 2022
}

car["brand"] = "brown"
print(car)
 
print( car["model"])

print(car.keys())
print(car.values())
print(car.get("model"))
print(car.items())

car.update({"song":20202})
print(car.pop("model"))


# In[29]:


a = 455
b = 45
if b > a:     print("b is greater then a")
elif a == b:  print("a and b are equal")
else: print("not")    


# In[32]:


print("A") if a<b else print("=")  if a ==b else print("not") 


# In[31]:


a = 345
b = 34
if a < b :
    print("if b lesse than show that")
 elif a == b:
    print("Equal")


# In[12]:


def function(email*):
    print("this is email:" + email[2])
    
    
function("malcolm@gmail.com", "malcolm", "oka")


# In[14]:


def my_function(child3, child2, child1, child5):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus", child5 = "Emil")


# In[24]:


def fruit(food):
 for x in (food):
  print(x)
li = ["km", "orange"]
fruit(li)


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




