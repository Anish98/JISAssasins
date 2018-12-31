#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Question 7

n=int(input("enter a no"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print ("the total sum of digit is:",tot) 


# In[ ]:




