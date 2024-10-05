#!/usr/bin/env python
# coding: utf-8

# In[11]:


import re

# make a regular expression for valid email address
# valid email address starts with word characters, can have . or - before @
# and then any word character . followed by a 2 or 3 letter domain 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      
# function definition for validating email address 
def check_valid_address(email):  
    # pass the regualar expression and the string in search() method 
    # and if successful then print out username and domain
    count = 0
    
    if(re.search(regex,email)):
        # check number of @ present
        count = email.count('@')
        # if only 1 @ then valid
        if count == 1:
            print("email: " + email,", ", end=" ")
            print("username: " + email.split("@")[0],", ", end=" ")
            print("host: " + email.split("@")[1], end=" ")
        # if more than 1 @ exists then return invalid message
        else:
            print("Not a valid email address")
    # if unsuccessful then return invalid message
    else:  
        print("Not a valid email address")

# main code
# ask user for a valid email address
email_address = input("Please input your email address: ")
# pass email address to check function
check_valid_address(email_address)


# In[ ]:




