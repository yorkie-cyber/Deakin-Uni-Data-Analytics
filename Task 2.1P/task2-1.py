#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Fibonacci function non-recursive
def fibonacci_nonrecursive(terms):
    # first two numbers and count initialised
    num1, num2, count = 0, 1, 0

    # check if the number of terms is 1, if so only print 1 term - num1
    if terms == 1:
        print("Fibonacci sequence up to ",terms,": ",num1, end=" ")
    # otherwise loop through while the count is less than the required terms
    else:
        print("Fibonacci sequence up to ",terms,": ", end=" ")
        while count < terms:
            # check if it is the last iteration ,if so then no ", "
            if count == terms - 1:
                print(num1, end=" ")
            # otherwise add a ", " to the string
            else:
                print(num1,", ", end=" ")
            # nth is sum of (n-1)th and (n-2)th term
            nth = num1 + num2
            # update values for nxt iteration
            # num1 takes on num2 value
            num1 = num2
            # num2 takes on nth (sum) value
            num2 = nth
            # increase the count for the while loop
            count += 1

# initalise variable user_input for use with while loop
user_input = -1

#get valid input of positive integer from user
while user_input <= 0:
    # get integer input from user and cast to integer
    user_input = int(input('How many terms? '))
    # check that the input is greater than 0, if not then request another input
    if user_input <= 0:
        print("Please enter a positive integer, try again.")

#call the fibonacci_nonrecursive function passing the user input
fibonacci_nonrecursive(user_input)

