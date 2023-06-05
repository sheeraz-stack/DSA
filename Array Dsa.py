#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


# In[20]:


def pushZerosToEnd(arr,n):
    count = 0 
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count] = 0
        count += 1
arr = [0,1,0,3,12]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)



# In[ ]:




