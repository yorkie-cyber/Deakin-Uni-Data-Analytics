#!/usr/bin/env python
# coding: utf-8

# In[25]:


# initalise variable squares_input for use with while loop
squares_input = -1

# use whie loop until valid input received - integer and greater than 0
while squares_input <= 0:
    # get integer input from user and cast to integer
    squares_input = int(input('Please input an integer number: '))
    # check that the value entered is greater than 0
    if squares_input <= 0:
        print("Sorry the input needs to be an integer greater than 0, please try again.")

# use of nested for loops to create a square based on input
# for loop 1 printing out number of lines
for x in range(squares_input):
    # for loop 2 printing out number of columns
    for y in range(squares_input):
        print(" * ", end=" ")
    # go to new line after finishing printing each line
    print("\n")


# In[ ]:




