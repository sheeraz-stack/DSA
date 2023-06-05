#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# In[61]:


myStr ="leetcode"
while myStr != "":
    slen = len(myStr)
    ch = myStr[0]
    myStr = myStr.replace(ch, "")
    slen1 = len(myStr)
    if slen1 == slen-1:
        print ("First non-repeating character = ",ch)
        break;
    else:
        print ("No Unique Character Found!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




