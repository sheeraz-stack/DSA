#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q - Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from
the input list. Use list comprehension to solve this problem.


# In[12]:


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")


# In[ ]:


Q - Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator
should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate
the execution time.


# In[23]:


def timer(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute
    
    return inner

@timer
def function_1():
    for i in range(100000):
        pass
function_1()


# In[ ]:


Q - Write a function called ‘calculate_mean’ that takes a list of numbers as input and returns the mean (average) of
the numbers. The function should calculate the mean using the sum of the numbers divided by the total count.


# In[24]:


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           
    avg = sum_num / len(num)
    return avg
print("The average is", cal_average( [10, 15, 20, 25, 30]))


# In[ ]:


Q - Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as input, representing two samples.
The function should perform a two-sample t-test and return the p-value. Use the ‘scipy.stats’ module in Python to calculate
the t-test and p-value.


# In[40]:


import numpy as np

group1 = np.array([14, 15, 15, 16, 13, 8, 14, 17, 16, 14, 19, 20, 21, 15, 15, 16, 16, 13, 14, 12])
group2 = np.array([15, 17, 14, 17, 14, 8, 12, 19, 19, 14, 17, 22, 24, 16, 13, 16, 13, 18, 15, 13])


# In[41]:


print(np.var(group1), np.var(group2))


# In[42]:


import scipy.stats as stats

stats.ttest_ind(a=group1, b=group2, equal_var=True)


# In[ ]:




