#!/usr/bin/env python
# coding: utf-8

# In[10]:


#question 26
salary=int(input("enter your salary"))
if salary>=5000:
    hra=salary*0.15
    da=salary*1.5
    grosssalary=hra+da+salary
    print("Gross salary",grosssalary)
else:
    hra=salary*0.10
    da=salary*1.1
    grosssalary=hra+da+salary
    print("gross salary",grosssalary)


# In[ ]:




