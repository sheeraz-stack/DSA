#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 


# In[14]:


def floorSqrt(x):
    if (x == 0 or x == 1):
        return x
    i = 1
    result = 1
    while (result <= x):

        i += 1
        result = i * i

    return i - 1
x = 8
print(floorSqrt(x))


# In[ ]:




