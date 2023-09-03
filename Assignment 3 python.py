#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function.

[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[2]:


player_score = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[3]:


sorted(player_score , key = lambda x:x[1])


# In[5]:


Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[7]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(map(lambda x :x**2,a))


# In[ ]:


Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions

Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


# In[20]:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_tuple = tuple(map(lambda x: x, my_list))

print(my_tuple)  


# In[ ]:


Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.


# In[14]:


from functools import reduce

def multiply(x, y):
    return x * y

numbers = list(range(1, 26))

product = reduce(multiply, numbers)

print(product)


# In[19]:


#Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.

list1 = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x : x%2 == 0 or x%3 ==0,list1))


# In[ ]:





# In[ ]:





# In[ ]:




