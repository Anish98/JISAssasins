#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 12
def reverseword(s):
    w=s.split(" ")
    nw=[i[::-1]for i in w]
    ns=" ".join(nw)
    return ns
s=input("enter a sentence")
print (reverseword(s))


# In[ ]:




