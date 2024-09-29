#!/usr/bin/env python
# coding: utf-8

# In[13]:


#create a list initialised with months of the year
mylist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#create a tuple initialised with months of the year
mytuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#create a set initialised with months of the year
myset = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}

#create a dictionary initialised with months of the year
mydict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 10
}

# print list type and contents
print(type(mylist))
for x in mylist:
    print(x)
    
# print tuple type and contents
print(type(mytuple))
for x in mytuple:
    print(x)
    
# print set type and contents
print(type(myset))
for x in myset:
    print(x)
    
# print dict type and contents
print(type(mydict))
for x in mydict:
    print(x)


# In[ ]:




