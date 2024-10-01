#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Fibonacci function recursive
def fibonacci_recursive(terms):
    # check if the number of terms is 1, if so only print 1 term
    if terms <= 1:
        return terms
    else:
        return(recur_fibo(terms-1) + recur_fibo(terms-2))

# initalise variable user_input for use with while loop
user_input = -1

#get valid input of positive integer from user
while user_input <= 0:
    # get integer input from user and cast to integer
    user_input = int(input('How many terms? '))
    # check that the input is greater than 0, if not then request another input
    if user_input <= 0:
        print("Please enter a positive integer, try again.")

print("Fibonacci sequence up to ",user_input,": ", end=" ")
# call the recursive function for the number of terms requested
for i in range(user_input):
    # check if it is the last iteration ,if so then call recursive function
    # do not add ", " to the end of string
    if i == user_input-1:
        print(fibonacci_recursive(i), end=" ")
    # otherwise call recursive function and add a ", " to the string
    else:
        print(fibonacci_recursive(i),", ", end=" ")


# In[ ]:




