#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Question 8
def func(a,b):
    a='new-value'
    b=b+1
    return a,b
x,y = func('old-value',99)
print(x,y)


# In[ ]:




