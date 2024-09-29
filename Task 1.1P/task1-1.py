#!/usr/bin/env python
# coding: utf-8

# In[11]:


#import regular expression module
import re

# request user input and save to 'phrase' variable
phrase = input('Please input a phrase: ')

#split the user phrase by white space character and re.split
#command and save in 'split_phrase'
split_phrase = re.split("\s", phrase)
#loop throught the split phrase and print each word on a new line
for x in split_phrase:
    print(x)


# In[ ]:




